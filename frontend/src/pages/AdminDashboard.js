import React, { useState } from "react";
import ProfileDropdown from "../components/ProfileDropdown";
import AlertPill from "../components/AlertPill";

export default function AdminDashboard({ user, onLogout }) {

  const [file, setFile] = useState(null);
  const [documents, setDocuments] = useState([]);
  const [showProfile, setShowProfile] = useState(false);
  const [loading, setLoading] = useState(false);
  const [alert, setAlert] = useState(null);

  // Select file
  const handleFileChange = (e) => {
    const selected = e.target.files[0];

    if (!selected) return;

    if (selected.type !== "application/pdf") {
      setAlert({
        type: "error",
        message: "Please select a valid PDF"
      });
      return;
    }

    setFile(selected);
  };

  // DELETE (Frontend + Pinecone)
  const handleDelete = async () => {
    try {
      await fetch("http://127.0.0.1:8000/delete", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          company: user.company.toUpperCase()
        })
      });

      setDocuments([]);
      setFile(null);

      setAlert({
        type: "success",
        message: "Document deleted successfully"
      });

    } catch {
      setAlert({
        type: "error",
        message: "Delete failed"
      });
    }
  };

  // Upload
  const handleUpload = async () => {
    if (!file) {
      setAlert({
        type: "error",
        message: "Please select a PDF first"
      });
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("company", user.company.toUpperCase());

    setLoading(true);

    try {
      await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData
      });

      const newDoc = {
        name: file.name,
        pages: Math.floor(Math.random() * 30) + 1,
        size: (file.size / (1024 * 1024)).toFixed(2),
        date: new Date().toISOString().split("T")[0]
      };

      setDocuments([newDoc]);
      setFile(null);

      setAlert({
        type: "success",
        message: "Document uploaded successfully"
      });

    } catch {
      setAlert({
        type: "error",
        message: "Upload failed. Try again"
      });
    }

    setLoading(false);
  };

  return (
    <div className="admin-dashboard">

      {/* LOADING OVERLAY */}
      {loading && (
        <div className="upload-overlay">
          <div className="spinner"></div>
          <p>Uploading document...</p>
        </div>
      )}

      {/* ALERT */}
      {alert && (
        <AlertPill
          message={alert.message}
          type={alert.type}
          onClose={() => setAlert(null)}
        />
      )}

      {/* HEADER */}
      <div className="header">
        <div>
          <h2>SmartDocQA</h2>
          <p className="sub">your workplace knowledge, instantly</p>
        </div>

        <div
          className="profile-icon"
          onClick={() => setShowProfile(!showProfile)}
        >
          👤
        </div>
      </div>

      {showProfile && (
        <ProfileDropdown user={user} onLogout={onLogout} />
      )}

      {/* STATS */}
      <div className="stats">
        <div className="card">
          <p>Total Documents</p>
          <h3>{documents.length}</h3>
        </div>

        <div className="card">
          <p>Total Pages</p>
          <h3>
            {documents.reduce((sum, d) => sum + d.pages, 0)}
          </h3>
        </div>
      </div>

      {/* UPLOAD */}
      <div className="upload-section">
        <div className="upload-header">
          <h3>Upload Documents</h3>
          <button onClick={handleUpload}>Upload PDF</button>
        </div>

        <div className="upload-box">
          <label htmlFor="fileInput">

            {!file ? (
              <>
                Drag and drop PDF files here
                <p>or click the upload button above</p>
              </>
            ) : (
              <>
                <strong>{file.name}</strong>
               
              </>
            )}

          </label>

          <input
            id="fileInput"
            type="file"
            accept=".pdf"
            onChange={handleFileChange}
            hidden
          />
        </div>
      </div>

      {/* DOCUMENT LIST */}
      <div className="doc-list">
        <h3>Uploaded Documents</h3>

        {documents.length === 0 ? (
          <p>No documents uploaded</p>
        ) : (
          documents.map((doc, i) => (
            <div key={i} className="doc-item">
              <div>
                <p>{doc.name}</p>
                <span>
                 {doc.pages} pages • {doc.date}
                </span>
              </div>

              <button className="delete" onClick={handleDelete}>
                🗑
              </button>
            </div>
          ))
        )}
      </div>

    </div>
  );
}
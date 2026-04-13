import React, { useState } from "react";
import "../styles.css";
import AlertPill from "../components/AlertPill";
import {
  validateEmail,
  isCompanyEmail,
  validatePassword
} from "../utils/Validation";

export default function Login({ onLogin }) {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("User");
  const [showAlert, setShowAlert] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();

    // ✅ 1. empty check
    if (!email || !password) {
      setShowAlert(true);
      return;
    }

    // ✅ 2. email format validation
    if (!validateEmail(email)) {
      setShowAlert(true);
      return;
    }

    // ✅ 3. password validation
    if (!validatePassword(password)) {
      alert("Password must be at least 6 characters");
      return;
    }

    // ❌ 4. block gmail BEFORE extraction
   if (!isCompanyEmail(email)) {
  setShowAlert(true);
  return;
}

    // ✅ 5. SAFE extraction (no crash)
    const parts = email.split("@");

    if (!parts[1]) {
      setShowAlert(true);
      return;
    }

    const name = parts[0]
      .replace(".", " ")
      .replace("_", " ");

    const company = parts[1]
      .split(".")[0]
      .toUpperCase();

    const user = {
      email,
      role,
      name,
      company
    };

    // ✅ store user
    localStorage.setItem("user", JSON.stringify(user));

    // ✅ login
    onLogin(user);
  };

  return (
    <div className="login-container">

      {/* 🔥 ALERT PILL */}
      {showAlert && (
        <AlertPill
          message="Please use your organization email"
          onClose={() => setShowAlert(false)}
        />
      )}

      {/* HEADER */}
      <div className="login-header">
        <h1>SmartDocQA</h1>
        <p>your workplace knowledge, instantly</p>
      </div>

      {/* CARD */}
      <div className="login-card">
        <form onSubmit={handleSubmit}>

          {/* EMAIL */}
          <label>Email</label>
          <input
            type="email"
            placeholder="you@company.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />

          {/* PASSWORD */}
          <label>Password</label>
          <input
            type="password"
            placeholder="Enter your password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />

          {/* ROLE */}
          <label>Role</label>
          <select
            value={role}
            onChange={(e) => setRole(e.target.value)}
          >
            <option>User</option>
            <option>Admin</option>
          </select>

          {/* BUTTON */}
          <button type="submit" className="login-btn">
            ➜ Login
          </button>

        </form>
      </div>

    </div>
  );
}
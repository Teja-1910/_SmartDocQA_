import React, { useState, useEffect, useRef } from "react";
import ProfileDropdown from "../components/ProfileDropdown";

export default function Dashboard({ user, onLogout }) {

  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [showProfile, setShowProfile] = useState(false);
  const [showWelcome, setShowWelcome] = useState(true);
  const [showPill, setShowPill] = useState(true);
  const bottomRef = useRef(null);


  // Welcome pill timing
  useEffect(() => {
    const timer = setTimeout(() => {
      setShowPill(false);
    }, 2500);

    return () => clearTimeout(timer);
  }, []);

  useEffect(() => {
  bottomRef.current?.scrollIntoView({ behavior: "smooth" });
}, [messages]);
  

  // SEND MESSAGE
  const sendMessage = async () => {
    if (!message.trim()) return;

    const userMsg = { type: "user", text: message };

    setMessages((prev) => [...prev, userMsg]);
    setMessage("");
    setShowWelcome(false);

    setMessages((prev) => [
  ...prev,
  { type: "bot", text: "", loading: true }
]);

    try {
      const res = await fetch("http://127.0.0.1:8000/query", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          question: message,
          company: user?.company?.toLowerCase() || ""
        })
      });

      if (!res.ok) throw new Error("Server error");

      const data = await res.json();

      typeEffect(data?.answer || "No response available");

    } catch {
      typeEffect("No response available right now. Please try again later.");
    }
  };

  // SAFE TYPING EFFECT
  const typeEffect = (text = "") => {

    if (!text) {
      setMessages((prev) => [
        ...prev,
        { type: "bot", text: "No response available" }
      ]);
      return;
    }

    let i = 0;
    let current = "";

    const interval = setInterval(() => {
      current += text[i] || "";
      i++;

      setMessages((prev) => {
        const last = prev[prev.length - 1];

        if (last && last.type === "bot") {
          const updated = [...prev];
          updated[updated.length - 1] = {
            type: "bot",
            text: current
          };
          return updated;
        }

        return [...prev, { type: "bot", text: current }];
      });

      if (i >= text.length) clearInterval(interval);
    }, 18);
  };

  return (
    <div className="dashboard">

      {/* HEADER */}
      <div className="header">
        <div>
          <h2>SmartDocQA</h2>
          <p className="sub">Your Workplace Knowledge, Instantly</p>
        </div>

        <div
          className="profile-icon"
          onClick={() => setShowProfile(!showProfile)}
        >
          👤
        </div>
      </div>

      {/* PROFILE */}
      {showProfile && (
        <ProfileDropdown user={user} onLogout={onLogout} />
      )}

      {/* WELCOME PILL (FINAL PERFECT) */}
      <div className={`welcome-pill ${showPill ? "show" : "hide"}`}>
        Welcome back, <span>{user?.name || "User"}</span> 👋
      </div>

      {/* CHAT AREA */}
      <div className="chat-container">

        {showWelcome && (
          <div className="welcome-center">
            <div className="bot-icon">🤖</div>
            <h2>Welcome to SmartDocQA</h2>
          </div>
        )}

        <div className="messages">

          {messages.map((msg, i) => (
  <div key={i} className={`row ${msg.type}`}>

    {msg.type === "bot" && (
      <div className="avatar">🤖</div>
    )}

    <div className={`bubble ${msg.type}`}>
      {msg.loading ? (
        <div className="typing">
          <span></span>
          <span></span>
          <span></span>
        </div>
      ) : (
        msg.text
      )}
    </div>

    {msg.type === "user" && (
      <div className="avatar user-avatar">
        {user?.name?.charAt(0) || "U"}
      </div>
    )}
  <div ref={bottomRef}></div>
  </div>
))}

        </div>

      </div>

      {/* INPUT */}
      <div className="input-area">
        <div className="input-box">

          <input
            type="text"
            placeholder="Type your question here..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") sendMessage();
            }}
          />

          <button onClick={sendMessage}>
            ➤
          </button>

        </div>
      </div>

    </div>
  );
}
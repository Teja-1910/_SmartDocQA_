import React, { useState, useEffect } from "react";

export default function ProfileDropdown({ user, onLogout }) {

  const [darkMode, setDarkMode] = useState(false);

  // load saved mode
  useEffect(() => {
    const saved = localStorage.getItem("darkMode");
    if (saved === "true") {
      setDarkMode(true);
      document.body.classList.add("dark");
    }
  }, []);

  const toggleDarkMode = () => {
    const newMode = !darkMode;
    setDarkMode(newMode);

    if (newMode) {
      document.body.classList.add("dark");
    } else {
      document.body.classList.remove("dark");
    }

    localStorage.setItem("darkMode", newMode);
  };

  return (
    <div className="profile-dropdown">

      <div className="profile-top">
        <div className="avatar">👨🏻‍💻</div>
        <div>
          <p className="name">{user.name}</p>
          <p className="email">{user.email}</p>
        </div>
      </div>

      <div className="divider"></div>

      <div className="company-box">
        🏢 {user.company}
      </div>

      <div className="divider"></div>

      {/* DARK MODE */}
      <div className="dropdown-item">
        <div className="dropdown-left">
          🌙 <p>Dark Mode</p>
        </div>

        <label className="switch">
          <input
            type="checkbox"
            checked={darkMode}
            onChange={toggleDarkMode}
          />
          <span className="slider"></span>
        </label>
      </div>

      <div className="divider"></div>

      {/* LOGOUT */}
      <div className="dropdown-item logout" onClick={onLogout}>
        <div className="dropdown-left">
          ↪ <p>Logout</p>
        </div>
      </div>

    </div>
  );
}
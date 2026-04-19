import React, { useState, useEffect } from "react";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import AdminDashboard from "./pages/AdminDashboard";

function App() {
  const [user, setUser] = useState(null);

  // Load user + theme on start
  useEffect(() => {
    const storedUser = localStorage.getItem("user");

    if (storedUser) {
      setUser(JSON.parse(storedUser));
    }

    // apply saved theme
    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "dark") {
      document.body.classList.add("dark");
    }
  }, []);

  //  Logout
  const handleLogout = () => {
    localStorage.removeItem("user");
    setUser(null);
  };

  // Not logged in → Login page
  if (!user) {
    return <Login onLogin={setUser} />;
  }

  // Admin view
  if (user.role === "Admin") {
    return (
      <AdminDashboard
        user={user}
        onLogout={handleLogout}
      />
    );
  }

  // User view
  return (
    <Dashboard
      user={user}
      onLogout={handleLogout}
    />
  );
}

export default App;
import React, { useEffect, useState } from "react";

export default function WelcomePill({ name }) {

  const [visible, setVisible] = useState(true);

  useEffect(() => {
    // auto hide after 3 seconds
    const timer = setTimeout(() => {
      setVisible(false);
    }, 3000);

    return () => clearTimeout(timer);
  }, []);

  return (
    <div className={`welcome-pill ${visible ? "show" : "hide"}`}>
      Welcome back, <span>{name}</span>!
    </div>
  );
}
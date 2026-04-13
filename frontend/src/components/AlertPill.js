import React, { useEffect, useState } from "react";

export default function AlertPill({ message, type = "error", onClose }) {

  const [visible, setVisible] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      setVisible(false);

      setTimeout(() => {
        if (onClose) onClose();
      }, 300);

    }, 2500);

    return () => clearTimeout(timer);
  }, [onClose]);

  return (
    <div className={`alert-pill ${type} ${visible ? "show" : "hide"}`}>
      {type === "success" ? "✅" : "⚠"} {message}
    </div>
  );
}
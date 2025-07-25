import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/Login.css"; // ✅ Ensure path is correct relative to file
import { FaUser, FaLock } from "react-icons/fa"; // ✅ Icons!

function Login() {
  const [formData, setFormData] = useState({ username: "", password: "" });
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert("Login successful!");
    navigate("/dashboard");
  };

  return (
    <div className="login-page">
      <div className="login-card animated-fade-in">
        <h2 className="login-title">🌟 TechSister AI</h2>
        <form className="login-form" onSubmit={handleSubmit}>
          <div className="input-wrapper">
            <FaUser className="input-icon" />
            <input
              type="text"
              name="username"
              placeholder="Username"
              onChange={handleChange}
              required
            />
          </div>

          <div className="input-wrapper">
            <FaLock className="input-icon" />
            <input
              type="password"
              name="password"
              placeholder="Password"
              onChange={handleChange}
              required
            />
          </div>

          <button type="submit" className="login-btn glow-button">Login</button>
        </form>
      </div>
    </div>
  );
}

export default Login;

// src/components/pages/Signup.jsx
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { FaSun, FaMoon } from "react-icons/fa";
import "../styles/global.css"; // ✅ Ensure path is correct relative to file

function Signup() {
  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    email: "",
    username: "",
    password: "",
    location: "",
    age: ""
  });

  const [darkMode, setDarkMode] = useState(true);
  const navigate = useNavigate(); // ✅ Used for client-side navigation

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const toggleTheme = () => {
    setDarkMode(!darkMode);
    document.body.classList.toggle("light-mode");
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert("Signup successful!");
    navigate("/login"); // ✅ Correct client-side redirect
  };

  return (
    <div
      className={`signup-page ${darkMode ? "dark" : "light"}`}
      style={{
        backgroundImage: `url('https://cdn.pixabay.com/photo/2022/09/07/09/56/african-7438510_1280.jpg')`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        minHeight: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        padding: "20px",
      }}
    >
      {/* 🌞 / 🌙 Theme Toggle Button */}
      <div style={{ position: "absolute", top: 20, right: 20, cursor: "pointer" }} onClick={toggleTheme}>
        {darkMode ? <FaSun size={24} color="#f7a8f0" /> : <FaMoon size={24} color="#1a1a2e" />}
      </div>

      <div className={`signup-container age-${formData.age}`}>
        <h2>👩🏽‍💻 Join <span style={{ color: "#ff61d2" }}>TechSister AI</span> ✨</h2>
        <form className="signup-form" onSubmit={handleSubmit}>
          <input type="text" name="firstName" placeholder="First Name" onChange={handleChange} required />
          <input type="text" name="lastName" placeholder="Last Name" onChange={handleChange} required />
          <input type="email" name="email" placeholder="Email" onChange={handleChange} required />
          <input type="text" name="username" placeholder="Username" onChange={handleChange} required />
          <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
          <input type="text" name="location" placeholder="Location" onChange={handleChange} required />
          <select name="age" onChange={handleChange} required>
            <option value="">Select Age Group</option>
            <option value="under13">Under 13</option>
            <option value="13to16">13–16</option>
            <option value="17plus">17+</option>
          </select>
          <button type="submit">🚀 Sign Up</button>
        </form>
      </div>
    </div>
  );
}

export default Signup;

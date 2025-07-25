// src/App.js
import React, { useState } from "react";
import { Routes, Route,  } from "react-router-dom";
import Signup from "./components/pages/Signup";
import Login from "./components/pages/Login";
import Dashboard from "./components/pages/Dashboard";
import UserProfile from './components/pages/Dashboard';
import AiCoach from'./components/pages/AiCoach';
import CoursesPage from'./components/pages/CoursesPage';
import StudyMaterials from'./components/pages/StudyMaterials';


function App() {
  const [theme, setTheme] = useState("light");

  const toggleTheme = () => {
    setTheme(theme === "light" ? "dark" : "light");
    document.body.classList.toggle("light-mode");
  };

  return (
    <div className={`app-container ${theme}`}>
      <header>
        <h1 className="app-title">TechSister AI</h1>
        <button onClick={toggleTheme} className="theme-toggle-btn">
          {theme === "light" ? "🌙 Dark Mode" : "☀️ Light Mode"}
        </button>
      </header>

      <main>
        <Routes>
          <Route path="/" element={<Signup />} />
          <Route path="/login" element={<Login />} />
          <Route path="/dashboard" element={<Dashboard />} /> {/* ✅ This uses it */}
          <Route path="/profile" element={<UserProfile />} />
          <Route path="/ai-coach" element={<AiCoach />} />
          <Route path="/courses" element={<CoursesPage />} />
          <Route path="/materials" element={<StudyMaterials />} />


          {/* Add other routes as needed */}
          </Routes>
      </main>
    </div>
  );
}

export default App;

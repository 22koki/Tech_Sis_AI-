// src/components/pages/Dashboard.js
import React, { useState } from "react";
import { FaBook, FaUserFriends, FaUser, FaSun, FaMoon, FaChalkboardTeacher, FaComments, FaCheckCircle } from "react-icons/fa";
import '../styles/global.css';


function Dashboard() {
  const [darkMode, setDarkMode] = useState(true);
  const toggleTheme = () => {
    setDarkMode(!darkMode);
    document.body.classList.toggle("light-mode");
  };

  return (
    <div className={`dashboard-container ${darkMode ? 'dark' : 'light'}`}>
      {/* Toggle Button */}
      <div className="theme-toggle-btn" onClick={toggleTheme}>
        {darkMode ? <FaSun size={20} color="#f7a8f0" /> : <FaMoon size={20} color="#1a1a2e" />}
      </div>

      {/* Sidebar */}
      <aside className="sidebar">
        <h2>🌍 TechSister AI</h2>
        <nav>
          <ul>
            <li><FaUser /> Profile</li>
            <li><FaBook /> Courses</li>
            <li><FaCheckCircle /> Progress</li>
            <li><FaComments /> Confidence Journal</li>
            <li><FaChalkboardTeacher /> Mentor Match</li>
          </ul>
        </nav>
      </aside>

      {/* Main Content */}
      <main className="dashboard-main">
        <h1>Hey Sis, welcome back! 👋🏽</h1>
        <p className="tagline">Empowering girls to lead in tech. 🚀</p>

        <div className="dashboard-grid">
          <div className="card gradient-pink">
            <h3>👩🏾‍💻 Your Track</h3>
            <p><strong>Preferred:</strong> Entrepreneurship</p>
            <p><strong>Learning Style:</strong> Visual</p>
          </div>

          <div className="card gradient-purple">
            <h3>📚 Enrolled Course</h3>
            <p><strong>Title:</strong> Intro to Web Dev</p>
            <p><strong>Level:</strong> Beginner</p>
            <p><strong>Progress:</strong> 3/6 modules</p>
          </div>

          <div className="card gradient-orange">
            <h3>💬 Confidence Log</h3>
            <p>“I nailed that coding quiz today!”</p>
            <p><strong>Tone:</strong> 🌟 Positive</p>
          </div>

          <div className="card gradient-blue">
            <h3>🤝 Mentor Matched</h3>
            <p><strong>Mentor:</strong> Jane Mwangi</p>
            <p><strong>Goal:</strong> Build confidence in pitching ideas</p>
          </div>

          <div className="card gradient-green">
            <h3>📈 Session Feedback</h3>
            <p><strong>Was it helpful?</strong> ✅ Yes</p>
            <p>“She was patient and encouraging.”</p>
          </div>
        </div>
      </main>
    </div>
  );
}

export default Dashboard;

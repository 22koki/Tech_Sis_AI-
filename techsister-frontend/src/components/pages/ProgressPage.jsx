import React, { useEffect, useState } from "react";
import axios from "axios";
import "../styles/progress.css";

function ProgressPage() {
  const [progressList, setProgressList] = useState([]);

  useEffect(() => {
    fetchProgress();
  }, []);

  const fetchProgress = async () => {
    try {
      const res = await axios.get("/api/progress/");
      setProgressList(res.data);
    } catch (error) {
      console.error("Failed to fetch progress", error);
    }
  };

  return (
    <div className="progress-container">
      <h2>Your Learning Progress</h2>
      <div className="progress-grid">
        {progressList.map((item) => (
          <div className="progress-card" key={item.id}>
            <h4>{item.module_title || "Untitled Module"}</h4>
            <p>Course: {item.course_title || "N/A"}</p>
            <div className="progress-bar">
              <div
                className="progress-fill"
                style={{ width: `${item.percentage}%` }}
              ></div>
            </div>
            <p className="percentage">{item.percentage}% complete</p>
            <small>Last updated: {new Date(item.updated_at).toLocaleDateString()}</small>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ProgressPage;

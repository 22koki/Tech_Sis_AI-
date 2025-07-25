import React, { useEffect, useState } from "react";
import axios from "axios";
import "../styles/StudyMaterial.css"; // ✅ Ensure path is correct relative to file

function StudyMaterials() {
  const [materials, setMaterials] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get("http://localhost:8000/api/study-materials/")
      .then((res) => {
        setMaterials(res.data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching materials:", err);
        setLoading(false);
      });
  }, []);

  return (
    <div className="study-materials-page">
      <h2>📚 Study Materials</h2>

      {loading ? (
        <p>Loading...</p>
      ) : materials.length === 0 ? (
        <p>No study materials found.</p>
      ) : (
        <div className="material-grid">
          {materials.map((item) => (
            <div className="material-card" key={item.id}>
              <h3>{item.title}</h3>
              <p><strong>Subject:</strong> {item.subject}</p>
              <p><strong>Description:</strong> {item.description}</p>
              <a href={item.file} target="_blank" rel="noopener noreferrer">
                📥 Download / View
              </a>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default StudyMaterials;

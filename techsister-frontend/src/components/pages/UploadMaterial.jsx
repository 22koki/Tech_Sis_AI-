import React, { useState, useEffect } from "react";
import axios from "axios";

function UploadMaterial() {
  const [formData, setFormData] = useState({
    title: "",
    content: "",
    article: "",
    video: null,
    notes: null,
    pdf: null,
  });
  const [contentOptions, setContentOptions] = useState([]);

  useEffect(() => {
    axios.get("/api/educational-content/")
      .then((res) => {
        setContentOptions(res.data);
      })
      .catch((err) => console.error("Failed to fetch content options:", err));
  }, []);

  const handleChange = (e) => {
    if (["video", "notes", "pdf"].includes(e.target.name)) {
      setFormData({ ...formData, [e.target.name]: e.target.files[0] });
    } else {
      setFormData({ ...formData, [e.target.name]: e.target.value });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const submission = new FormData();
    Object.entries(formData).forEach(([key, value]) => {
      if (value) submission.append(key, value);
    });

    try {
      await axios.post("/api/study-materials/", submission, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      alert("Material uploaded successfully!");
    } catch (error) {
      console.error(error);
      alert("Upload failed.");
    }
  };

  return (
    <div className="upload-page">
      <h2>Upload Study Material</h2>
      <form onSubmit={handleSubmit} encType="multipart/form-data">
        <label>Material Title</label>
        <input type="text" name="title" onChange={handleChange} required />

        <label>Link to Educational Content</label>
        <select name="content" onChange={handleChange} required>
          <option value="">Select Content</option>
          {contentOptions.map((item) => (
            <option key={item.id} value={item.id}>{item.title}</option>
          ))}
        </select>

        <label>Video File</label>
        <input type="file" name="video" accept="video/*" onChange={handleChange} />

        <label>Notes File</label>
        <input type="file" name="notes" accept=".txt,.doc,.docx" onChange={handleChange} />

        <label>PDF File</label>
        <input type="file" name="pdf" accept="application/pdf" onChange={handleChange} />

        <label>Article Content (optional)</label>
        <textarea name="article" onChange={handleChange} rows="5" />

        <button type="submit">Upload Material</button>
      </form>
    </div>
  );
}

export default UploadMaterial;

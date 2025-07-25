import React, { useState } from "react";
import axios from "axios";
import "../styles/aiCoach.css"; // You can style this separately

function AICoach() {
  const [reflection, setReflection] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResponse(null);
    try {
      const res = await axios.post(
        "http://localhost:8000/api/reflect/",
        { reflection },
        {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
          },
        }
      );
      setResponse(res.data);
    } catch (err) {
      setResponse({ ai_response: "Something went wrong. Try again later." });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="ai-coach-container">
      <h2>🌸 TechSister AI Coach</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          value={reflection}
          onChange={(e) => setReflection(e.target.value)}
          placeholder="What's on your mind today?"
          required
        ></textarea>
        <button type="submit" disabled={loading}>
          {loading ? "Sending..." : "Get AI Encouragement 💬"}
        </button>
      </form>

      {response && (
        <div className={`ai-response-box tone-${response.tone}`}>
          <p><strong>AI Coach:</strong> {response.ai_response}</p>
        </div>
      )}
    </div>
  );
}

export default AICoach;

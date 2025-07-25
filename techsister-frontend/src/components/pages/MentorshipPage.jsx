import React, { useEffect, useState } from "react";
import axios from "axios";
import "../styles/mentorship.css";

function MentorshipPage() {
  const [match, setMatch] = useState(null);
  const [mentors, setMentors] = useState([]);
  const [goal, setGoal] = useState("");

  useEffect(() => {
    fetchMatch();
    fetchMentors();
  }, []);

  const fetchMatch = async () => {
    try {
      const res = await axios.get("/api/mentorship/match/");
      setMatch(res.data);
    } catch (error) {
      console.error("No active match");
    }
  };

  const fetchMentors = async () => {
    try {
      const res = await axios.get("/api/mentorship/mentors/");
      setMentors(res.data);
    } catch (error) {
      console.error("Error loading mentors", error);
    }
  };

  const handleRequestMatch = async (mentorId) => {
    try {
      await axios.post("/api/mentorship/request/", {
        mentor_id: mentorId,
        learning_goal: goal,
      });
      alert("Mentorship request sent!");
      fetchMatch();
    } catch (error) {
      console.error("Error requesting match", error);
    }
  };

  return (
    <div className="mentorship-container">
      <h2>Mentorship</h2>
      {match ? (
        <div className="match-info">
          <h3>You're matched with:</h3>
          <p><strong>{match.mentor_name}</strong></p>
          <p><em>{match.mentor_bio}</em></p>
          <p>Goal: {match.learning_goal}</p>
        </div>
      ) : (
        <>
          <h4>No match yet – Pick a mentor:</h4>
          <input
            type="text"
            placeholder="Your learning goal..."
            value={goal}
            onChange={(e) => setGoal(e.target.value)}
          />
          <div className="mentor-list">
            {mentors.map((mentor) => (
              <div key={mentor.id} className="mentor-card">
                <h5>{mentor.username}</h5>
                <p>{mentor.expertise}</p>
                <button onClick={() => handleRequestMatch(mentor.id)}>
                  Request Match
                </button>
              </div>
            ))}
          </div>
        </>
      )}
    </div>
  );
}

export default MentorshipPage;

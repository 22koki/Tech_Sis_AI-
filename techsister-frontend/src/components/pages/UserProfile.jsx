import React, { useEffect, useState } from "react";
import axios from "axios";
import "../styles/profile.css";

function UserProfile() {
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const token = localStorage.getItem("token"); // or sessionStorage if you're using that
        const response = await axios.get("http://localhost:8000/api/profile/", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        setProfile(response.data);
      } catch (error) {
        console.error("Error fetching profile:", error);
      }
    };

    fetchProfile();
  }, []);

  if (!profile) return <div className="profile-page">Loading profile...</div>;

  return (
    <div className="profile-page">
      <div className="profile-card animated-slide-in">
        <h2 className="profile-title">👩🏽‍💻 My Profile</h2>

        <div className="profile-info">
          <p><strong>Full Name:</strong> {profile.full_name}</p>
          <p><strong>Username:</strong> @{profile.username}</p>
          <p><strong>Age:</strong> {profile.age}</p>
          <p><strong>Focus Area:</strong> {profile.focus_area}</p>
          <p><strong>Interests:</strong> {profile.interests}</p>
          <p><strong>Joined:</strong> {profile.joined}</p>
        </div>

        <button className="edit-btn glow-button">Edit Profile</button>
      </div>
    </div>
  );
}

export default UserProfile;

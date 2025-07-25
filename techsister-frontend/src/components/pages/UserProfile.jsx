import React, { useEffect, useState } from 'react';
import api from '../api/axios';
import '../styles/UserProfile.css';  // ✅ Import the CSS styling

const UserProfile = () => {
  const [profile, setProfile] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get('/user-profiles/')
      .then((res) => {
        setProfile(res.data[0]);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Error fetching profile:', err);
        setLoading(false);
      });
  }, []);

  if (loading) return <p className="profile-loading">Loading profile...</p>;
  if (!profile) return <p className="profile-error">No profile found.</p>;

  return (
    <div className="profile-container">
      <div className="profile-card">
        <h2 className="profile-heading">👩🏾‍💻 My TechSister Profile</h2>
        <ul className="profile-list">
          <li><strong>Username:</strong> {profile.user}</li>
          <li><strong>Age:</strong> {profile.age}</li>
          <li><strong>Learning Style:</strong> {profile.learning_style}</li>
          <li><strong>Preferred Track:</strong> {profile.preferred_track || 'Not chosen yet'}</li>
          <li><strong>Track Decided:</strong> {profile.is_track_decided ? '✅ Yes' : '❌ No'}</li>
        </ul>
      </div>
    </div>
  );
};

export default UserProfile;

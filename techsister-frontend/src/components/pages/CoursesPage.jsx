import React, { useEffect, useState } from 'react';
import "../styles/courses.css"; // ✅ Ensure path is correct relative to filect relative to file

const CoursesPage = () => {
  const [courses, setCourses] = useState([]);
  const [expandedCourseId, setExpandedCourseId] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/api/courses/') // adjust to your actual URL
      .then(res => res.json())
      .then(data => setCourses(data))
      .catch(err => console.error('Failed to fetch courses:', err));
  }, []);

  const toggleExpand = (id) => {
    setExpandedCourseId(prev => (prev === id ? null : id));
  };

  return (
    <div className="courses-page">
      <h1 className="courses-title">📚 Explore Your Courses</h1>
      {courses.map(course => (
        <div key={course.id} className="course-card">
          <div className="course-header" onClick={() => toggleExpand(course.id)}>
            <h2>{course.title}</h2>
            <p><strong>Category:</strong> {course.category} | <strong>Level:</strong> {course.level}</p>
          </div>
          {expandedCourseId === course.id && (
            <div className="modules-list">
              {course.modules?.map((module, index) => (
                <div key={module.id || index} className="module-card">
                  <h3>{module.title}</h3>
                  <p>{module.content}</p>
                  {module.video && <a href={module.video} target="_blank" rel="noreferrer">🎥 Watch Video</a>}
                  {module.pdf && <a href={module.pdf} target="_blank" rel="noreferrer">📄 View PDF</a>}
                  {module.notes && <a href={module.notes} target="_blank" rel="noreferrer">📝 View Notes</a>}
                </div>
              ))}
            </div>
          )}
        </div>
      ))}
    </div>
  );
};

export default CoursesPage;

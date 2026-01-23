import React, { useState } from 'react';
import './App.css';

/**
 * Main App Component
 * A simple form-based UI for collecting subject and content from users
 * Features:
 * - Subject input field for form title
 * - Content textarea for detailed information
 * - Clear visual feedback on form submission
 * - Form validation before submission
 */
function App() {
  // State for subject input
  const [subject, setSubject] = useState('');

  // State for content input
  const [content, setContent] = useState('');

  // State to show feedback message after submission
  const [feedback, setFeedback] = useState('');

  /**
   * Handle form submission
   * Validates inputs and displays success/error messages
   */
  const handleSubmit = (e) => {
    e.preventDefault();

    // Validate subject is not empty
    if (!subject.trim()) {
      setFeedback('⚠️ Please enter a subject');
      return;
    }

    // Validate content is not empty
    if (!content.trim()) {
      setFeedback('⚠️ Please enter content');
      return;
    }

    // Show success message
    setFeedback('✓ Content saved successfully!');

    // Reset form fields after successful submission
    setSubject('');
    setContent('');

    // Clear feedback message after 3 seconds
    setTimeout(() => setFeedback(''), 3000);
  };

  /**
   * Handle subject input change
   * Updates state as user types
   */
  const handleSubjectChange = (e) => {
    setSubject(e.target.value);
  };

  /**
   * Handle content input change
   * Updates state as user types
   */
  const handleContentChange = (e) => {
    setContent(e.target.value);
  };

  return (
    // Main container with gradient background
    <div className="container">
      {/* Card wrapper for form */}
      <div className="card">
        {/* Header section */}
        <div className="header">
          <h1 className="title">📝 Spokeperson</h1>
          <p className="subtitle">Store Your Content</p>
        </div>

        {/* Form section */}
        <form onSubmit={handleSubmit} className="form">
          {/* Subject input group */}
          <div className="form-group">
            <label htmlFor="subject" className="label">
              Subject
            </label>
            <input
              id="subject"
              type="text"
              className="input"
              placeholder="Enter subject..."
              value={subject}
              onChange={handleSubjectChange}
            />
          </div>

          {/* Content input group */}
          <div className="form-group">
            <label htmlFor="content" className="label">
              Content
            </label>
            <textarea
              id="content"
              className="textarea"
              placeholder="Enter content..."
              value={content}
              onChange={handleContentChange}
              rows="8"
            />
          </div>

          {/* Submit button */}
          <button type="submit" className="button">
            Save Content
          </button>
        </form>

        {/* Feedback message displayed after submission */}
        {feedback && (
          <div className="feedback">
            {feedback}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;

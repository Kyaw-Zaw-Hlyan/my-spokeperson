import React, { useState } from 'react';
import './App.css';

/**
 * Main App Component
 * Premium content submission form with FastAPI backend integration
 * Features:
 * - Save content with word count validation (max 150 words)
 * - Real-time word count display
 * - Clean, sophisticated UI with dark gradient background
 * - API integration with FastAPI backend
 */
function App() {
  // State for subject input
  const [subject, setSubject] = useState('');

  // State for content input
  const [content, setContent] = useState('');

  // State to show feedback message after submission
  const [feedback, setFeedback] = useState('');

  // State for loading during API call
  const [loading, setLoading] = useState(false);

  // Maximum allowed word count
  const MAX_WORDS = 150;

  /**
   * Count words in content
   * Splits by whitespace and counts non-empty words
   */
  const countWords = (text) => {
    return text.trim().split(/\s+/).filter(word => word.length > 0).length;
  };

  // Get current word count
  const wordCount = countWords(content);

  // Check if content exceeds word limit
  const isWordLimitExceeded = wordCount > MAX_WORDS;

  /**
   * Handle form submission
   * Validates inputs and sends data to FastAPI backend
   */
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validate subject is not empty
    if (!subject.trim()) {
      setFeedback('Please enter a subject');
      return;
    }

    // Validate content is not empty
    if (!content.trim()) {
      setFeedback('Please enter content');
      return;
    }

    // Validate word count on frontend
    if (isWordLimitExceeded) {
      setFeedback(`Content exceeds 150 words. Current: ${wordCount} words`);
      return;
    }

    // Set loading state
    setLoading(true);
    setFeedback('');

    try {
      // Send POST request to FastAPI backend
      const response = await fetch('http://127.0.0.1:8000/api/save', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          subject: subject.trim(),
          content: content.trim(),
        }),
      });

      const data = await response.json();

      if (response.ok) {
        // Success - show confirmation message
        setFeedback(`✓ Saved! (${data.word_count} words)`);

        // Reset form fields
        setSubject('');
        setContent('');

        // Clear feedback after 4 seconds
        setTimeout(() => setFeedback(''), 4000);
      } else {
        // Error response from backend
        setFeedback(data.detail || 'Failed to save content');
      }
    } catch (error) {
      // Network or connection error
      setFeedback('Error connecting to server. Make sure FastAPI is running on http://localhost:8000');
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  /**
   * Handle subject input change
   */
  const handleSubjectChange = (e) => {
    setSubject(e.target.value);
  };

  /**
   * Handle content input change
   */
  const handleContentChange = (e) => {
    setContent(e.target.value);
  };

  return (
    // Main container with animated background
    <div className="container">
      {/* Premium card wrapper */}
      <div className="card">
        {/* Header section */}
        <div className="header">
          <h1 className="title">Spokeperson</h1>
          <p className="subtitle">Save Your Knowledge</p>
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
              disabled={loading}
              autoFocus
            />
          </div>

          {/* Content input group */}
          <div className="form-group">
            <div className="label-with-count">
              <label htmlFor="content" className="label">
                Content
              </label>
              {/* Word count display */}
              <span className={`word-count ${isWordLimitExceeded ? 'exceeded' : ''}`}>
                {wordCount} / {MAX_WORDS}
              </span>
            </div>
            <textarea
              id="content"
              className={`textarea ${isWordLimitExceeded ? 'error' : ''}`}
              placeholder="Enter your content here... (max 150 words)"
              value={content}
              onChange={handleContentChange}
              disabled={loading}
              rows="8"
            />
            {isWordLimitExceeded && (
              <span className="error-message">
                Content exceeds 150 words limit
              </span>
            )}
          </div>

          {/* Premium submit button */}
          <button 
            type="submit" 
            className="button" 
            disabled={loading || isWordLimitExceeded}
          >
            {loading ? 'Saving...' : 'Save Content'}
          </button>
        </form>

        {/* Premium feedback message */}
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

import React, { useState } from 'react';
import './LandingPage.css';

const LandingPage = ({ onSubmit }) => {
  const [repoUrl, setRepoUrl] = useState('');

  const handleSubmit = () => {
    if (repoUrl.trim() !== '') {
      onSubmit(repoUrl);
    }
  };

  return (
    <div className="landing-outer">
      <div className="landing-inner">
        <h1 className="landing-title">📘 DocuGen</h1>
        <p className="landing-subtitle">
          Auto-generate beautiful documentation from any GitHub codebase in seconds.
        </p>

        <div className="input-group">
          <input
            type="text"
            placeholder="Paste GitHub repo URL"
            className="repo-input"
            value={repoUrl}
            onChange={(e) => setRepoUrl(e.target.value)}
          />
          <button className="generate-btn" onClick={handleSubmit}>
            🚀 Generate Docs
          </button>
        </div>

        <p className="demo-note">Or try a sample repo to see how it works.</p>
      </div>
    </div>
  );
};

export default LandingPage;

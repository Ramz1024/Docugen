import React from 'react';
import Navbar from './components/Navbar';
import LandingPage from './components/LandingPage';
import Footer from './components/Footer';

function App() {
  const handleRepoSubmit = (repoUrl) => {
    console.log("Repo submitted:", repoUrl);
    // Connect to backend here
  };

  return (
    <>
      <Navbar />
      <LandingPage onSubmit={handleRepoSubmit} />
      <Footer />
    </>
  );
}

export default App;

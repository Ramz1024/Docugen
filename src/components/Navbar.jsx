import React from 'react';
import './Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-logo">📘 DocuGen</div>
      <ul className="navbar-links">
        <li><a href="#">Home</a></li>
        <li><a href="#">Docs</a></li>
        <li><a href="#">How it works</a></li>
        <li><a href="#">GitHub</a></li>
      </ul>
    </nav>
  );
};

export default Navbar;

// App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage'; // Adjust according to your actual page/component
import IncidentPage from './pages/IncidentPage'; // Adjust according to your actual page/component

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/incidents" element={<IncidentPage />} />
      </Routes>
    </Router>
  );
}

export default App;

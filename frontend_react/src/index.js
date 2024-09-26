// src/index.js
import React from 'react';
import ReactDOM from 'react-dom/client'; // Make sure this path is correct
import App from './App';
import './index.css'; // Adjust if your CSS file has a different name or path


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// src/index.js
import React from 'react';
import ReactDOM from 'react-dom/client'; // Ensure this line is using 'react-dom/client'
import App from './App';
import './styles.css';

const root = ReactDOM.createRoot(document.getElementById('root')); // This creates a root for your app
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// src/App.js
import React from 'react';
import Header from './components/Header';
import HomePage from './pages/HomePage';  // Updated import path
import IncidentPage from './pages/IncidentPage';  // Updated import path
import Footer from './components/Footer';
import './styles.css';

const App = () => {
    return (
        <div>
            <Header />
            <HomePage />
            <IncidentPage />
            <Footer />
        </div>
    );
};

export default App;

import React from 'react';
import './Footer.css'; // Add CSS if needed

const Footer = () => {
    return (
        <footer>
            <p>&copy; {new Date().getFullYear()} Cyber Incident Monitoring Tool</p>
        </footer>
    );
};

export default Footer;

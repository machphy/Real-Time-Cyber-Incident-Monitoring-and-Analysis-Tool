import axios from 'axios';

const API_URL = 'http://your-backend-url/api'; // Replace with your backend URL

export const getIncidents = async () => {
    const response = await axios.get(`${API_URL}/incidents`);
    return response.data;
};

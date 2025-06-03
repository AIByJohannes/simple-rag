import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Assuming the FastAPI backend is running on http://localhost:8000
        // Adjust the URL if your backend runs on a different port or host
        const response = await axios.get('http://localhost:8000/');
        setMessage(response.data.message);
      } catch (err) {
        setError('Failed to fetch message from backend. Ensure the backend is running and accessible.');
        console.error("Error fetching data:", err);
      }
    };

    fetchData();
  }, []); // Empty dependency array means this effect runs once on mount

  return (
    <>
      <h1>Vite + React Frontend</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {message && <p>Message from Backend: {message}</p>}
      {!message && !error && <p>Loading message...</p>}
    </>
  );
}

export default App;

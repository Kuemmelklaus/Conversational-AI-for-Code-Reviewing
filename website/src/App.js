import './App.css';
import React, { useState, useEffect } from 'react';

function App() {

  const [healthStatus, setHealthStatus] = useState(null);
  const [errorMessage, setErrorMessage] = useState(null);

  useEffect(() => {
    const getHealth = async () => {
      const response = await fetch("http://127.0.0.1:5000/health");
      const data = await response.json();
      setHealthStatus(data.status);
    }
    getHealth().catch(error => {
      setErrorMessage(error.toString());
      console.error("There was an error!", error);
    });
  }, []);

  return (
    <div className="App">
      <div className="App-header">
        <div>Health: {healthStatus}</div>
        {errorMessage != null &&
          <div>Error: {errorMessage}</div>
        }
      </div>
      <div className = "App-body">
        <input type = "text" name = "code" size = "40"/>
      </div>
    </div>
  );
}


export default App;

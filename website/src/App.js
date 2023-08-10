import './App.css';
import React, {useState, useEffect} from 'react';

function App() {

  const [status, setStatus] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/health")
    .then(response => response.json())
    .then(data => setStatus(data.status));
  }, []);

    return (
      <div className="App">
        <header className="App-header">
          <div>Health: {status}</div>
        </header>
      </div>
    );
  }


export default App;

import "./App.css";
import React, { useState, useEffect, onChange } from "react";
import Editor from "@monaco-editor/react";

function App() {
  const [healthStatus, setHealthStatus] = useState(null);
  const [errorMessage, setErrorMessage] = useState(null);
  const [code, setCode] = useState(null);
  const [theme, setTheme] = useState("cobalt");

  const CodeEditorWindow = ({ onChange, language, code, theme }) => {
    const [value, setValue] = useState(code || "");

    const handleEditorChange = (value) => {
      setValue(value);
      onChange("code", value);
    };

    return (
      <div className="input-window">
        <Editor
          height="70vh"
          width={`100%`}
          language={language || "python"}
          value={value}
          theme={theme}
          defaultValue="// some comment"
          onChange={handleEditorChange}
        />
      </div>
    );
  };

  const onChange = (action, data) => {
    switch (action) {
      case "code": {
        setCode(data);
        break;
      }
      default: {
        console.warn("case not handled!", action, data);
      }
    }
  };

  useEffect(() => {
    const getHealth = async () => {
      const response = await fetch("http://127.0.0.1:5000/health");
      const data = await response.json();
      setHealthStatus(data.status);
    };

    getHealth().catch((error) => {
      setErrorMessage(error.toString());
      console.error("There was an error!", error);
    });
  }, []);

  return (
    <div className="App">
      <div className="App-header">
        <div>Health: {healthStatus}</div>
        {errorMessage != null && <div>Error: {errorMessage}</div>}
      </div>
      <div className="App-body">
        <div>
          <CodeEditorWindow 
            code={code}
            onChange={onChange}
            theme={theme.value}
          />
          <p>
            <br />
          </p>
          <ReviewButton />
        </div>
      </div>
    </div>
  );
}

function ReviewButton() {
  return <button>Send review request</button>;
}

export default App;

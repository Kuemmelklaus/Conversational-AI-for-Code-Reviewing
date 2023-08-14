import "./App.css";
import React, { useState, useEffect } from "react";
import Editor from "@monaco-editor/react";

const CodeEditor = ({ lang }) => {
  const [code, setCode] = useState(null);
  const [language, setLanguage] = useState(null);
  const [theme, setTheme] = useState("vs-dark");

  useEffect(() => {
    setLanguage(lang);
  }, []);

  const handleEditorChange = (data) => {
    setCode(data);
    console.log(data, code);
  };

  function ReviewButton() {
    function sendPostRequest(code, language) {
      console.log(code, language);
      var jsonData = {
        programmingLanguage: language,
        code: code,
      };
      console.log(jsonData);

      const fetchRequest = async () => {
        const response = await fetch("http://127.0.0.1:5000/linter", {
          method: "POST",
          headers: new Headers({ "content-type": "application/json" }),
          body: JSON.stringify(jsonData),
        });
        const data = await response.json();
        console.log(data);
      };

      return fetchRequest();
    }
    return (
      <button onClick={() => sendPostRequest(code, language)}>
        Send review request
      </button>
    );
  }

  return (
    <div>
      <Editor
        height={"70vh"}
        width={`100%`}
        value={code}
        language={language}
        theme={theme}
        onChange={handleEditorChange}
      />
      <p>
        <br />
      </p>
      <ReviewButton />
    </div>
  );
};

function App() {
  const [healthStatus, setHealthStatus] = useState(null);
  const [errorMessage, setErrorMessage] = useState(null);
  const [language, setLanguage] = useState("python");

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
        <div className="code-editor">
          <CodeEditor lang={language} />
        </div>
      </div>
    </div>
  );
}

export default App;

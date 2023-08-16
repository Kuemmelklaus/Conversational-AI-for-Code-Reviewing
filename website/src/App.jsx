import "./App.css";
import React, { useState, useEffect, useCallback } from "react";
import Editor from "@monaco-editor/react";
import Select from "react-select";

const CodeEditor = ({ lang, onLangChange }) => {
  const [code, setCode] = useState(null);
  const [language, setLanguage] = useState(null);
  const [theme, setTheme] = useState("vs-dark");
  const [lint, setLint] = useState(null);
  const [working, setWorking] =useState(false);
  const langOptions = [
    { value: "python", label: "Python" },
    { value: "abap", label: "ABAP" },
  ];

  //initialize programming language
  useEffect(() => {
    setLanguage(lang);
  }, []);

  useEffect(() => {
    console.log("response:", lint);
  }, [lint]);

  //save code in react state
  const handleEditorChange = (data) => {
    setCode(data);
  };

  //change programming language
  const handleLangChange = useCallback(
    (event) => {
      setLanguage(event.value);
    },
    [onLangChange]
  );

  function ReviewButton() {
    function sendPostRequest(code, language) {
      var jsonData = {
        programmingLanguage: language,
        code: JSON.stringify(code),
      };

      //send http request
      const fetchRequest = async () => {
        const response = await fetch(
          "http://127.0.0.1:5000/linter?dummy=true",
          {
            method: "POST",
            headers: new Headers({ "content-type": "application/json" }),
            body: JSON.stringify(jsonData),
          }
        );
        const data = await response.json();
        setLint(data);
      };

      fetchRequest().catch((error) => {
        console.error("There was an error:", error);
      });
    }
    return (
      <button onClick={() => sendPostRequest(code, language)}>
        Send review request
      </button>
    );
  }

  return (
    <div>
      <div className="lang-select">
      <Select
        onChange={(event) => {
          onLangChange(event);
          handleLangChange(event);
        }}
        options={langOptions}
        defaultValue={langOptions[0]}
      />
      </div>
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

  //periodically check health status
  useEffect(() => {
    const catchError = () => {
      getHealth().catch((error) => {
        setHealthStatus("fail");
        setErrorMessage(error.toString());
        console.error("There was an error!", error);
      });
    };

    const getHealth = async () => {
      const response = await fetch("http://127.0.0.1:5000/health");
      const data = await response.json();
      setHealthStatus(data.status);
      setErrorMessage(null);
    };

    const interval = setInterval(() => {
      catchError();
    }, 30000);

    catchError();
    return () => clearInterval(interval);
  }, []);

  const langChange = (event) => {
    setLanguage(event.value);
  };

  return (
    <div className="App">
      <div className="App-header">
        <div>Health: {healthStatus}</div>
        {errorMessage != null && <div>Error: {errorMessage}</div>}
      </div>
      <div className="App-body">
        <div className="code-editor">
          <CodeEditor lang={language} onLangChange={langChange} />
        </div>
      </div>
    </div>
  );
}

export default App;

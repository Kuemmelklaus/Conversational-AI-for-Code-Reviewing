import "./App.css";
import { useEffect, useState } from "react";
import LangSelect from "./LangSelect";
import InputEditor from "./InputEditor";
import SubmitButton from "./SubmitButton";

function App() {
  const [healthStatus, setHealthStatus] = useState(null);
  const [errorMessage, setErrorMessage] = useState(null);
  const [language, setLanguage] = useState("python");
  const [code, setCode] = useState(() => {
    const localValue = localStorage.getItem("CODE");
    if (localValue === null) return null;
    return JSON.parse(localValue);
  });
  const [lint, setLint] = useState(null);

  useEffect(() => {
    if (lint != null) {
      console.log(lint);
      console.log(
        lint.lint.map((item) => {
          return item.message;
        })
      );
    }
  }, [lint]);

  //store code locally
  useEffect(() => {
    localStorage.setItem("CODE", JSON.stringify(code));
  }, [code]);

  //periodically check health status
  useEffect(() => {
    const getHealth = async () => {
      const response = await fetch("http://127.0.0.1:5000/health");
      const data = await response.json();
      setHealthStatus(data.status);
      setErrorMessage(null);
    };

    const catchError = () => {
      getHealth().catch((error) => {
        setHealthStatus("fail");
        setErrorMessage(error.toString());
        console.error("There was an error!", error);
      });
    };

    const interval = setInterval(() => {
      catchError();
    }, 30000);

    catchError();
    return () => clearInterval(interval);
  }, []);

  function changeLanguage(data) {
    setLanguage(data.value);
  }

  function handleEditorChange(data) {
    setCode(data);
  }

  function handleResponse(data) {
    setLint(data);
  }

  return (
    <div className="App">
      Health: {healthStatus}
      <br />
      {errorMessage != null && <>Error: {errorMessage}</>}
      <br />
      <br />
      <LangSelect onChange={changeLanguage} />
      <InputEditor
        language={language}
        code={code}
        onChange={handleEditorChange}
      />
      {lint != null && (
        <>
          Test{" "}
          {lint.lint.map((item) => {
            return item.message;
          })}
        </>
      )}
      <br />
      <SubmitButton language={language} code={code} onClick={handleResponse} />
      <br />
    </div>
  );
}

export default App;

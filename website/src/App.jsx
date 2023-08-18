import "./App.css";
import { useEffect, useState } from "react";
import LangSelect from "./LangSelect";
import InputEditor from "./InputEditor";
import SubmitButton from "./SubmitButton";
import Result from "./Result";

function App() {
  const [healthStatus, setHealthStatus] = useState(null);
  const [errorMessage, setErrorMessage] = useState(null);
  const [language, setLanguage] = useState("python");
  const [code, setCode] = useState(() => {
    const localValue = localStorage.getItem("CODE");
    if (localValue === null) return null;
    return JSON.parse(localValue);
  });
  const [reviewedCode, setReviewedCode] = useState(null);
  const [lint, setLint] = useState(null);
  const [reviewState, setReviewState] = useState("init");

  //   useEffect(() => {
  //     if (lint != null) {
  //       console.log(lint);
  //     }
  //   }, [lint]);

  //   useEffect(() => {
  //     console.log(reviewState);
  //   }, [reviewState]);

  //store code locally
  useEffect(() => {
    localStorage.setItem("CODE", JSON.stringify(code));
    if (reviewState !== "init") setReviewState("modified");
    // eslint-disable-next-line react-hooks/exhaustive-deps
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

  function handleReviewState(state) {
    setReviewState(state);
  }

  function handleResponse(data) {
    setLint(data);
    setReviewedCode(code);
  }

  return (
    <div className="App">
      Health: {healthStatus}
      {errorMessage != null && (
        <>
          <br />
          Error: {errorMessage}
        </>
      )}
      <br />
      <br />
      <span>
        Programming Language:
        <LangSelect onChange={changeLanguage} />
      </span>
      <InputEditor
        language={language}
        code={code}
        onChange={handleEditorChange}
      />
      <br />
      {(reviewState === "init" || reviewState === "modified") && (
        <SubmitButton
          language={language}
          code={code}
          onClick={handleResponse}
          handleReviewState={handleReviewState}
        />
      )}
      <br />
      <div className="result">
        {lint != null &&
          (reviewState === "success" || reviewState === "modified") && (
            <Result language={language} response={lint} code={reviewedCode} />
          )}
      </div>
    </div>
  );
}

export default App;

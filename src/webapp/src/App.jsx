import "./App.css";
import { useEffect, useState } from "react";
import LangSelect from "./LangSelect";
import InputEditor from "./InputEditor";
import SubmitButton from "./SubmitButton";
import Result from "./Result";
import ModelSelect from "./ModelSelect";

function App() {
  //declaring react states
  const [healthStatus, setHealthStatus] = useState(null);
  const [errorMessage, setErrorMessage] = useState(null);
  const [language, setLanguage] = useState("python");
  const [model, setModel] = useState("gpt-3.5-turbo-16k");
  const [code, setCode] = useState(() => {
    const localValue = localStorage.getItem("CODE");
    if (localValue === null) return null;
    return JSON.parse(localValue);
  });
  const [reviewedCode, setReviewedCode] = useState(null);
  const [caial, setCaial] = useState(null);
  const [reviewState, setReviewState] = useState("init");

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

    function catchError() {
      getHealth().catch((error) => {
        setHealthStatus("fail");
        setErrorMessage(error.toString());
        console.error("There was an error!", error);
      });
    }

    const interval = setInterval(() => {
      catchError();
    }, 5000);

    catchError();
    return () => clearInterval(interval);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  function changeLanguage(data) {
    if (reviewState !== "generating") {
      setLanguage(data.value);
      setReviewState("modified");
    } else {
      console.warn(
        "Do not change language while a request is still processing!"
      );
    }
  }

  function changeModel(data) {
    if (reviewState !== "generating") {
      setModel(data.value);
      setReviewState("modified");
    } else {
      console.warn(
        "Do not change model while a request is still processing!"
      );
    }
  }

  function handleEditorChange(data) {
    setCode(data);
  }

  function handleReviewState(state) {
    setReviewState(state);
  }

  function handleResponse(data) {
    setCaial(data);
    setReviewedCode(code);
  }

  //returning DOM
  return (
    <div className="App">
      <div className="request">
        Health: {healthStatus}
        {errorMessage != null && (
          <>
            <br />
            Error: {errorMessage}
          </>
        )}
        <br />
        <br />
        <div className="Select">
          Language:&emsp;
          <LangSelect onChange={changeLanguage} reviewState={reviewState} />
          &emsp;&emsp; Model:&emsp;
          <ModelSelect onChange={changeModel} reviewState={reviewState} />
        </div>
        <InputEditor
          language={language}
          code={code}
          onChange={handleEditorChange}
        />
        <br />
        {reviewState !== "generating" && (
          <SubmitButton
            language={language}
            code={code}
            model={model}
            handleResponse={handleResponse}
            handleReviewState={handleReviewState}
          />
        )}
        {reviewState === "generating" && <div className="loader" />}
        {reviewState === "fail" && <>Failed generating!</>}
      </div>
      <br />
      <div className="result">
        {caial != null &&
          (reviewState === "success" || reviewState === "modified") && (
            <Result language={language} response={caial} code={reviewedCode} />
          )}
      </div>
    </div>
  );
}

export default App;

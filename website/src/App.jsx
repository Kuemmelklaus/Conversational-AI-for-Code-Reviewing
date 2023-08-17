import "./App.css";
import { useEffect, useState } from "react";
import LangSelect from "./LangSelect";
import InputEditor from "./InputEditor";
import SubmitButton from "./SubmitButton";

function App() {
  const [healthStatus, setHealthStatus] = useState(null);
  const [errorMessage, setErrorMessage] = useState(null);
  const [language, setLanguage] = useState("python");
  const [code, setCode] = useState(null);
  const [lint, setLint] = useState(null);

  useEffect(() => {
    console.log(lint);
  }, [lint]);

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
      <br />
      <SubmitButton language={language} code={code} onClick={handleResponse}/>
      <br />
    </div>
  );
}

export default App;

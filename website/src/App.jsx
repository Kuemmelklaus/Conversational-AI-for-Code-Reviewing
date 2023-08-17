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

  useEffect(() => {
    console.log(language);
  }, [language]);

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

  return (
    <div className="App">
      Health: {healthStatus}
      {errorMessage != null && <>Error: {errorMessage}</>}
      <br />
      <LangSelect onChange={changeLanguage} />
      <InputEditor
        language={language}
        code={code}
        onChange={handleEditorChange}
      />
      <br />
      <SubmitButton />
    </div>
  );
}

export default App;

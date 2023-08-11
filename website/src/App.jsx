import "./App.css";
import React, { useState, useEffect } from "react";
import Editor from "@monaco-editor/react";

const CodeEditor = () => {
  const [code, setCode] = useState(null);
  const [language, setLanguage] = useState("python");
  const [theme, setTheme] = useState("vs-dark");

  const handleEditorChange = () => {

  };

  return(

    <Editor
      height={"70vh"}
      width={`100%`}
      value={code}
      language={language}
      theme={theme}
      onChange={handleEditorChange}
    />
  );
};

function App() {
  const [healthStatus, setHealthStatus] = useState(null);
  const [errorMessage, setErrorMessage] = useState(null);
  const [code, setCode] = useState(null);
  const [theme, setTheme] = useState("cobalt");
  const [language, setLanguage] = useState("python");

  /*
  const onChange = (action, data) => {
    switch (action) {
      case "code": {
        setCode(data);
        console.log(code);
        break;
      }
      default: {
        console.warn("case not handled!", action, data);
      }
    }
  };

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
          defaultValue={"" || "# some comment"}
          onChange={handleEditorChange}
        />
      </div>
    );
  };
  */

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
          <CodeEditor
            code={code}
            onChange={""}
            theme={theme.value}
            language={language}
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
  return <button onClick={() => sendPostRequest()}>Send review request</button>;
}

function sendPostRequest() {
  const fetchRequest = async () => {
    const response = await fetch("http://127.0.0.1:5000/linter", {
      method: "POST",
    });
  };
  console.log("AAA");
}




export default App;

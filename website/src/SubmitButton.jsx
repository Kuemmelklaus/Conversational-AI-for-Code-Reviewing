import { useState } from "react";

function SubmitButton({ language, code, handleResponse, handleReviewState }) {
  const [dummy, setDummy] = useState(false);

  function handleDummyChange(event) {
    setDummy(event.target.checked);
  }

  function sendPostRequest(language, code) {
    handleReviewState("generating");

    //creating request body
    var jsonData = {
      programmingLanguage: language,
      code: JSON.stringify(code),
    };

    //send http request
    const fetchRequest = async () => {
      if (dummy) {
        var url = "http://127.0.0.1:5000/linter?dummy=true";
      } else {
        url = "http://127.0.0.1:5000/linter";
      }
      
      const response = await fetch(url, {
        method: "POST",
        headers: new Headers({ "content-type": "application/json" }),
        body: JSON.stringify(jsonData),
      });
      const data = await response.json();
      if (data.success === true) {
        handleResponse(data);
        handleReviewState("success");
      } else {
        console.warn("No valid response!");
        handleReviewState("fail");
      }
    };

    fetchRequest().catch((error) => {
      console.error("There was an error:", error);
      handleReviewState("fail");
    });
  }

  return (
    <>
      <label>
        Dummy:{" "}
        <input
          type="checkbox"
          checked={dummy}
          onChange={(event) => handleDummyChange(event)}
        />
      </label>
      <button
        className="button"
        onClick={() => sendPostRequest(language, code)}
      >
        Send review request
      </button>
    </>
  );
}

export default SubmitButton;

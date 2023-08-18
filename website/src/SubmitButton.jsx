function SubmitButton({ language, code, onClick, handleReviewState }) {
  function sendPostRequest(language, code) {
    handleReviewState("generating");
    var jsonData = {
      programmingLanguage: language,
      code: JSON.stringify(code),
    };

    //send http request
    const fetchRequest = async () => {
      const response = await fetch("http://127.0.0.1:5000/linter?dummy=true", {
        method: "POST",
        headers: new Headers({ "content-type": "application/json" }),
        body: JSON.stringify(jsonData),
      });
      const data = await response.json();
      onClick(data);
      handleReviewState("success");
    };

    fetchRequest().catch((error) => {
      console.error("There was an error:", error);
      handleReviewState("fail");
    });
  }

  return (
    <button className="button" onClick={() => sendPostRequest(language, code)}>
      Send review request
    </button>
  );
}

export default SubmitButton;

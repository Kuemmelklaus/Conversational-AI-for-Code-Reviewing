function SubmitButton({ language, code, onClick }) {
  function sendPostRequest(language, code) {
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
    };

    fetchRequest().catch((error) => {
      console.error("There was an error:", error);
    });
  }

  return (
    <button
      className="button"
      onClick={() => sendPostRequest(language, code)}
    >
      Send review request
    </button>
  );
}

export default SubmitButton;

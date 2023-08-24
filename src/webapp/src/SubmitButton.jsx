function SubmitButton({
  language,
  code,
  model,
  handleResponse,
  handleReviewState,
}) {
  function sendPostRequest(language, code) {
    handleReviewState("generating");

    //creating request body
    const jsonData = {
      programmingLanguage: language,
      code: JSON.stringify(code),
    };

    //send http request
    const fetchRequest = async () => {
      switch (model) {
        case "gpt-3.5-turbo-16k":
          var url = `http://127.0.0.1:5000/caial?model=${model}`;
          break;
        case "gpt-4":
          url = `http://127.0.0.1:5000/caial?model=${model}`;
          break;
        case "dummy":
          url = `http://127.0.0.1:5000/caial?model=${model}`;
          break;
        default:
          throw Error("wrong query");
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
        console.warn("No valid response!", data);
        handleReviewState("fail");
      }
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

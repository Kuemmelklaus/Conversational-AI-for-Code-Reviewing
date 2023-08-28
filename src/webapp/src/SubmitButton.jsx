function SubmitButton({
  language,
  code,
  model,
  modelOptions,
  handleResponse,
  handleReviewState,
}) {
  function sendPostRequest(language, code) {
    //creating request body
    const jsonData = {
      programmingLanguage: language,
      code: JSON.stringify(code),
    };

    //send http request to flask server
    const fetchRequest = async () => {
      handleReviewState("generating");

      if(modelOptions.some((dict) => dict.value === model)) {
        var url = `http://127.0.0.1:5000/caial?model=${model}`;
      } else {
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

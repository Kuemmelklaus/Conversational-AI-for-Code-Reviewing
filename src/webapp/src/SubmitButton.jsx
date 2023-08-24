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

    // const options = [
    //   { value: "gpt-3.5-turbo-16k", label: "gpt-3.5-turbo-16k" },
    //   { value: "gpt-4", label: "gpt-4" },
    //   { value: "dummy", label: "Dummy" },
    // ];

    //send http request
    const fetchRequest = async () => {
      // if (options.includes({ value: "dummy", label: "Dummy" })) {
      //   console.log("a");
      // }

      switch (model) {
        case "gpt-3.5-turbo-16k":
          var url = `http://127.0.0.1:5000/linter?model=${model}`;
          break;
        case "gpt-4":
          url = `http://127.0.0.1:5000/linter?model=${model}`;
          break;
        case "dummy":
          url = `http://127.0.0.1:5000/linter?model=${model}`;
          break;
        default:
          throw Error("wrong query");
      }

      // if (dummy) {
      //   var url = "http://127.0.0.1:5000/linter?dummy";
      // } else {
      //   url = "http://127.0.0.1:5000/linter";
      // }

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

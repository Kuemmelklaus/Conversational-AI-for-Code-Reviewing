import { CodeBlock, dracula } from "react-code-blocks";

function Result({ language, response, code }) {
  //get code between lineFrom and lineTo
  function getCode(lineFrom, lineTo) {
    var split = code.split("\r\n");
    var snippet = split.slice(lineFrom - 1, lineTo).join("\r\n");
    return snippet;
  }

  return (
    <>
      <h1>Review Result</h1>
      <h3>Metadata:</h3>
      <span>
        Model: {response.model}
        <br />
        Total Tokens: {response.total_tokens}
        <br />
        Request Tokens: {response.total_tokens - response.completion_tokens}
        <br />
        Completion Tokens: {response.completion_tokens}
        <br />
        <br />
      </span>
      <h3>Critique:</h3>
      {response.caial.map((item) => {
        return (
          <span key={response.caial.indexOf(item)}>
            <CodeBlock
              text={getCode(item.lineFrom, item.lineTo)}
              showLineNumbers={true}
              startingLineNumber={item.lineFrom}
              theme={dracula}
              language={language}
            />
            Message: {item.message}
            <br />
            <br />
          </span>
        );
      })}
    </>
  );
}

export default Result;

import { CodeBlock, dracula } from "react-code-blocks";

function Result({ language, response, code }) {
  const lint = response.lint;

  function getCode(lineFrom, lineTo) {
    var split = code.split("\r\n");
    var snippet = split.slice(lineFrom - 1, lineTo).join("\r\n");
    return snippet;
  }

  return (
    <>
    <h1>Result</h1>
      {lint.map((item) => {
        return (
          <span key={lint.indexOf(item)}>
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

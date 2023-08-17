import { CodeBlock, dracula } from "react-code-blocks";

function Result({ language, lint, code }) {
  function getCode(lineFrom, lineTo) {
    var split = code.split("\r\n");
    var snippet = split
      .slice(lineFrom - 1, lineTo)
      .toString()
      .replaceAll(",", "\r\n");
    return snippet;
  }

  return (
    <>
      <CodeBlock
        text={getCode(lint.lineFrom, lint.lineTo)}
        showLineNumbers={true}
        startingLineNumber={lint.lineFrom}
        theme={dracula}
        language={language}
      />
      Message: {lint.message}
    </>
  );
}

export default Result;

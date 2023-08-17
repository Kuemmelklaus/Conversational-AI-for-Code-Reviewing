import { Editor } from "@monaco-editor/react";

function InputEditor({ language, code, onChange }) {

  return (
    <Editor
      height={"60vh"}
      width={`100%`}
      value={code}
      language={language}
      theme={"vs-dark"}
      onChange={onChange}
    />
  );
}

export default InputEditor;

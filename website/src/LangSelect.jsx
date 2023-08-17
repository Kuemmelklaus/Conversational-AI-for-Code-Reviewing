import Select from "react-select";

function LangSelect({ onChange }) {
  const langOptions = [
    { value: "python", label: "Python" },
    { value: "abap", label: "ABAP" },
  ];

  return (
    <Select
      options={langOptions}
      defaultValue={langOptions[0]}
      onChange={onChange}
    />
  );
}

export default LangSelect;

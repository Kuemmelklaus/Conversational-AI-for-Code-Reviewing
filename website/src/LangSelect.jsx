import Select from "react-select";

function LangSelect({ onChange }) {
  const langOptions = [
    { value: "python", label: "Python" },
    { value: "abap", label: "ABAP" },
  ];

  const theme = (theme) => ({
    ...theme,
    borderRadius: 5,
    colors: {
      ...theme.colors,
      text: "white",
      primary25: "#555555",
      primary: "#7c7c7c",
      neutral0: "#202020",
      neutral80: "white",
      neutral20: "#858585",
      primary50: "#71a8cc",
    },
  });

  return (
    <Select
      options={langOptions}
      defaultValue={langOptions[0]}
      onChange={onChange}
      theme={theme}
    />
  );
}

export default LangSelect;

import Select from "react-select";

function LangSelect({ onChange, reviewState }) {

  //creating programming language options
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
      primary50: "#6088a3",
    },
  });

  return (
    <Select
      options={langOptions}
      defaultValue={langOptions[0]}
      onChange={onChange}
      theme={theme}
      isDisabled={reviewState === "generating" ? true : false}
    />
  );
}

export default LangSelect;

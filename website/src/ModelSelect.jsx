import Select from "react-select";

function ModelSelect({ onChange, reviewState }) {
  const options = [
    { value: "gpt-3.5-turbo-16k", label: "gpt-3.5-turbo-16k" },
    { value: "gpt-4", label: "gpt-4" },
    { value: "dummy", label: "Dummy" },
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
      options={options}
      defaultValue={options[0]}
      onChange={onChange}
      theme={theme}
      isDisabled={reviewState === "generating" ? true : false}
    />
  );
}

export default ModelSelect;

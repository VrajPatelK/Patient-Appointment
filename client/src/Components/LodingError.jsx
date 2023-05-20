import React from "react";

const LodingError = ({ code, displayComponent }) => {
  // console.log(code);
  return (
    <>
      {code === 0 ? (
        <>Loading...</>
      ) : code === -1 ? (
        <h1>Server Error</h1>
      ) : code === 2 ? (
        <h1>No Data</h1>
      ) : (
        <>{displayComponent}</>
      )}
    </>
  );
};

export default LodingError;

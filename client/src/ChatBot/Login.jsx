// import React from "react";
// import { useState } from "react";
// import { TextField } from "@mui/material";
// import FlexBetween from "../../Components/FlexBetween";
// import { MyBtn } from "../../Components/MyComponent";
// import { VerifyAndStartChat, sendOtpEmail } from "./chatApis";
// const initialValue = {
//   name: "",
//   email: "",
//   otp: "",
// };
// function Login({ setId }) {
//   const [values, setValues] = useState(initialValue);
//   const [otpSent, setOtpSent] = useState(false);
//   const onChangehandle = (val, name) => {
//     let tmp = { ...values };
//     tmp[name] = val;
//     setValues(tmp);
//   };
//   const [loading, setLoading] = useState(false);
//   const sendOtp = () => {
//     if (!values.name || !values.email) {
//       alert("Please enter nam and Email to continue");
//     } else {
//       setLoading(true);
//       sendOtpEmail({ email: values.email })
//         .then((x) => {
//           setOtpSent(x);
//           setLoading(false);
//         })
//         .catch(() => {
//           setLoading(false);
//         });
//     }
//   };
//   const startChat = () => {
//     setLoading(true);
//     VerifyAndStartChat(values)
//       .then((x) => {
//         setId(x);
//         setLoading(false);
//       })
//       .catch(() => {
//         setOtpSent(false);
//         setLoading(false);
//       });
//   };
//   return (
//     <FlexBetween gap={"0.2rem"} flexDirection={"column"}>
//       {loading ? (
//         <>Loading...</>
//       ) : (
//         <>
//           {otpSent ? (
//             <>
//               <TextField
//                 onChange={(e) => onChangehandle(e.target.value, "otp")}
//                 sx={{ width: "10rem" }}
//                 placeholder="Enter 6 digit OTP"
//               />
//               <MyBtn label="start chat" onclickHandle={startChat} />
//             </>
//           ) : (
//             <>
//               <TextField
//                 onChange={(e) => onChangehandle(e.target.value, "name")}
//                 sx={{ width: "10rem" }}
//                 placeholder="Enter name..."
//               />
//               <TextField
//                 onChange={(e) => onChangehandle(e.target.value, "email")}
//                 sx={{ width: "10rem" }}
//                 type="email"
//                 placeholder="Enter Email..."
//               />
//               <MyBtn label="Send OTP" onclickHandle={sendOtp} />
//             </>
//           )}
//         </>
//       )}
//     </FlexBetween>
//   );
// }

// export default Login;

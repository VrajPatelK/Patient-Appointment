import * as React from "react";
import Box from "@mui/material/Box";
import Collapse from "@mui/material/Collapse";
import IconButton from "@mui/material/IconButton";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Typography from "@mui/material/Typography";
import Paper from "@mui/material/Paper";
import KeyboardArrowDownIcon from "@mui/icons-material/KeyboardArrowDown";
import KeyboardArrowUpIcon from "@mui/icons-material/KeyboardArrowUp";
import { Close, Done } from "@mui/icons-material";
import { Button } from "@mui/material";
import FlexBetween from "./FlexBetween";
import FlexEvenly from "./FlexEvenly";
import { AddResult } from "./MyComponent";
// export function createDataRow(
//   AID,
//   time,
//   status,
//   date,
//   contactNumber,
//   email,
//   message,
//   name
// ) {
//   return {
//     AID,
//     time,
//     status,
//     AllData: {
//       Date: date,
//       "Contact Number": contactNumber,
//       Email: email,
//       Message: message,
//       Name: name,
//     },
//   };
// }
function Row({ row }) {
  const [open, setOpen] = React.useState(false);
  var total = row.dailydebit + row.dailyCredit;
  return (
    <React.Fragment>
      <TableRow sx={{ "& > *": { borderBottom: "unset" } }}>
        <TableCell>
          <IconButton
            aria-label="expand row"
            size="small"
            onClick={() => setOpen(!open)}
          >
            {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
          </IconButton>
        </TableCell>
        {Object.keys(row).map((key) => {
          return (
            <TableCell
              key={key}
              component="th"
              scope="row"
              sx={{
                fontWeight: open && "bold",
              }}
            >
              {key === "entries" ? total : row[key]}
            </TableCell>
          );
        })}
      </TableRow>
      <TableRow>
        <TableCell style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={6}>
          <Collapse in={open} timeout="auto" unmountOnExit>
            <Box sx={{ margin: 1 }}>
              <Typography variant="h6" gutterBottom component="div">
                All Expense of {row["month"]}
              </Typography>
              <Table size="small" aria-label="purchases">
                <TableHead>
                  <TableRow>
                    <TableCell sx={{ fontWeight: "700" }}>Comment</TableCell>
                    <TableCell sx={{ fontWeight: "700" }}>Expense</TableCell>
                  </TableRow>
                </TableHead>
                {row.entries.map((m) => {
                  return (
                    <TableRow key={m}>
                      {Object.keys(m).map((k) => {
                        return (
                          <TableCell key={k} color="Primary">
                            {m[k]}
                          </TableCell>
                        );
                      })}
                    </TableRow>
                  );
                })}
              </Table>
            </Box>
          </Collapse>
        </TableCell>
      </TableRow>
    </React.Fragment>
  );
}
export default function CollapsibleTable({ data }) {
  const [rows, setRows] = React.useState(data);
  const [refresh, setRefresh] = React.useState(false);
  React.useEffect(() => {
    setRows(data);
  }, [refresh, data]);

  var totalDebit = 0;
  var totalCredit = 0;
  return (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell />
            <TableCell sx={{ fontWeight: "700" }}>Month</TableCell>
            <TableCell sx={{ fontWeight: "700" }}>Debit</TableCell>
            <TableCell sx={{ fontWeight: "700" }}>Credit</TableCell>
            <TableCell sx={{ fontWeight: "700" }}>Total</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row, i) => {
            totalDebit = totalDebit + row.dailydebit;
            totalCredit = totalCredit + row.dailyCredit;
            return <Row key={i} row={row} />;
          })}
          <TableRow>
            <TableCell />
            <TableCell sx={{ fontWeight: "bold" }}>Total</TableCell>
            <TableCell sx={{ fontWeight: "bold" }}>{totalDebit}</TableCell>
            <TableCell sx={{ fontWeight: "bold" }}>{totalCredit}</TableCell>
            <TableCell sx={{ fontWeight: "bold" }}>
              {totalDebit + totalCredit}
            </TableCell>
          </TableRow>
        </TableBody>
        {/* <AllTotal totalDebit={totalDebit} totalCredit={totalCredit} /> */}
      </Table>
    </TableContainer>
  );
}

export const AllTotal = ({ totalDebit, totalCredit }) => {
  return (
    <TableHead>
      <TableRow>
        <TableCell sx={{ fontWeight: "700" }}>TOTAL</TableCell>
        <TableCell sx={{ fontWeight: "700" }}>TOTAL</TableCell>
        <TableCell sx={{ fontWeight: "700" }}>{totalDebit}</TableCell>
        <TableCell sx={{ fontWeight: "700" }}>{totalCredit}</TableCell>
        <TableCell sx={{ fontWeight: "700" }}>
          {totalCredit - totalDebit}
        </TableCell>
      </TableRow>
    </TableHead>
  );
};

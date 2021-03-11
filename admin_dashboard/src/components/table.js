// src/components/pagination.table.js
import React, { Component } from "react";

import {
  useTable,
  usePagination,
  useFilters,
  useGlobalFilter,
  useAsyncDebounce,
  useSortBy,
} from "react-table";
import "bootstrap/dist/css/bootstrap.min.css";

// Define a default UI for filtering
function GlobalFilter({
  preGlobalFilteredRows,
  globalFilter,
  setGlobalFilter,
}) {
  const count = preGlobalFilteredRows.length;
  const [value, setValue] = React.useState(globalFilter);
  const onChange = useAsyncDebounce((value) => {
    setGlobalFilter(value || undefined);
  }, 200);

  return (
    <span>
      Search:{" "}
      <input
        className="form-control"
        value={value || ""}
        onChange={(e) => {
          setValue(e.target.value);
          onChange(e.target.value);
        }}
        placeholder={`${count} records...`}
      />
    </span>
  );
}

function DefaultColumnFilter({
  column: { filterValue, preFilteredRows, setFilter },
}) {
  const count = preFilteredRows.length;

  return (
    <input
      className="form-control"
      value={filterValue || ""}
      onChange={(e) => {
        setFilter(e.target.value || undefined);
      }}
      placeholder={`Search ${count} records...`}
    />
  );
}

function Table({ columns, data, onColumnClick }) {
  const defaultColumn = React.useMemo(
    () => ({
      // Default Filter UI
      Filter: DefaultColumnFilter,
    }),
    []
  );
  // Use the state and functions returned from useTable to build your UI
  const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    rows,
    prepareRow,
    page,
    state,
    canPreviousPage,
    canNextPage,
    pageOptions,
    pageCount,
    gotoPage,
    nextPage,
    previousPage,
    setPageSize,
    preGlobalFilteredRows,
    setGlobalFilter,

    state: { pageIndex, pageSize },
  } = useTable(
    {
      columns,
      data,
      initialState: { pageIndex: 2, pageSize: 5 },
      defaultColumn,
    },
    useFilters,
    useGlobalFilter,
    useSortBy,
    usePagination
  );

  const handleColumnClick = (e) => {
    if (typeof onColumnClick === "function") {
      const value = e.target.getAttribute("data_id");
      onColumnClick(value);
    }
  };

  const handleNonColumnClick = (e) => {
    e.stopImmediatePropagation?.();
    e.stopPropagation();
    e.preventDefault();
    return;
  };

  // Render the UI for your table
  return (
    <div>
      {/* <GlobalFilter
                preGlobalFilteredRows={preGlobalFilteredRows}
                globalFilter={state.globalFilter}
                setGlobalFilter={setGlobalFilter}
            /> */}
      <table className="table" {...getTableProps()}>
        <thead>
          {headerGroups.map((headerGroup) => (
            <tr {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map((column) => {
                const { onClick, otherProps } = column.getHeaderProps(
                  column.getSortByToggleProps()
                );
                const handleClick = (e) => {
                  handleColumnClick(e);
                  onClick(e);
                };
                return (
                  <th
                    data_id={column.render("Header")}
                    {...column.getHeaderProps()}
                    {...otherProps}
                    onClick={handleClick}
                  >
                    {column.render("Header")}
                    {/* Render the columns filter UI */}
                    <div onClick={handleNonColumnClick}>
                      {column.canFilter ? column.render("Filter") : null}
                    </div>
                    {/* Add a sort direction indicator */}
                    <span onClick={handleNonColumnClick}>
                      {column.isSorted ? (column.isSortedDesc ? " " : " ") : ""}
                    </span>
                  </th>
                );
              })}
            </tr>
          ))}
        </thead>

        <tbody {...getTableBodyProps()}>
          {page.map((row, i) => {
            prepareRow(row);
            return (
              <tr {...row.getRowProps()}>
                {row.cells.map((cell) => {
                  return (
                    <td {...cell.getCellProps()}>{cell.render("Cell")}</td>
                  );
                })}
              </tr>
            );
          })}
        </tbody>
      </table>
      {/* 
        Pagination can be built however you'd like. 
        This is just a very basic UI implementation:
      */}

      <br></br>

      <nav aria-label="Page navigation example">
        <ul className="pagination justify-content-center">
          <li
            className="page-item"
            onClick={() => gotoPage(0)}
            disabled={!canPreviousPage}
          >
            <a className="page-link">First</a>
          </li>
          <li
            className="page-item"
            onClick={() => previousPage()}
            disabled={!canPreviousPage}
          >
            <a className="page-link">{"<"}</a>
          </li>
          <li
            className="page-item"
            onClick={() => nextPage()}
            disabled={!canNextPage}
          >
            <a className="page-link">{">"}</a>
          </li>
          <li
            className="page-item"
            onClick={() => gotoPage(pageCount - 1)}
            disabled={!canNextPage}
          >
            <a className="page-link">Last</a>
          </li>
          <li>
            <a className="page-link">
              Page{" "}
              <strong>
                {pageIndex + 1} of {pageOptions.length}
              </strong>{" "}
            </a>
          </li>
          <li>
            <a className="page-link">
              <input
                className="form-control"
                type="number"
                defaultValue={pageIndex + 1}
                onChange={(e) => {
                  const page = e.target.value ? Number(e.target.value) - 1 : 0;
                  gotoPage(page);
                }}
                style={{ width: "100px", height: "20px" }}
              />
            </a>
          </li>{" "}
          <select
            className="form-control"
            value={pageSize}
            onChange={(e) => {
              setPageSize(Number(e.target.value));
            }}
            style={{ width: "120px", height: "38px" }}
          >
            {[5, 10, 20, 30, 40, 50].map((pageSize) => (
              <option key={pageSize} value={pageSize}>
                Show {pageSize}
              </option>
            ))}
          </select>
        </ul>
      </nav>
    </div>
  );
}

function PaginationTableComponent(props) {
  const columns = React.useMemo(() => []);

  const sample = props.data;
  const headerdata = [];
  console.log('check', sample);
  
  Object.keys(sample[0]).slice(0, 74).map((val, k) => {
      headerdata.push({
        Header: "Specifications",
        columns: [
          {
            Header: val,
            accessor: val,
          },
        ],
      });
    });

  return (
    <Table
      columns={headerdata}
      data={sample}
      onColumnClick={props.onColumnClick}
    />
  );
}

export default PaginationTableComponent;

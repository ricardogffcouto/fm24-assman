import { createNewCell } from './cellCreator.js';

export function addNewColumn(playerTable, columnName, sourceColumns, calculationFunction) {
  // Add a new column header
  const headerRow = playerTable.querySelector("thead tr");
  const newHeader = document.createElement("th");
  newHeader.innerText = columnName;
  headerRow.appendChild(newHeader);

  // Find the indices of the source columns
  const headerCells = playerTable.querySelectorAll("thead th");
  const columnIndices = sourceColumns.map(colId => {
    return Array.from(headerCells).findIndex(cell => cell.id === colId);
  });

  // Iterate through each row in the table body
  const bodyRows = playerTable.querySelectorAll("tbody tr");
  bodyRows.forEach((row) => {
    try {
      const cells = row.querySelectorAll("td");
      const values = columnIndices.map(index => 
        parseInt(cells[index].querySelector(".rounded-full").innerText)
      );

      console.log("Source values:", values);

      // Calculate the new value
      const newValue = calculationFunction(values);

      // Create a new cell and insert the calculated value
      const newCell = createNewCell(newValue);
      row.appendChild(newCell);
    } catch (error) {
      console.error("Error processing row:", error);
    }
  });
}

// No export statement needed

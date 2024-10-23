// contentScript.js
console.log("Content script loaded");

// Create a MutationObserver to detect changes in the DOM
const observer = new MutationObserver((mutations, observer) => {
  // Try to find the table by its ID
  const playerTable = document.querySelector("#player-table");

  if (playerTable) {
    console.log("Player table found:", playerTable);

    // Add a new column header
    const headerRow = playerTable.querySelector("thead tr");
    const newHeader = document.createElement("th");
    newHeader.innerText = "Physical + Mental";
    headerRow.appendChild(newHeader);

    // Find the index of the "Physical" and "Mental" columns
    const headerCells = playerTable.querySelectorAll("thead th");
    let physicalIndex = -1;
    let mentalIndex = -1;
    headerCells.forEach((cell, index) => {
      if (cell.id === "col-Physical") physicalIndex = index;
      if (cell.id === "col-Mental") mentalIndex = index;
    });

    // Iterate through each row in the table body
    const bodyRows = playerTable.querySelectorAll("tbody tr");
    bodyRows.forEach((row) => {
      try {
        const cells = row.querySelectorAll("td");
        const physical = parseInt(cells[physicalIndex].querySelector(".rounded-full").innerText);
        const mental = parseInt(cells[mentalIndex].querySelector(".rounded-full").innerText);

        console.log("Physical value:", physical, "Mental value:", mental);

        // Calculate the average
        const average = (physical + mental) / 2;

        // Create a new cell and insert the average value
        const newCell = document.createElement("td");
        newCell.innerText = average.toFixed(2); // Format to 2 decimal places
        row.appendChild(newCell);
      } catch (error) {
        console.error("Error processing row:", error);
      }
    });

    // Once the table is found and processed, stop observing
    observer.disconnect();
  } else {
    console.log("Player table not found yet.");
  }
});

// Start observing the body of the document for any changes in child elements
observer.observe(document.body, { childList: true, subtree: true });

console.log("MutationObserver is set up and running...");

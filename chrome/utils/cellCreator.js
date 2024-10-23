import { calculateColor } from './colorCalculator.js';

function createNewCell(value) {
  const newCell = document.createElement("td");
  newCell.className = "table-cell px-4 py-2 align-middle [&:has([role=checkbox])]:pr-0 [&>[role=checkbox]]:translate-y-[2px] relative bg-background";
  
  const color = calculateColor(value);
  
  const cellContent = `
    <div class="flex gap-2 items-center font-normal justify-center" title="${value.toFixed(2)}">
      <div class="rounded-full border px-2.5 transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 font-bold text-sm flex text-center justify-center items-center py-[6px] min-w-[60px] !leading-4 text-[${color}] border-[${color}]">
        ${value.toFixed(2)}
      </div>
    </div>
  `;
  
  newCell.innerHTML = cellContent;
  return newCell;
}

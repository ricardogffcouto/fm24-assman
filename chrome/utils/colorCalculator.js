function calculateColor(value) {
  if (value > 13.5) {
    return '#1dff21'; // Green for values > 13.5
  }
  
  // Gradient calculation for values between 0 and 13.5
  const minValue = 0;
  const maxValue = 13.5;
  const minColor = [255, 28, 0];  // #ff1c00 (red)
  const maxColor = [227, 255, 0]; // #e3ff00 (yellow)
  
  const ratio = (value - minValue) / (maxValue - minValue);
  const r = Math.round(minColor[0] + ratio * (maxColor[0] - minColor[0]));
  const g = Math.round(minColor[1] + ratio * (maxColor[1] - minColor[1]));
  const b = Math.round(minColor[2] + ratio * (maxColor[2] - minColor[2]));
  
  return `#${r.toString(16).padStart(2, '0')}${g.toString(16).padStart(2, '0')}${b.toString(16).padStart(2, '0')}`;
}

// No export statement needed

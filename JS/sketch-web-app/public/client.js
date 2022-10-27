export function setUpCanvas(canvas) {
  const ctx = canvas.getContext('2d');
  canvas.width = 1500;
  canvas.height = 1000;
  canvas.style.width = '100vw';
  canvas.style.height = '100vh';
  canvas.style.backgroundColor = '#f8f9fa';
  return ctx;
}

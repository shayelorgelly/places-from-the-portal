process.stdout.write('\x1b[?1000h'); // does not work.
process.stdout.write('\x1b[?1002h'); // Enable mouse button press/release tracking

process.stdin.setRawMode(true);
process.stdin.setEncoding('utf8');

process.stdin.on('data', (data) => {
  const input = data.toString();

  if (input.startsWith('\x1b[')) {
    const event = parseMouseEvent(input);
    if (event) {
      console.log('Mouse event:', event);
    }
  } else if (input === '\u0003') {
    // Exit application when Ctrl+C is pressed
    process.exit();
  }
});

function parseMouseEvent(input) {
  const match = /^\x1b\[(\d+);(\d+);(\d+)M/.exec(input);
  if (match) {
    const [, buttonCode, col, row] = match;
    const button = parseInt(buttonCode, 10) - 32;
    return { button, col, row };
  }
  return null;
}

console.log('Listening for mouse events. Press Ctrl+C to exit.');

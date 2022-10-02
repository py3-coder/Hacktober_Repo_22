const argv = process.argv.slice(2);
const operation = argv[0];
const operators = [];

operators[0] = parseInt(argv[1]);
operators[1] = parseInt(argv[2]);

switch (operation) {
  case 'add':
    outputToConsole(operation, '+', operators);
    console.log('Result: ' + (operators[0] + operators[1]));
    break;
  case 'subtract':
    outputToConsole(operation, '-', operators);
    console.log('Result: ' + (operators[0] - operators[1]));
    break;
  case 'multiply':
    outputToConsole(operation, '*', operators);
    console.log('Result: ' + (operators[0] * operators[1]));
    break;
  case 'divide':
    outputToConsole(operation, '/', operators);
    console.log('Result: ' + (operators[0] / operators[1]));
    break;
}

function outputToConsole(operation, operationSymbol, operators) {
  console.log('Operation: ' + operation);
  console.log('Condition: ' + operators[0] + ' ' + operationSymbol + ' ' + operators[1]);
}
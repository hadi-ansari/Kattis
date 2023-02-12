const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function askForName() {
  rl.question('Enter the correct name: ', (answer) => {
    if (answer === 'Jack') {
      console.log('Good job!');
      rl.close();
    } else {
      askForName();
    }
  });
}

askForName();

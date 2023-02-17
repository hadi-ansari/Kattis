const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})
if (!process.stdin.isTTY) {
    // Input is coming from a file, so don't print the input
    rl._writeToOutput = () => {}
}


rl.on("line", (input) => {
    console.log(input/4)
})
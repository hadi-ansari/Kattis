const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
}) 

const readInput = async () => {
    await rl.question("", (i) => {
        console.log("hhshshsh", i)
        return i
    })  
}

const main = async () => {
    let first = await readInput()
    console.log("HHHH", await first)
}


main()
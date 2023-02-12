const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on("line", (input) => {
    let inputCharArray = []
    for(let i = 0; i < input.length; i++){
        inputCharArray.push(input.charAt(i))
    }

    let totalLenght = input.length
    let whiteSpaceCounter = 0
    let lowercaseCounter = 0
    let uppercaseCounter = 0
    let symboleCounter = 0

    inputCharArray.forEach(e  => {
        let asciiCode = e.charCodeAt(0)
        if(e === "_")
            whiteSpaceCounter ++
        else if(asciiCode >= 65 && asciiCode <= 90)
            uppercaseCounter ++
        else if(asciiCode >= 97 && asciiCode <= 122)
            lowercaseCounter ++
        else
            symboleCounter ++
    } )

    console.log(whiteSpaceCounter/totalLenght)
    console.log(lowercaseCounter/totalLenght)
    console.log(uppercaseCounter/totalLenght)
    console.log(symboleCounter/totalLenght)
    rl.close()
});
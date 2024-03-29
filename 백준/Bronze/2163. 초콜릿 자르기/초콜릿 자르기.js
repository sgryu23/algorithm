const fs = require('fs')
const [n, m] = fs.readFileSync('/dev/stdin').toString().trim().split(' ')

const solution = (a, b) => {
    return a * b - 1
}
console.log(solution(n, m))
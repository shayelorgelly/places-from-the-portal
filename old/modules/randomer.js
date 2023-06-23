module.exports.array = (table)=>{
    return table[Math.floor(Math.random() * table.length)]
}

module.exports.getRandomInt = (max)=>{
    return Math.floor(Math.random() * max)
}
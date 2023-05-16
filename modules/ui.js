module.exports = {
    getTerminalSize: ()=>{
        return [process.stdout.rows, process.stdout.columns]
    },
    checkTerminalSize: (rows, columns)=>{
        let currentSize = module.exports.getTerminalSize()
        let maxSize = [rows, columns]
        if(mixSize[0] < currentSize[0] || minSize[1] < currentSize){
            console.warn("no")
        }
    }
}
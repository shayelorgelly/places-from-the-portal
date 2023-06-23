module.exports.loopSync = (i, callback)=>{
    if (i <= 0){
        return true;
    }
    callback(i)
    setTimeout(()=>{
        module.exports.loopSync(i - 1, callback)
    }, 0)//make it wait
} 
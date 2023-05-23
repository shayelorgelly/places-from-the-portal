//
const path = require("node:path")
const { spawn, exec } = require("node:child_process")
//nodejs imports

//
const { playSound } = require("./modules/noise.js")
const { print, printColor } = require("./modules/console.js")
const { loopSync }= require("./modules/looper.js")
const { waitSync, loopPrintOnTimer, fakeTypingPrintTimerColor } = require("./modules/timer.js")
const random = require("./modules/randomer.js")
//my own modules made for this project


let items = []
let unlocks = []
let player = {
    "name": "Jim Johnson"
}
let npcA = []
let currentLocation = ""

class npc{
    forEachInRoom(room, cb){
        npcA.forEach((_npc)=>{
            if (_npc.location == room){
                cb()
            }
        })
    }
    constructor(name, location){
        this.name = name
        npcA.push(this)
        this.id = npcA.length - 1
        this.location = location
        this.say = (message)=>{
            print(`[${this.name}]: ${message}`)
        }
    }
    
}
//npcs
var john_Smith = new npc("John Smith", "portalRoom")
const enterRoom = (name)=>{
    printColor(`Now entering ${name} \n`, [255,255,0])
}


//portal room starting area
const portalRoom = ()=>{
    enterRoom("Portal Room")//print cool entering room text
    currentLocation = "portalRoom"//set currentlocation for npcs
    waitSync(2000)
    let greetings = ["Welcome back, ", "Hey there, ", "How is it going, ", "Whats up, ", "Howdy, ", ""]
    let randomGreeting = random.array(greetings)
    npcA.forEach(person => {
        if (person.location == currentLocation){
            person.say(`${randomGreeting}${player.name}\n`)
        }
    });


}




//tests
function testNPC(){
    console.log(npcA)
    var Thomas_Willson = new npc("Thomas Willson", "portalRoom");
    print(`\n${Thomas_Willson.location}, ${Thomas_Willson.id}, ${Thomas_Willson.name}`);
    Thomas_Willson.say("hello");
}

async function setupGame(){
    await playSound("./audio/untitled.wav")//sort of blocking function
    console.log("Places From The Portal");
    loopPrintOnTimer(".", 5, 1000);
    waitSync(3000);//no await needed as it blocks async and regular sync
    portalRoom(); // go to portal room
}
fakeTypingPrintTimerColor("Places From The Portal", 150, [255,255,0])
// try {//try catch incase skip setup isn't defined
//     if(skipSetup){
//         portalRoom();
//     } else {
//         setupGame();
//     }
// } catch (error) {
//     setupGame();
// }

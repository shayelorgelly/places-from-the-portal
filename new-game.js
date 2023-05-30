//
const path = require("node:path")
const { spawn, exec } = require("node:child_process")
//nodejs imports

//
const fs = require("fs")
const { playSound } = require("./modules/noise.js")
const { print, printColor, input } = require("./modules/console.js")
const { loopSync }= require("./modules/looper.js")
const { waitSync, loopPrintOnTimer, fakeTypingPrintTimerColor } = require("./modules/timer.js")
const random = require("./modules/randomer.js")
//my own modules made for this project


class inventory{
    inventories = []
    player = true
    constructor(owner, inventorySize){
        this.owner = owner;
        this.inventorySize = inventorySize;
        this.items = [];
        this.addItem = (itemName)=>{
            this.items.push(itemName);
        };
        this.removeItem = (itemName)=>{
            if (this.items[itemName]){
                this.items[itemName] = undefined;
            };
        };
        this.getItems = ()=>{
            return this.items.join(", ")
        }
        this.inventories.push(this)
    };
};
let unlocks = [];
let player = {
    "name": "Jim Johnson",
    "inventory": new inventory("player", 4)
};
let npcA = [];
let currentLocation = ""
class npc {
    static forEachInRoom = (room, callback)=>{
        npcA.forEach((_npc)=>{
            if (_npc.location == room){
                callback(_npc);
            }
        })
    }
    constructor(name, location){
        this.name = name;
        npcA.push(this);
        this.id = npcA.length - 1;
        this.location = location;
        this.say = (message)=>{
            print(`[${this.name}]: ${message}`);
        };
        this.dialog = []
    }
    
}
//npcs
var john_Smith = new npc("John Smith", "portalRoom")
const enterRoom = (name)=>{
    printColor(`Now entering ${name} \n`, [255,255,0]);
};


//portal room starting area
module.exports.portalRoom = ()=>{
    enterRoom("Portal Room");//print cool entering room text
    currentLocation = "portalRoom";//set currentlocation for npcs
    waitSync(2000);
    let greetings = ["Welcome back, ", "Hey there, ", "How is it going, ", "Whats up, ", "Howdy, ", ""];
    npc.forEachInRoom("portalRoom",(person)=>{
        let randomGreeting = random.array(greetings);//moved to here so i can get a different greeting from everyone
        person.say(`${randomGreeting}${player.name}\n`)
    });

    `Hey ${player.name}, do ya need me to make you anything?`
    `Here you go ${player.name}, here is your ${itemName}`
    `The portal is ready ${player.name}, should we test it out?`
    `[INVENTORY] [NPC] [TRAVEL] [idk]`


};





async function setupGame(){
    await playSound("./audio/untitled.wav")//sort of blocking function
    console.log("Places From The Portal");
    loopPrintOnTimer(".", 5, 1000);
    waitSync(3000);//no await needed as it blocks async and regular sync
    portalRoom(); // go to portal room
}
// try {//try catch incase skip setup isn't defined
//     if(skipSetup){
//         portalRoom(); 
//     } else {
//         setupGame();
//     }
// } catch (error) {
//     setupGame();
// }



// function testNPC(){
//     console.log(npcA)
//     var Thomas_Willson = new npc("Thomas Willson", "portalRoom");
//     print(`\n${Thomas_Willson.location}, ${Thomas_Willson.id}, ${Thomas_Willson.name}`);
//     Thomas_Willson.say("hello");
// }

// const g = input("hello\n")
// console.log("you said " + g)
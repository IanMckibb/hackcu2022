// Importing expresss
const express=require("express");
var queryString = require('querystring');
const app=express();

 
// Handling get request
app.get("/doIt",(req,res,next)=>{
    console.log("Getting...");
    var queryString = req.query.search;
    const spawn = require("child_process").spawn;
    const pythonProcess = spawn('python',["script.py", queryString]);
    pythonProcess.stdout.on('data', (data) => {
    console.log("Done!");
    res.send(String(data));
    });
})
app.get("/get/users",(req,res,next)=>{
    res.send("This is the get/users request")
})
app.listen(8000,()=>{
    console.log("Server is Running");
})
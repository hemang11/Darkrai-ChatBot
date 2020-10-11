const express = require('express');
const app = express();
const cp = require('child_process')

// Routes
app.get('/',(req,res)=>res.send('Routes Working Fine'));

app.get('/name',invoke);

function invoke(req,res){
   let spawn = cp.spawn;
   let process = spawn('python',['./b.py',req.query.text]);

   process.stdout.on('data', (data) => {
   console.log(data); 
   res.send(data.toString()); 
   });
}

app.listen(3100,()=>console.log('Server Started'));
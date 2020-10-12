const express=require('express'); 
const app=express(); 

//Import PythonShell module. 
const {PythonShell} =require('python-shell'); 
 
app.get("/", (req, res)=>{  // Request Made to /?name=".."
   const search = req.query.name;
	let options = { 
		mode: 'text', 
		pythonOptions: ['-u'], // get print results in real-time 
		//scriptPath: 'path/to/my/scripts' //If you are having python_test.py script in same folder, then it's optional. 
		args: [search] //An argument which can be accessed in the script using sys.argv[1] 
	}; 
	

PythonShell.run('chat.py', options, function (err, result){ 
		if (err) res.send(err.message); 
      const len = result.length;
      const response = result[len-1];
		console.log('result: ', response.toString()); 
		res.send(response.toString()) 
	}); 
}); 

const port=5500; 
app.listen(port, ()=>console.log(`Server connected to ${port}`));

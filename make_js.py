import os
import subprocess 
file = open("./data/vocab80000.from")
js = open("test.js",'a+')
lines = file.readlines()
count  =0
header_line = "const translate = require('google-translate-api');\nvar sleep = require('sleep');\n"
# os.system(": > test_5k.js")


file = open("populate_dic.js", 'a+')
file.write(header_line)
file.close()
# js.write(header_line)
# js.write(header_line)
arr = []
for line in lines:
	# file = open(filenames[count/5000],'a+')
	line = line.strip()
	arr.append(line)
	print(count)
	# command = "translate(\""+line+"\", {to: 'fr'}).then(res => { console.log(\""+line+"\",res.text); }).catch(err => { console.error(err); });\nsleep.msleep(5)\n"
	
	# file.write(command)
	count= count+1
	# file.close()
	# if count %5000 == 0:
	# # 	test = subprocess.Popen(['node','test.js'])
	# 	newFile= "test"+"_"+str(count/1000)+"k.js"
	# 	new_command = "touch "+newFile
	# 	os.system(new_command)
	# 	js = open(newFile,'a+')
	# 	js.write(header_line)

	# 	output = test.communicate()[0]
	# 	print (output)
		# break
		# os.system(": > test.js")
		# js.write(header_line)

file = open("populate_dic.js", 'a+');
file.write("var arr ="+str(arr) +";")
file.close()
# var processItems = function(x){
#    if( x < arr.length ) {
#    		var word = arr[x];
#        translate(word, {to: 'fr'}).then(res => { 
# 	    	console.log(word,res.text); 
# 	    	// sleep.msleep(5);
# 	    	processItems(x+1);
# 	    }).catch(err => { 
# 	    	console.error(err); 
# 	    });
	    
#    }
# };

# processItems(0);)


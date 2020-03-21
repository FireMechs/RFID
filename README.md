## Laptop Security RFID-based project

### Getting started

* 1. Make sure to have git installed in your windows or linux machine 
Follow the following link for instructions on installation of git in your system
[Git installation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

* 2. After joining FireMechs organization @[FireMechs](https://github.com/FireMechs) you will have read&write access to the repositories so you can update it as you see deem fit

* 3.  But first let us set up your repo. 

	* a. Open up you git bash: Windows (type 'git' in cortana search bar)

	* b. Navigate to your project directory using 
	```bash
		cd directory Name #changing to the directory
		cd .. # moving back to the previous directory(parent directory)
		```

	* c. Initialize git in that repo
	```bash
		git init
		```

	* d. Add the remote github repo so you can commit files to it.
	```bash 
		git remote add origin https://github.com/FireMechs/RFID.git
		``` 

	* e. Start your project, add read and write files in your project repository using your preferred IDE or Editor.
	
	* f. Ready to send your work to the online repo?

Yes  but then not everything inside my directory is to be send. Then, fire up git bash and ignore this files ...
	```bash
		touch .gitignore # do this in your project repository
		```
You will find this file '.gitignore' in your project repository. Edit it using any editor you like. If you don't want to send a certain directoty online the add the directory name to the  '.gitignore' file as follows
	```.gitignore
		sda_hymns/   
		```
if it is a file, then
	```bash
		filename
		```

	* g. What if some fellow has already uploaded his/her work before me. Oh, the rule is I need to have that update before I send my work.
	```bash
		git pull 
		```

	* h. Finally my files are ready and I am ready to upload
	```bash
		git add . # prepares the files for staging

		git commit -m "my commit message" # staging the files ready for upload

		git push -u origin master 
		```

Your will be asked for the username and password, and vuala! my work is online.

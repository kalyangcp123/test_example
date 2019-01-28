# test_example

To Run the file :
python name of the file .py (eg: python task.py)

Explantion:
1. First I have create the Project folder.

2. In that I have created the task folder:
	a. locators.py
	b. variables.json
	c. webelementactions.py
	d. Task.py(Main File)

3. In the task.py(Main File) first imported the locators and varibales and webelementactions files

4. In the task.py(Main File) 

	i. Created the class name as "task".
	ii. In the intialization part, I have used chromedriver to control the chrome browser.
	
		a. First i have open the chrome browser.
		b. I have get the google url and then I have opened the quickfuseapps page

	iii. Created the create_app(Defination) to perform all the below operations 
	
		a. Click on Create an App
		b. You will land up on default page and then click “Lets’ get started
		c. Create a new page and give it a name

	iv. created the messaging(Defination) to perform all the below operations
	
		a. Click on “Messaging” group appearing on the left pane under MODULES
		b. Drag component “Send an SMS” to the main app page & join the line from start acting as connector
		c. Fill the details of Phone Number and Message text

	v.  created the darg_an_email(Defination) to perform all the below operations
	
		a. Drag component “Send an email” from the left module and join line from “Not sent” output port.
		b. fill all the details of the mail
	
	vi. created the exit_app_sent_sms(Defination) to perform all the below operations
	
		a. Click on component “Basic” on left Module and drag “Exit App” joining to “Sent” output port of Sent an sms  box
	
	vii. created the exit_app_email(Defination) to perform all the below operations
	
		a. Similarly, Join all the open output ports of “Send an Email” to Exit app by dragging
	
	viii. Created the shut_down(Defination) to close the open browser in the first step

5. In the task.py(Main File) , i have created the object to that class and I have called all the definations to perfom the scenario.

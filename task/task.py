import os
import time
import json
import ast
from locators import *
from WebElementActions import WebElementActions
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#To load the config variables from the variables.json file
conf = json.load(open("C:/Users/ksunku/Desktop/project/task/variables.json",'r'))  # to load the config values to change this path

class Task():

	def __init__(self):
		chromedriver = "C:/Users/ksunku/Downloads/chromedriver_win32/chromedriver.exe" # need to change the path to use chromedriver
		os.environ["webdriver.chrome.driver"] = chromedriver
		self.driver = webdriver.Chrome(chromedriver)
		self.webactions = WebElementActions(self.driver)
		self.webactions.UsingMyBrain()
		self.driver.get("http://google.com")
		self.driver.maximize_window()
		object=self.driver.find_element_by_name("q")
		# I have opened the quickfuseapps page
		self.driver.get("http://quickfuseapps.com/")
		self.webactions.UsingMyBrain()
		logo = self.driver.find_element_by_xpath(LogoFeild) # Here I am checking the logo
		if logo.is_displayed():
			print("Element found")
		else:
			print("Element not found")

	def create_app(self):
		'''
			2. Click on Create an App
			3. You will land up on default page and then click “Lets’ get started
			4. Create a new page and give it a name
		'''
		try:
			self.driver.find_element_by_xpath(createappButton).click()
			self.webactions.UsingMyBrain()
			self.driver.find_element_by_xpath(popupbutton).click()
			self.webactions.UsingMyBrain()
			self.driver.find_element_by_xpath(newpagebutton).click()
			self.webactions.UsingMyBrain()
			self.driver.find_element_by_xpath(createapppage).send_keys(str(conf['createpage']))
			self.webactions.UsingMyBrain()
			self.driver.find_element_by_xpath(createbutton).click()
		except Exception as e:
			raise

	def messaging(self):
		'''
			5. Click on “Messaging” group appearing on the left pane under MODULES
			6. Drag component “Send an SMS” to the main app page & join the line from start acting as connector
			7. Fill the details of Phone Number and Message text

		'''
		try:
			self.driver.find_element_by_xpath(messagingtabbutton).click()
			time.sleep(2)
			source_element = self.driver.find_element_by_xpath(sendansmsdrag)
			ActionChains(self.driver).drag_and_drop_by_offset(source_element,700,-5).perform()
			self.webactions.UsingMyBrain()
			node1 = self.driver.find_element_by_xpath(startbuttonsource)
			node2 = self.driver.find_element_by_xpath(sendansmsdestinationnotsent)
			ActionChains(self.driver).drag_and_drop(node1,node2).perform()
			time.sleep(2)
			self.driver.find_element_by_xpath(phonenumberinput).send_keys(conf['sendphonenumber'])
			time.sleep(2)
			self.driver.find_element_by_xpath(messagetextvariableinput).send_keys(conf['sendmessagetext'])
			time.sleep(2)
		except Exception as e:
			raise

	def darg_an_email(self):
		'''
			8. Drag component “Send an email” from the left module and join line from “Not sent” output port.Also fill all the details of the mail as shown
		'''
		try:
			source_element = self.driver.find_element_by_xpath(sendanemaildrag)
			time.sleep(2)
			ActionChains(self.driver).drag_and_drop_by_offset(source_element,970,170).perform()
			self.webactions.UsingMyBrain()
			node3 = self.driver.find_element_by_xpath(sendansmssource)
			node4 = self.driver.find_element_by_xpath(sendanemaildestination)
			ActionChains(self.driver).drag_and_drop(node3,node4).perform()
			time.sleep(2)
			self.driver.find_element_by_xpath(smtphost).send_keys(conf['smtphost'])
			self.driver.find_element_by_xpath(port).send_keys(conf['port'])
			self.driver.find_element_by_xpath(Username).send_keys(conf['username'])
			self.driver.find_element_by_xpath(Password).send_keys(conf['password'])
			self.driver.find_element_by_xpath(From).send_keys(conf['from'])
			self.driver.find_element_by_xpath(To).send_keys(conf['to'])
			self.driver.find_element_by_xpath(Subject).send_keys(conf['Subject'])
			self.driver.find_element_by_xpath(sendanemailmsgtextvariable).send_keys(conf['sendanemailmsgtextvariable'])
			self.webactions.UsingMyBrain()
		except Exception as e:
			raise


	def exit_app_sent_sms(self):
		'''
			9.Click on component “Basic” on left Module and drag “Exit App” joining to “Sent” output port of Sent an sms  box
		'''
		try:
			self.driver.find_element_by_xpath(basicbutton).click()
			time.sleep(4)
			source_element = self.driver.find_element_by_xpath(hanguporexit)
			ActionChains(self.driver).drag_and_drop_by_offset(source_element,470,270).perform()
			self.webactions.UsingMyBrain()
			node5 = self.driver.find_element_by_xpath(sendansmssourcesent)
			node6 = self.driver.find_element_by_xpath(hanguporexitdestination)
			self.webactions.UsingMyBrain()
			ActionChains(self.driver).drag_and_drop(node5,node6).perform()
			self.webactions.UsingMyBrain()
		except Exception as e:
			raise

	def exit_app_email(self,params):
		'''
			#10. Similarly, Join all the open output ports of “Send an Email” to Exit app by dragging
		'''
		try:
			source_element = self.driver.find_element_by_xpath(hanguporexit)
			if params == 'sent_port':
				time.sleep(2)
				ActionChains(self.driver).drag_and_drop_by_offset(source_element,850,560).perform()
				self.webactions.UsingMyBrain()
				node7 = self.driver.find_element_by_xpath(sendanemailsentsource)
				node8 = self.driver.find_element_by_xpath(hanguporexitdestinationforsentemail)
				self.webactions.UsingMyBrain()
				ActionChains(self.driver).drag_and_drop(node7,node8).perform()
				time.sleep(2)
			elif params == 'Not_sent_port':
				time.sleep(2)
				ActionChains(self.driver).drag_and_drop_by_offset(source_element,1250,560).perform()
				self.webactions.UsingMyBrain()
				node9 = self.driver.find_element_by_xpath(sendanemailnotsentsource)
				node10 = self.driver.find_element_by_xpath(hanguporexitdestinationfornotsentemail)
				self.webactions.UsingMyBrain()
				ActionChains(self.driver).drag_and_drop(node9,node10).perform()
				time.sleep(5)
			elif params == 'both':
				time.sleep(2)
				ActionChains(self.driver).drag_and_drop_by_offset(source_element,850,560).perform()
				self.webactions.UsingMyBrain()
				node7 = self.driver.find_element_by_xpath(sendanemailsentsource)
				node8 = self.driver.find_element_by_xpath(hanguporexitdestinationforsentemail)
				self.webactions.UsingMyBrain()
				ActionChains(self.driver).drag_and_drop(node7,node8).perform()
				time.sleep(2)
				ActionChains(self.driver).drag_and_drop_by_offset(source_element,1250,560).perform()
				self.webactions.UsingMyBrain()
				node9 = self.driver.find_element_by_xpath(sendanemailnotsentsource)
				node10 = self.driver.find_element_by_xpath(hanguporexitdestinationfornotsentemail)
				self.webactions.UsingMyBrain()
				ActionChains(self.driver).drag_and_drop(node9,node10).perform()
				time.sleep(5)


		except Exception as e:
			raise

	def shut_down(self):
		'''
			closing the browser
		'''
		self.driver.close()


# Here i am creating the object for that class
test =Task()
# here i am calling all the definations to start the task
test.create_app()
test.messaging()
test.darg_an_email()
test.exit_app_sent_sms()
test.exit_app_email('both')
test.shut_down()

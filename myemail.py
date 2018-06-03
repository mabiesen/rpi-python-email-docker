#!flask/bin/python
import smtplib
import json

class myemail:
	
	def __init__(self):
		cred = json.load(open('creds.txt'))
		self.username = cred['username']
		self.password = cred['password']

	def send_email(self,recipient,msg="empty",title="emptytitle",fname="dunno",lname="dunno",toself=False):
		smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
		smtpObj.ehlo()
		smtpObj.starttls()
		smtpObj.login(self.username, self.password)
		if toself==True:
		    smtpObj.sendmail(self.username,self.username,
			"Subject: New email from site!" +
			"\n\nnew email from " + recipient + 
			"\n\n" + "Fullname: " + fname + " " + lname +
			"\n\n" + "Title: " + title + 
			"\n\n" + "Message: "+ msg +
			"\n\n thank you, your site")
		smtpObj.sendmail(self.username,recipient,
		    "Subject: Thank you for contacting me!" +
		    "\nI appreciate your time, I will contact you shortly")
		smtpObj.quit()

                

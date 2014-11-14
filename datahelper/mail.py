#coding:utf-8
# Author:LuYu
# Date:2014-11-14

import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage  
  
class EmailHelper(object):
    """docstring for EmailHelper"""
    def __init__(self, sender , smtpserver ,username ,password):
        super(EmailHelper, self).__init__()
        self.sender = sender
        self.smtp = smtplib.SMTP()
        self.smtp.connect(smtpserver)
        self.smtp.login(username, password)

    def setContent(self,title,msg):
        self.msgRoot = MIMEMultipart('related') 
        text = MIMEText(msg, 'html') 
        self.msgRoot['Subject'] = title
        self.msgRoot.attach(text)

    def send(self,receiver):
        self.smtp.sendmail(self.sender, receiver, self.msgRoot.as_string())

    def addAttach(self,filepath,rename):
        att = MIMEText(open(filepath, 'rb').read(), 'base64', 'utf-8')  
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="{rename}"'.format(rename=rename)  
        self.msgRoot.attach(att)

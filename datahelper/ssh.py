import pexpect
import pxssh
import os
class Ssh(object):
    """docstring for ssh"""
    def __init__(self, hostname,  username,password):
        super(Ssh, self).__init__()
        try:
            self.host     = hostname
            self.user     = username
            self.password = password
            self.ssh      = pxssh.pxssh()
            self.ssh.login(hostname, username, password)
        except Exception, e:
            print("pxssh failed on login.")
            print(e)
            raise e

    def run(self,cmd):
        self.ssh.sendline(cmd)
        self.ssh.prompt()
        return self.ssh.before

    def logout(self):
        self.ssh.logout()

    def scp2(self, filename, dst_path):  
        if os.path.isdir(filename):  
            cmdline = 'scp -r %s %s@%s:%s' % (filename, self.user, self.host, dst_path)  
        else:  
            cmdline = 'scp  %s %s@%s:%s' % (filename, self.user, self.host, dst_path)  
        try:      
            child = pexpect.spawn(cmdline)  
            child.expect('password:')  
            child.sendline(self.password)  
            child.expect(pexpect.EOF)  
            #child.interact()  
            #child.read()  
            #child.expect('$')  
            print "uploading"  
        except: 
            print "upload faild!"
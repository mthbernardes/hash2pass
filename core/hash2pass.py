import time
import requests
from tempMail import tempMail

class HashToPass:
    def __init__(self,):
        self.confi_file = 'etc/token.txt'

    def getEmail(self,):
        m = tempMail.mailer()
        email = m.getEmail()
        return email,m

    def receiveEmail(self,m):
        while 1:
            result = m.mailBox()
            if result:
                token = result['body'].split('<strong>')[1].split('</strong>')[0]
                break
            time.sleep(2)
        open(self.confi_file,'w').write('%s:%s'%(token,self.emailAccount))
        return token

    def register(self,email):
        url = 'http://md5decrypt.net/en/Api/'
        s = requests.Session()
        headers = {'Referer':'http://md5decrypt.net/en/Api/','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Host':'md5decrypt.net','Upgrade-Insecure-Requests': '1'}
        r = s.get(url,headers=headers)
        cookies = dict(r.cookies)
        data = {'email_api':email}
        r = requests.post(url,cookies=cookies,headers=headers,data=data)

    def crackHash(self,hash,hash_type,email,code):
        params = {'hash':hash,'hash_type':hash_type,'email':email,'code':code}
        site = 'http://md5decrypt.net/Api/api.php'
        r = requests.get(site,params=params)
        if '001' in r.content or '002' in r.content or '006' in r.content:
            print r.content
            self.createAccount()
            print 'Account created, try again'
        elif 'PDO' in r.content:
            print 'Error, try again!'
        else:
            return r.content

    def createAccount(self,):
        print '[+] - Getting an API'
        self.emailAccount,m = self.getEmail()
        self.register(self.emailAccount)
        token = self.receiveEmail(m)
        print '[+] - Saving api key'
        open(self.confi_file,'w').write('%s:%s'%(token,self.emailAccount))
        print "API KEY: %s\nEmail: %s" % (token,self.emailAccount)
        return self.emailAccount,token

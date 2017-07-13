import os
from core.hash2pass import HashToPass

while 1:
    crack = HashToPass()
    hashid = raw_input("hash: ")
    hashtype = raw_input("hash type [md4,md5,sha1,sha256,sha384,sha512,ntlm]: ")
    if not os.path.exists(crack.confi_file):
        emailAccount,token = crack.createAccount()
    token,emailAccount = open(crack.confi_file).read().split(':')
    password = crack.crackHash(hashid,hashtype,emailAccount,token)
    if password:
        print '[+] - Cracked password: %s\n' % password

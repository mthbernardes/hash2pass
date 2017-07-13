# hash2pass
Crack the hash using the <a href="http://md5decrypt.net/">md5decrypt.net</a> API, the hash2pass will automatically create a account to you, if you reach the limit of queries, the hash2pass will register another account.

# install
<pre>
pip install -r requeriments.txt
</pre>

# Usage
<pre>
➜  hash2pass python main.py
hash: 5fee00239940f883d4c2854e41c7f989e75278a3
hash type [md4,md5,sha1,sha256,sha384,sha512,ntlm]: sha1
[+] - Getting an API
[+] - Saving api key
API KEY: YOUR_HASH_KEY
Email: TEMP_EMAIL@TEMPEMAIL.COM
[+] - Cracked password: nicole
</pre>

# Source
<a href="http://md5decrypt.net/">md5decrypt.net</a>

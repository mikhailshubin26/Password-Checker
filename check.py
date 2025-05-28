import hashlib
import requests

def checker(pwd):
	sha1=hashlib.sha1(pwd.encode()).hexdigest().upper()
	prefix=sha1[:5]
	suffix=sha1[5:]
	url=f"https://api.pwnedpasswords.com/range/{prefix}"
	resp=requests.get(url)
	matches=suffix in resp.text
	if matches:
		return ["Пароль ненадёжный", "red"]
	return ["Пароль надёжный", "green"]
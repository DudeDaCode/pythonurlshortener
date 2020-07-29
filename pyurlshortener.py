import pyshorteners

s = pyshorteners.Shortener()
Url = input("Enter Your Url : ")
print(s.tinyurl.short(f'{Url}'))

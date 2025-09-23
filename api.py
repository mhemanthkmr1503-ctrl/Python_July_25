import requests
from rich import print

username = input("Enter your usernamae : ")

url = "https://api.github.com/users/" + username

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()

print("Username :", data['login'])
print("Name :", data['name'])
print("Email :", data['email'])
print("Bio :", data['bio'])
print("Location :", data['location'])
print("Repo Count :", data['public_repos'])

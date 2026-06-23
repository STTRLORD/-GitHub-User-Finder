import requests

username=input("enter your name ->")

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

data = response.json()
try:
  if response.status_code==200 :
    print(data["name"])
    print(data["followers"])
    print(data["following"])
    print(data["public_repos"])
    print(data["location"])
    print(data["created_at"])
    print(data["bio"])
  else :
   print("user not found")

except Exception as e:
    print("Error :", e)

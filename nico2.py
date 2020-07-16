import os
import requests

os.system('cls')

print("Welcome to IsItDown.py!")
while True:
  print("Please write a URL or URLs you want to check. (seqarated by comma)")


  pages = input("")
  for page in [page.strip() for page in pages.split(',')]:
    print(page)
    normal = "http://"
    goodpage = normal + page

    try:
      if page.startswith(normal):
        response = requests.get(page)
        if 200 == response.status_code:
          print(f"{page} is up!")
      elif not page.endswith(".com"):
        print(f"{page} is not a valid url.")
      else:
        response = requests.get(goodpage)
        if 200 == response.status_code:
          print(f"{goodpage} is up!")
    except:
      print(f"{page} is down!")

  while True:
    choice = input("Do you want to start over? y/n ")
    if choice == "y":
      break
    elif choice == "n":
      exit()
    else:
      print("That's not a valid answer.")
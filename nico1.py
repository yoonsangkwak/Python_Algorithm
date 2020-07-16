import os
import requests

os.system('cls')


a = True
b = True

while a == True:

    print("Welcome to IsItDown.py!")
    print("Please write a URL or URLs you want to check. (seqarated by comma)\n")

    page = input("")
    normal = "http://"
    # goodpage = normal + page
    strip_page = []
    lower_page = []
    splitted_page = page.split(",")
    # print(splitted_page)

    i = 0
    while i < len(splitted_page):
        strip_page.append(splitted_page[i].strip())
        i += 1
    # print(strip_page)

    i = 0
    while i < len(strip_page):
        lower_page.append(strip_page[i].lower())
        i += 1
    # print(lower_page)
    
    i = 0
    while i < len(lower_page):
        try:
            if normal in lower_page[i]:
                response = requests.get(lower_page[i])
                if 200 == response.status_code:
                    print(f"{lower_page[i]} is up!")
                    while b == True:
                        choice = input("Do you want to start over? y/n ")
                        if choice == "y":
                            a = True
                            b = False
                        elif choice == "n":
                            a = False
                            b = False
                        elif choice != "y" or choice != "n":
                            print("That's not a valid answer.")
                
            elif "." not in lower_page[i]:
                print(f"{lower_page[i]} is not a valid url.")
                while b == True:
                    choice = input("Do you want to start over? y/n ")
                    if choice == "y":
                        a = True
                        b = False
                    elif choice == "n":
                        a = False
                        b = False
                    elif choice != "y" or choice != "n":
                        print("That's not a valid answer.")
            elif normal not in lower_page[i]:
                goodpage = []
                goodpage[i] = "http://" + lower_page[i]
                # print(goodpage)
                response = requests.get(goodpage[i])
                if 200 == response.status_code:
                    print(f"{goodpage[i]} is up!")
                    while b == True:
                        choice = input("Do you want to start over? y/n ")
                        if choice == "y":
                            a = True
                            b = False
                        elif choice == "n":
                            a = False
                            b = False
                        elif choice != "y" or choice != "n":
                            print("That's not a valid answer.")
        except:
            print(f"{lower_page[i]} is down!")
            while b == True:
                choice = input("Do you want to start over? y/n ")
                if choice == "y":
                    a = True
                    b = False
                elif choice == "n":
                    a = False
                    b = False
                elif choice != "y" or choice != "n":
                    print("That's not a valid answer.")
        i += 1
                    
                    
                        
                        
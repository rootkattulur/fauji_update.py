from datetime import datetime

print("===== FAUJI UPDATE SYSTEM =====")

title = input("Enter update title: ")

current_date = datetime.now().strftime("%d-%m-%Y")

print("\n----- OUTPUT -----")
print("Title :", title)
print("Date  :", current_date)
print("------------------")

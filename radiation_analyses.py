# This programm aims to manage data regarding to radiation level of certain locations.
# It allows the user to enter, delete, update an alanyse the data.
# The data is stored in a .csv file.
# The functions to create, update, delete and analyse the data are in a separate file (radiation_functions.py)


import pandas as pd
from statistics import stdev
from radiation_functions import *

# Open file with stored radiation level.
#file_name = "radiation_data.csv"
file_name = "C:\\Users\\Rafael\\OneDrive\\Coding\\Courses\\Bootcamp\\Portfolio Session\\Week2 - Radiation Exposure Analysis\\Project\\radiation_data.csv"
file = pd.read_csv(file_name, usecols=["location", "radiation_level"])
file.index.name = "position"

# Menu of Options
menu = """
    1. Enter new data
    2. Update
    3. Delete
    4. Analyze
    5. Finish
"""


# Initial greetings
print(
f"""
{"="*60}
{"Welcome to the Radiation Level Analysis".center(60)}
{"="*60}
"""
)

if len(file) == 0:
    print("Currently there is no radiation level in our dataset.\n")
else:
    print("These are the radionation level priviouly stored.\n")
    print(file.groupby("location")["radiation_level"].agg(["mean", "std"]))

print(f"{'='*60}\n")
print('Any time you want to exit this program, please type the word "done".\n')


# Beggining of the Program
question = ""
while True:
    
    # File lenght == 0. Ask user if they want to enter data
    if len(file) == 0:
        question = input("Would you like to enter new data? (yes/no/done) ").lower()
        print("")

        if question == "yes":
            input_data(file)
        
        elif question == "done" or (question == "no" and len(file) == 0):
            print("Thank you for using our sistem!\n")
            break

        elif question == "no":
            continue
        
        else:
            print("Wrong option.\n")
    
    # File lenght > 0. Ask user if they want to enter, update, delete or analyse data
    if len(file) > 0:
        
        if question == "done":
            break

        else:
            question = input(f"What would you like to do now: {menu} \nPlease, select an option (1, 2, 3, 4 or 5): ").lower().strip()
            print("")

            if question in ("1", "enter"):
                input_data(file)
            
            elif question in ("2", "update"):
                update_data(file)
            
            elif question in ("3", "delete"):
                file = delete_data(file)

            elif question in ("4", "analyze"):
                analyse_data(file)

            elif question in ("done", "5", "finish"):
                break


# Store update to the file
while True:
    confirmation = input("Please, confirm that you want to overwrite the database with the update made so far (yes/no): ").lower().strip()
    print("")
    
    if confirmation not in ("yes", "no"):
        print("Invalid option.\n")
    
    elif confirmation == "yes":
        file.to_csv(file_name)
        print(f"Update made to the file {file_name}.")
        break
    
    elif confirmation == "no":
        print(f"No update make to the file {file_name}.")
        break
        
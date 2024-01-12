def input_data(dataframe):
    """
    This function will enter new data into the a pandas DF with the structure "location","radiation_level".
    Parameters:
        dataframe (dataframe): a dataframe with the structure.
    Returns:
        dataframe (dataframe): the update dataframe.
    """
    while True:
        location = input("Please, inform the location (one per time): ").strip().lower()
        print("")
        
        if location == "done":
            return dataframe
        
        elif location.replace(" ", "").isalpha():
            break

        else:
            print("Something is wrong with the entered data.\n")
    

    while True:
        values = input("Please, informe the radiation levels found (separete with comma): ").replace(" ", "").lower()
        print("")
        
        if values == "done":
            return dataframe
        
        elif all(map(lambda x: x.isdigit(), values.split(","))):
            break
        
        else:
            print("Something is wrong with the entered data.\n")
    
    
    values = values.split(",")
    if len(dataframe) == 0:
        start = -1
    else:
        start = len(dataframe)
    
    for index, item in enumerate(values, start=1):
        dataframe.loc[start + index] = [location.upper(), item]

    print("New data entered.\n")
    return dataframe


def update_data(dataframe):
    """
    This function will update data of a pandas DF with the structure "location","radiation_level".
    Parameters:
        dataframe (dataframe): a dataframe with the structure.
    Returns:
        dataframe (dataframe): the update dataframe.
    """

    current_location = ' '.join(dataframe['location'].drop_duplicates())

    print(f"This is the list o location stored so far: {current_location}\n")

    while True:
        location = input("Please, inform the location (one per time): ").strip().lower()
        print("")

        if location == "done":
            return dataframe

        elif location.replace(" ", "").isalpha():

            if location.upper() in current_location:
                print("This is the data regarding the location typed.\n")
                print(dataframe[dataframe["location"] == location.upper()])
                print("")
                break
            
            else:
                print("Data typed does not match the list of location.\n")

        else:
            print("Something is wrong with the entered data.\n")


    while True:
        position = input("Please, inform the position to change (one per time): ").strip().lower()
        print("")
        
        if position == "done":
            return dataframe

        elif position.isdigit():
            current_position = list(dataframe[dataframe["location"] == location.upper()].index)

            if int(position) in current_position:
                break

            else:
                print("This position does not exist.\n")

        else:
            print("Something is wrong with the entered data.\n")


    while True:
        new_value = input("Please, informe the new radiation levels: ").replace(" ", "").lower()
        print("")
        
        if new_value == "done":
            return dataframe
        
        elif new_value.isdigit():
            try:
                new_value = int(new_value)
                break
            except:
                print("Something is wrong with the entered data.\n")
        
        else:
            print("Something is wrong with the entered data.\n")


    dataframe.loc[int(position), "radiation_level"] = new_value
    print("Data update.\n")
    return dataframe


def delete_data(dataframe):
    """
    This function will delete data of a pandas DF with the structure "location","radiation_level".
    Parameters:
        dataframe (dataframe): a dataframe with the structure.
    Returns:
        dataframe (dataframe): the update dataframe.
    """

    # Menu of Options
    menu = """
        1. Delete all data
        2. Detele all data of a specific location
        3. Delete specific radiation level of a specific location
    """

    question = input(f"What would you like to do now: {menu} \nPlease, select an option (1, 2 or 3): ").lower().strip()
    while True:

        if question == "done":
            return dataframe

        elif question.isdigit():
            
            try:
                question = int(question)

                if question in [1, 2, 3]:
                    break

                else:
                    print("Invalid option.\n")
                    question = input(f"Please, try again. Select an option (1, 2 or 3): ").lower().strip()

            except:
                print("Invalid option.\n")
                question = input(f"Please, try again. Select an option (1, 2 or 3): ").lower().strip()

        else:
            print("Invalid option.\n")
            question = input(f"Please, try again. Select an option (1, 2 or 3): ").lower().strip()
    

    while True:
    
        if question == 1:
            dataframe = dataframe.drop(index=dataframe.index)
            print("All data has just been deleted.")
            return dataframe

        elif question == 2:
            
            current_location = ' '.join(dataframe['location'].drop_duplicates())

            print(f"This is the list o location stored so far: {current_location}\n")

            while True:
                location = input("Please, inform the location (one per time): ").strip().lower()
                print("")

                if location == "done":
                    return dataframe

                elif location.replace(" ", "").isalpha():

                    if location.upper() in current_location:
                        
                        first_index = dataframe[dataframe["location"]==location.upper()].first_valid_index()
                        last_index = dataframe[dataframe["location"]==location.upper()].last_valid_index() + 1
                        index_range = list(range(first_index, last_index))
                        
                        dataframe = dataframe.drop(index=index_range)
                        dataframe = dataframe.reset_index()
                        print(f"The data regarding the location {location.upper()} has just been deleted.\n")
                        return dataframe
                    
                    else:
                        print("Data typed does not match the list of location.\n")

                else:
                    print("Something is wrong with the entered data.\n")


        elif question == 3:
            current_location = ' '.join(dataframe['location'].drop_duplicates())

            print(f"This is the list o location stored so far: {current_location}\n")

            while True:
                location = input("Please, inform the location (one per time): ").strip().lower()
                print("")

                if location == "done":
                    return dataframe

                elif location.replace(" ", "").isalpha():

                    if location.upper() in current_location:
                        print("This is the data regarding the location typed.\n")
                        print(dataframe[dataframe["location"] == location.upper()])
                        print("")
                        break
                    
                    else:
                        print("Data typed does not match the list of location.\n")

                else:
                    print("Something is wrong with the entered data.\n")


            while True:
                position = input("Please, inform the position to delete (one per time): ").strip().lower()
                print("")
                
                if position == "done":
                    return dataframe

                elif position.isdigit():
                    current_position = list(dataframe[dataframe["location"] == location.upper()].index)

                    if int(position) in current_position:
                        dataframe = dataframe.drop(int(position))
                        dataframe = dataframe.reset_index()
                        print("Data deleted.")
                        return dataframe

                    else:
                        print("This position does not exist.\n")

                else:
                    print("Something is wrong with the entered data.\n")


def analyse_data(dataframe):
    """
    This function will analyse data of a pandas DF with the structure "location","radiation_level".
    Parameters:
        dataframe (dataframe): a dataframe with the structure.
    Returns:
        dataframe (dataframe): a dataframe with some information.
    """

    # Menu of Options
    menu = """
        1. List all data
        2. List data of a specific location
        3. Display the Average and Standard Deviation of all data
    """

    question = input(f"What would you like to do now: {menu} \nPlease, select an option (1, 2 or 3): ").lower().strip()
    while True:

        if question == "done":
            return dataframe

        elif question.isdigit():
            
            try:
                question = int(question)

                if question in [1, 2, 3]:
                    break

                else:
                    print("Invalid option.\n")
                    question = input(f"Please, try again. Select an option (1, 2 or 3): ").lower().strip()

            except:
                print("Invalid option.\n")
                question = input(f"Please, try again. Select an option (1, 2 or 3): ").lower().strip()

        else:
            print("Invalid option.\n")
            question = input(f"Please, try again. Select an option (1, 2 or 3): ").lower().strip()
    

    while True:
    
        if question == 1:
            return print(dataframe)
        

        elif question == 2:
            current_location = ' '.join(dataframe['location'].drop_duplicates())

            print(f"This is the list o location stored so far: {current_location}\n")

            while True:
                location = input("Please, inform the location (one per time): ").strip().lower()
                print("")

                if location == "done":
                    return dataframe

                elif location.replace(" ", "").isalpha():

                    if location.upper() in current_location:
                        
                        return print(dataframe[dataframe["location"]==location.upper()])
                    
                    else:
                        print("Data typed does not match the list of location.\n")

                else:
                    print("Something is wrong with the entered data.\n")


        elif question == 3:
            return print(f'\n{dataframe.groupby("location")["radiation_level"].agg(["mean", "std"])}\n\n')
        
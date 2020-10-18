def add_new_friend():
    while True:
        try:
            name = (str(input("Enter your friend's first and last name"
                              " seperated by a space, omit prefixes"
                              " and suffixes: ")))
            birthday = input("Enter birthday in this format MM/DD/YYYY"
                             " use a leading zero for months 1-9 and"
                             " if you don't know the year, enter any"
                             " year in the last 100 years.")
            if not su.is_full_string(name):
                raise ValueError("Enter a name.")
            elif su.is_number(name):  # name is not just numbers
                raise ValueError("Enter a name, not a number.")
            elif not name.count(" ") == 1:  # name is not two words
                raise ValueError("Enter two names with a space in between")
            if validate_date(birthday) == False:
                raise ValueError("You did not enter a valid birthday.")
        except ValueError as error:
            print(error)
        else:
            break



def validate_date(date):
    " "
    NUMB_IDX = (0, 1, 3, 4, 6, 7, 8, 9)
    PUNC_IDX = (2, 5)
    DATES_DICT = {30: [4,6,9,11], 29: 2, }

    # quickly check presence of punctuation and length
    if (date.count("/") == 2) and (len(date) == 10):
        return True
    else:
        return False
    
    # check type and position
    for char in range(0, len(date)):
        if (date[char].isdigit()) and (char in NUMB_IDX) and\
           (date[char] == "/") and (char in PUNC_IDX):
            return True
        else:
            return False
    
    # validate date
    month, day, year = date.split("/")
    thirties = [4, 6, 9, 11]
    thirty_ones = [1, 3, 5, 7, 8, 10, 12]

    if (int(month) in range(1, 13)) and (int(day) in range(1, 32)) and\
       (int(year) in range(1920, 2021)):
        continue
    elif (int(month) == 2) and (int(day) < 30):
        return True
    elif (int(month) in thirties) and (int(day) < 31):
        return True
    elif (int(month) in thirty_ones) and (int(day) < 32):
        return True
    else:
        return False
    
    
    


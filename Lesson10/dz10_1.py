
def month_name():
    # Define simple dictionary about mounthes
    dict_months = {
        '1': 'January',
        '2': 'February',
        '3': 'March',
        '4': 'April',
        '5': 'May',
        '6': 'June',
        '7': 'July',
        '8': 'August',
        '9': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }

# Cycle for checking month number

    while True:
        month_number = input("\nEnter month number: ")
        try:
            if not month_number.isdigit():
                raise ValueError()
            print(dict_months[month_number])
            break
        # If month number is too big or 0
        except KeyError:
            print("You enter incorrect month number. Try again")
            continue
        # if month number is float or negative or any other incorrect symbol
        except ValueError:
            print("You enter incorrect symbol for month number. Try again")
            continue

month_name()

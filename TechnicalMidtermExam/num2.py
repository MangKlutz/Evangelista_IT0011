from datetime import datetime

def format_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        formatted_date = date_obj.strftime("%B %d, %Y")
        print(f"Today is {formatted_date}")
    except ValueError:
        print("Wrong Format. Please use mm/dd/yyyy.")

date_input = input("Enter the date (mm/dd/yyyy): ")
format_date(date_input)
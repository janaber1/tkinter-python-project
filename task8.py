from datetime import datetime

def convert_date_format(date_str):
    try:
        # convert string to date
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        # Format the date as "DD-MM-YYYY"
        # method srftime()   object is (date obj  )and format string to date d-m-y
        formatted_date = date_obj.strftime("%d-%m-%Y")
        return formatted_date
    except ValueError:#invalid input
        return "Invalid date format. Please use the format YYYY-MM-DD."

# Example usage:
input_date = "2024-04-26"
output_date = convert_date_format(input_date)
print(output_date)  # Output: 26-04-2024

# Example with invalid input:
invalid_input = "2024/04/26"
output_date = convert_date_format(invalid_input)
print(output_date)  # Output: Invalid date format. Please use the format YYYY-MM-DD.

#func date format
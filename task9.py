from datetime import datetime

def convert_date_format(date_str, input_format="%Y-%m-%d", output_format="%d-%m-%Y"):
    try:
        # Parse the input date string
        date_obj = datetime.strptime(date_str, input_format)
        # Format the date as specified
        formatted_date = date_obj.strftime(output_format)
        return formatted_date
    except ValueError:
        return "Invalid date format. Please check the input format and try again."

# Example usage:
input_date = "2024-04-26"
output_date = convert_date_format(input_date)
print(output_date)  # Output: 26-04-2024

custom_input_date = "04/26/2024"
custom_output_date = convert_date_format(custom_input_date, input_format="%m/%d/%Y", output_format="%d-%m-%Y")
print(custom_output_date)  # Output: 26-04-2024


# Example with invalid input:
invalid_input = "2024/04/26"
output_date = convert_date_format(invalid_input)
print(output_date)  # Output: Invalid date format. Please use the format YYYY-MM-DD.

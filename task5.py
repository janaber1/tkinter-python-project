def replace_with_stars(string):
    if len(string) <= 5:
        return string
    else:
        return '*' * (len(string) - 5) + string[-5:]

original_string = "kdi39323swe"
new_string = replace_with_stars(original_string)
print("Original String:", original_string)
print("New String:", new_string)

def replace_with_stars(string):
    if len(string) <= 5:
        return string
    else:
        return '*' * (len(string) - 5) + string[-5:]

original_string = "12345abcdef"
new_string = replace_with_stars(original_string)
print("Original String:", original_string)
print("New String:", new_string)

def replace_with_stars(string):
    if len(string) <= 5:
        return string
    else:
        return '*' * (len(string) - 5) + string[-5:]

original_string = "12345"
new_string = replace_with_stars(original_string)
print("Original String:", original_string)
print("New String:", new_string)



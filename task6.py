#txt = "Hello World"[::-1]
#print(txt)
def reverse_string(input_string):
    reversed_string = ""
    index = len(input_string) - 1
    while index >= 0:
        reversed_string += input_string[index]
        index -= 1
    return reversed_string

input_string = "hello world"
reversed_string = reverse_string(input_string)
print("Original String:", input_string)
print("Reversed String:", reversed_string)


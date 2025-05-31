
# Reading console Inputs and formatting outputs

txt = input("Can you see this? Yes or No") # automatically converts input into a string
print("you said", txt)

txt = input("Give me a number: ")

try: 
    num = int(txt)
    print("the number you entered was: ", num)

except:
    print("Please enter only a number with the prompt")


salary = 40000
txt = "You make {} pounds a year. {} pounds is how much you make" # {field_name:conversion}
print(txt.format(salary, salary))
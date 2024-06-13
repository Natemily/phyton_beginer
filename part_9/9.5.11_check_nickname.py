line = input()
if (
    line.startswith("@") 
    and (line[1:].isalnum() 
    and (line.islower()) 
    or line[1:].isdigit()) 
    and 4 < len(line) < 16
):
    print("Correct")
else:
    print('Incorrect')
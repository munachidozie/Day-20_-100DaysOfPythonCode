print("== List Generator ==")
print()
starting_number = int(input("What number are you starting with?  "))
final_number = int(input("What number are we ending with?  "))
increment = int(input("What is the increment between the values?  "))
print()

for list in range (starting_number, final_number, increment):
  print(list)
def guess_number(minimum, maximum):
  
  if minimum == maximum:
    return minimum
  else:
    middle = (minimum + maximum) // 2
    answer = input("Is your number {}? ".format(middle))
    if answer == "yes":
      return middle
    elif answer == "no":
      answer = input("Is your number higher or lower than {}? ".format(middle))
      if answer == "higher":
        return guess_number(middle + 1, maximum)
      else:
        return guess_number(minimum, middle - 1)
    else:
      print("Invalid answer.")

number = int(input("Enter the maximum number: "))
guessed_number = guess_number(1, number)
print("The secret number was {}!".format(guessed_number))

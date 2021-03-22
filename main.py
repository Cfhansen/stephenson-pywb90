###solution to problem 90 in ben stephenson's "the python workbook".

def is_integer(value):
  good = True

  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

  for i in range(len(value)):
    if (value[i] == '+' or value[i] == '-') and i == 0:
      continue
    elif value[i] in numbers:
      continue
    else:
      good = False
      break
  return good

val = str(input('Enter a string to be tested: '))
print(f'Is that string an integer: {is_integer(val)}.')

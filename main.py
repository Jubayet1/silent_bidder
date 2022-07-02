from replit import clear
from art import logo
is_on = True
record = {}
def highest_bidder(record):
  name = ''
  price = 0
  for key in record:
    if record[key] > price:
      name = key
      price = record[key]
  print(f'highest bidder is {name} and his/her bid is {price}')
while is_on :
  print(logo)
  name = input("Enter Your Name  ")
  amount = int(input("Enter Your amount of bid  "))
  record[name] = amount
  should_continue = input('Want to add more   yes or no  ')
  if should_continue == 'yes':
    clear()
  else:
    is_on = False
highest_bidder(record)
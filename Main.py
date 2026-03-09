#Define variables
int first_term = 0
string operator = ""
int rate_of_growth = 0
int search_term = 0
#Function to enter variables as user input
def inputs():
  first_term = int(input("Enter the first term of the sequence: "))
  print("")
  operator = string(input("Enter the operator of growth (+, -, *, /): "))
  print("")
  rate_of_growth = int(input("Enter the rate of growth: "))
  print("")
  search_term = int(input("Enter the term you wish to search: "))

#Function with if statement that solves values based on operator

#Function to restart from beginning or solve for term

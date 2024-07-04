import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y' ,'z',]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '+']
print("Wlecome to the Password Generator")
num_letters = int(input("How many letters do you wnat in your password\n"))
num_numbers = int(input("How many numbers do you want in your password\n"))
num_symbols = int(input("How many symbols do you want in your password\n"))
if num_letters <= len(letters) and num_numbers <= len(numbers) and num_symbols <= len(symbols):

    total_letter = ""
    for letter in range(0,num_letters):
        letter = letters[random.randint(0,int(len(letters)-1))]
        total_letter += letter
 
    total_number = ""
    for number in range(0,num_numbers):
        number = numbers[random.randint(0,int(len(numbers)-1))]
        total_number += number

    
    total_symbols = ""
    for symbol in range(0,num_symbols):
        symbol = symbols[random.randint(0,int(len(symbols)-1))]
        total_symbols += symbol
    totals =total_letter+total_number+total_symbols
    new_total = ""
    for total in range(0,len(totals)):
        total = totals[random.randint(0,len(totals)-1)]
        new_total += total
    print(new_total)
else:
    print("Invalid input")
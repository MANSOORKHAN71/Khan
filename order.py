

from re import I




name=input("Whats your Name Sir")

print( name + " ,welcome to Starbucks")

menu="Latte, Espresso ,Cappucino , Black Coffe"

print( name + " What will you like to try from our menu? \n" + menu )

order=input()

quantity=input("How Much " +  order  + " you want " + name  )

price = 30

total = price * quantity

print(total)
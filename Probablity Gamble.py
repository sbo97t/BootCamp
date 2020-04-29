#Probablity Gamble

print("Enter the probablity")
prob = float(input("Chance of winning"))
prize = float(input("Amount of prize"))
cost_of_play = float(input("Cost of play"))

if prob == prob * prize > cost_of_play:
    print("Place you bets")
else:
    print("Time to go home") 

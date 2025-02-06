# guess number
a = int(input("enter  a guess:"))
while(a>1) or (a<9):
    a = int(input("enter a guess:"))
else:
    print("well guessed")    
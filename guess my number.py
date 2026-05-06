password=7
while True:
    guess=int(input("guess the number!"))
    if guess==password:
        print("correct")
    else:
        print("wrong")
        
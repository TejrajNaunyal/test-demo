print("welcome to quiz game where you can have chance to won 1 crore in every correct question and every wrong question will reset the game! ")

playing = input("DO you ready for the game? ")

if playing.lower() != "yes":
    quit()

print("ok ! let play the game : )")
price_money = 0 

answer = input('what is the capital of the Nepal? ') 
if answer.lower() == "kathmandu":
    print("correct you won 1 crore")
    price_money += 1
else:
    print("Game is Reset you have good luck next time")
    
answer = input('what is the national animal of the Nepal? ')
if answer.lower() == "cow":
    print("correct answer you won 1 crore")
    price_money += 1
else:
    print("game is reset and you have better luck next time")
    
answer = input("who is the prime minsiter of the nepal? ")
if answer.lower() =="sher bahadur deuba":
    print("correct answer you won 1 crore")
    price_money += 1
else:
    print("game is reset and you have better luck next time")
    

print("you won the price money " + str(price_money ) + " crore!")

print("you got " +str((price_money/3) * 100) + " %"  + " of the price money " + " congracluation for your achievement")
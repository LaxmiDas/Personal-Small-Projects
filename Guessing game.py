word = "Love"
guess = ""
cnt = 1
win = False
while cnt<=3:
    guess = input("Enter guess : ")
    if guess==word:
        win = True
    cnt+=1
if win==True:
    print("You win :) ")
else:
    print("You lose :( ")
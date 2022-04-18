import random
def choose():
    words=['rainbow','computer','science','programming','encouragement','reverse','while','function','mathematics']
    pick=random.choice(words)
    return pick
def jumble(word):
    m="".join(random.sample(word,len(word)))
    return m
def thank(p1n,p2n,p1,p2):
    print("summary of the game: ")
    print(p1n,'Your sore is : ',p1)
    print(p2n,'Your sore is : ',p2)
    if p1>p2: 
        print(p1n,'you won the game.')
    elif p1==p2:
        print("The game is Draw")
    else:
        print(p2n,'Better luck next time')
    print('Thanks for playing .\nHave a nice day.\nHope you again play here')
def play():
    p1=input("player 1: Enter your name : ")
    p2=input("player 2: Enter your name : ")
    points_p1=0
    points_p2=0
    turn=0
    while(1):
        #computer task to ensure fairness of the game without bias
        picked_word=choose()
        #create random word
        qn=jumble(picked_word)
        print(qn)
        if turn%2:
            print(p1,"Your turn , guess the right word : ")
            ans=input()
            if ans==picked_word:#if the guess of the player 1 is correct
                points_p1=points_p1+1
                print("right answer \n",p1,"Your points : ",points_p1)
            else: #if the guess of the player 1 is wrong
                print("wrong answer, right word is ",picked_word,"\nbetter luck next time :(\n")
                print(p1," Your points : ",points_p1)
            c=int(input("press 1 to continue 0 to end the game : "))
        else:
            print(p2,"Your turn , guess the right word : ")
            ans=input()
            if ans==picked_word:#if the guess of the player 2 is correct
                points_p2=points_p2+1
                print("right answer \n",p2,"Your points : ",points_p2)
            else:#if the guess of the player 2 is wrong
                print("wrong answer, right word is ",picked_word,"\nbetter luck next time :(\n")
                print(p2," Your points : ",points_p2)
            c=int(input("press 1 to continue 0 to end the game :"))
        if c==0:
            thank(p1,p2,points_p1,points_p2)
            break
        turn=turn+1
play()
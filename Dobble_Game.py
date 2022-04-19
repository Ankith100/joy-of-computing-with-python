import string
import random
symbols=list(string.ascii_letters)
print("Deck of symbols :")
print(symbols)
card1=[0]*5
card2=[0]*5
pos1=random.randint(0,4)
pos2=random.randint(0,4)
samesymbol=random.choice(symbols)
symbols.remove(samesymbol)
card1[pos1]=samesymbol
card2[pos2]=samesymbol
i,j=0,0
while i<5 and j<5 :
	if i!=pos1:
		a=random.choice(symbols)
		symbols.remove(a)
		card1[i]=a
	if j!=pos2:
		b=random.choice(symbols)
		symbols.remove(b)
		card2[j]=b
	i+=1
	j+=1
print("two set of cards having one symbol in common :")
print(card1)
print(card2)
ch=input("spot the similar symbol ")
if ch==samesymbol:
	print("Right answer")
else:
	print("wrong answer")
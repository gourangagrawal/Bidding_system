
#HINT: You can call clear() to clear the output in the console.
bids={}
def gtr():
  name_of_person=input("What is your name? : ")
  bid_by_him=int(input("What's your bid? : "))
  bids[name_of_person]=bid_by_him

def winner():
  y=0
  z=''
  names=[]
  winners={}
  q=0
  global bids
  for i in bids:
    if bids[i]>y:
      winners[i]=bids[i]
      z+=i
  for i in bids:
      if bids[i]==winners[z]:
          winners[i]=bids[i]
          q+=1
  for i in winners:
      names+=str(i)
  if q==0:
      print(f"The winner is {z} with a bid of {winners[z]}.")
  else:
      print(f"The winners are {names}, with bid amount of {winners[z]}")
      
      
x=1
while x>0:
  gtr()
  ask=input("Is there anyone else with a bid? type yes or no.\n")
  if ask=="yes":
      continue
  else:
      x-=1
      winner()



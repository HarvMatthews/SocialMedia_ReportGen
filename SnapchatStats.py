import os


from MessageStats import FindTopMessages

amount = "a"
while not amount.isdigit():
    print("How many ranks of people do you want to see?")
    amount = input()


for i in range(2):
    Top5Stats = FindTopMessages(int(amount), i)
    Top5 = Top5Stats[0]
    User = Top5Stats[1]
    Top5.reverse()
    
    if i == 0:
        message = 'messages'
    elif i == 1:
        message = '(Saved) Snaps'
    
    print('Youve sent %d %s' % (User[1], message))
    for Pos in range(len(Top5)):
        people = Top5[Pos]
        print(Pos + 1, ' Recieved %d from %s' % (people[1], people[0]))
    print('\n')

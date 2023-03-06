print("Welcome to my computer quiz!")

playing = input("Do you want to playthe game? (yse to play)")

if playing.lower() != "yes": # for Yes, YES, YEs, YeS, ...
    quit()
print('Ok! Let play')

score = 0
answer = input('What does CPU stand for?')
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

answer = input('What does GPU stand for?')
if answer.lower() == "graphic processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

answer = input('What does SSD stand for?')
if answer.lower() == "solid state drive":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

answer = input('What does RAM stand for?')
if answer.lower() == "random accessing memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

print("You got " + str(score)) 


#I made 2 files for 3 individuals where their diet and exercises are recorded.And this program retrive 
#their data according to user input.

var1=int(input("Press 1, 2 or 3: "))

def getDate():
    import datetime
    return datetime.datetime.now()

if var1 == 1:
    print("Mona's File")
    var2=int(input("Press 1 for Diet , press 2 for exercise: "))
    if var2 == 1:
        f= open("monaDiet.txt")
        content=f.read()
        print([getDate()]," ",content)
    else:
        f= open("monaExercise.txt")
        content=f.read()
        print([getDate()]," ",content)


elif var1 == 2:
    print("Sona's File")
    var2=int(input("Press 1 for Diet , press 2 for exercise: "))
    if var2 == 1:
        f= open("sonaDiet.txt")
        content=f.read()
        print([getDate()]," ",content)
    else:
        f= open("sonaExercise.txt")
        content=f.read()
        print([getDate()]," ",content)

else:
    print("Dona's File") 
    var2=int(input("Press 1 for Diet , press 2 for exercise: "))
    if var2 == 1:
        f= open("donaDiet.txt")
        content=f.read()
        print([getDate()]," ",content)
    else:
        f= open("donaExercise.txt")
        content=f.read()
        print([getDate()]," ",content)

#example code data. a way to enter data can be made later
newlist = []
weeklyneeds = ["greens", "beans", "tomatoes", "potatoes", "eggs", "lamb", "ram", "sugar", "hogs", "dogs", "lemons"]
currentstock = ["eggs", "sugar", "oranges"]
grocerylist = []

#input for weekly required list (later, just stick with test input for now)


#(repeating every time the program opens) input for currentstock


#output list
for i in weeklyneeds:
    if i not in currentstock:
        grocerylist.append(i)

print(grocerylist)

#add extra items or recipe (optional)



#recipe saving function
recipelist = {}
def saverecipe(recipename):
    print("enter the ingredients for this recipe")
    recipeingredients = []
    while True:
        i = input("")
        if i == "end list":
            break
        else:
            if i not in recipeingredients:
                recipeingredients.append(i)
            else:
                print("item already in list")
    recipelist[recipename] = recipeingredients

#option to change weeklyneeds

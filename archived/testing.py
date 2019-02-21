from archived.utils import Utils

myRecipeDict = {}
myWeeklyNeedsList = []
myUtil = Utils(recipeDict=myRecipeDict, weeklyNeedsList=myWeeklyNeedsList)

while True:
  recipeName = input("Enter a recipe name: ")
  if len(recipeName) > 0:
    break

myUtil.saveRecipe(recipeName, myRecipeDict)

print(myRecipeDict)
print(myWeeklyNeedsList)
print(myUtil.recipeDict)
print(myUtil.weeklyNeedsList)

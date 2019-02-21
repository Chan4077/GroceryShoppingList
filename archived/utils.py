import inflection
# from firebase_admin import firestore
from typing import List, Dict
import platform

"""
Class for a list of utilities
"""
class Utils:
  recipeDict = {}
  weeklyNeedsList = []
  def __init__(self, recipeDict: Dict[str, List[str]], weeklyNeedsList: List[str]):
    """
    Creates a new instance of the utility class
    """
    self.recipeDict = recipeDict
    self.weeklyNeedsList = weeklyNeedsList

  @staticmethod
  def addToWeeklyNeeds(myList: List):
    """
    Adds a grocery item to the weekly needs list
    """
    while True:
      i = input("")
      if i == "end list":
        break
      else:
        if i not in myList:
          myList.append(i)
  # TODO: Implement GUI functionality
  @staticmethod
  def changeList(e: str, recipeDict: Dict[str, List], weeklyNeedsList: List):
    """
    Internal function used to change the grocery list.
    """
    if e == "add":
      print("Enter the groceries needed:")
      while True:
        i = inflection.singularize(input("")).lower()
        if i == "end list":
          break
        elif i in recipeDict:
          for l in recipeDict[i]:
            if l not in weeklyNeedsList:
              weeklyNeedsList.append(l)
        else:
          if i not in weeklyNeedsList:
            weeklyNeedsList.append(i)
          else:
            print("The grocery specified is already in the list!")
    elif e == "minus":
      print("Enter the groceries to delete from the grocery list:")
      while True:
        i = inflection.singularize(input("")).lower()
        if i in ["end list", "end", "end input", "exit"]:
          break
        else:
          try:
            weeklyNeedsList.remove(i)
          except ValueError:
            print("Item is not in the list!")
  @staticmethod
  def saveRecipe(recipeName: str, recipeDict: Dict[str, List]):
    """
    Saves a recipe to a dictionary
    """
    print("Enter the ingredients for this recipe:")
    recipeIngredients = []
    while True:
        i = input("")
        if i == "end list":
          if not recipeIngredients:
            print("Please enter an ingredient before breaking!")
          else:
            break
        else:
            if i not in recipeIngredients:
                recipeIngredients.append(inflection.singularize(i))
            elif len(i) == 0:
              print("Please specify an item!")
            else:
              print("The item specified is already in the list!")
    recipeDict[recipeName] = recipeIngredients

  @staticmethod
  def getSystem():
    """
    Gets the system that this Python script is running on
    """
    try:
      return platform.system()
    except:
      return "N/A"

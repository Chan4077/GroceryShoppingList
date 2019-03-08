from typing import List


class SortingAlgorithm:
    def __init__(self, data: List[List[str]]):
        self.data = data
        self.high = []
        self.middle = []
        self.low = []
        """
        Example data structure:
        Name | Ability | Gender
        ---|---|---
        John Lim | High | M
        """
        for i in data:
            if i[1].lower() == "high" or i[1].lower() == "h":
                self.high.append(i[0])
            elif i[1].lower() == "middle" or i[1].lower() == "m":
                self.middle.append(i[0])
            elif i[1].lower() == "low" or i[1].lower() == "l":
                self.low.append(i[0])
        self.biggest_ability = []
        self.smallest_ability = []
        self.middle_ability = []
        self.final_list = []

        abilities_sorted = sorted([self.high, self.middle, self.low], key=len, reverse=True)

        print("Sorted abilities:", abilities_sorted)
        self.biggest_ability = abilities_sorted[0]
        self.middle_ability = abilities_sorted[1]
        self.smallest_ability = abilities_sorted[2]

        print("Self smallest ability:", self.smallest_ability)
        print("Self middle ability:", self.middle_ability)
        print("Self biggest ability:", self.biggest_ability)

    def sort_ability(self):
        # Clear any existing elements in the list
        # self.final_list.clear()
        self.final_list = []
        print("Final list (start):", self.final_list)
        self.final_list.append(self.high)
        self.final_list.append(self.middle)
        self.final_list.append(self.low)
        print("Final list (end):", self.final_list)
        return self.final_list

    def __sort_values(self, ability_group: List[str], groups: int) -> List[int]:
        result = []
        for n in range(groups):
            result.append(len(ability_group) // groups)
        for v in range(len(ability_group) % groups):
            result[v] += 1
        return result

    def sort_mixed(self, groups: int):
        # Assign locally so as to not overwrite the class variable
        smallest_ability = self.smallest_ability
        middle_ability = self.middle_ability
        biggest_ability = self.biggest_ability

        print("Smallest ability:", smallest_ability)
        print("Middle ability:", middle_ability)
        print("Biggest ability:", biggest_ability)

        print("Self smallest ability:", self.smallest_ability)
        print("Self middle ability:", self.middle_ability)
        print("Self biggest ability:", self.biggest_ability)

        # Sorting smallest/middle/biggest abilities into equal numbers in groups
        smallest_ability_grp = self.__sort_values(smallest_ability, groups)
        smallest_ability_grp.sort(reverse=True)
        # self.smallestabilitygrp.sort()
        middle_ability_grp = self.__sort_values(middle_ability, groups)
        middle_ability_grp.sort()
        biggest_ability_grp = self.__sort_values(biggest_ability, groups)
        biggest_ability_grp.sort()
        mixed_ability = []
        # Clear any existing elements in the final list
        # self.final_list.clear()
        self.final_list = []
        for i in range(groups):
            mixed_ability.append([smallest_ability_grp[i], middle_ability_grp[i], biggest_ability_grp[i]])
            grouper = []
            for x in range((mixed_ability[i])[0]):
                grouper.append(smallest_ability[0])
                smallest_ability.pop(0)
            for x in range((mixed_ability[i])[1]):
                grouper.append(middle_ability[0])
                middle_ability.pop(0)
            for x in range((mixed_ability[i])[2]):
                grouper.append(biggest_ability[0])
                biggest_ability.pop(0)
            self.final_list.append(grouper)

        return self.final_list

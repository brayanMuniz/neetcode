from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for every str in strs: 
            # if its not in a group
                # add it to a group that matches its alphabetical ordering
            # if no group matches its alphabetical ordering 
                # create a new group and make its alphabetical ordering 
        groups = []
        orderings = []
        for string in strs:
            order = ''.join(sorted(string))
            if order not in orderings:
                groups.append([string])
                orderings.append(order)
            else: 
                idx = orderings.index(order)
                groups[idx].append(string)
        return groups
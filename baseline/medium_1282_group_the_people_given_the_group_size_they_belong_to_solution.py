from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupSize_ids_map = defaultdict(list)
        
        for idx, grpSize in enumerate(groupSizes):
            groupSize_ids_map[grpSize].append(idx)
        
        groups = [] # Final Answer

        for grpSize, ids in groupSize_ids_map.items():
            # Here grpSize will be the Size of Group
            # ids is List of ID's             
            numOfPeople = len(ids)

            if numOfPeople <= grpSize:
                # Ex: No. of People with GroupSize = 2 are 2,,Id's List is [0,5]
                # Then Simply Append that List into Final Answer
                groups.append(ids)

            elif grpSize == 1 and numOfPeople > 1:
                # Ex: No. of People with GroupSize = 1 are 3,,Id's List is [0,2,3]
                # Then we have to make 3 Lists --> [0],[2],[3]
                for i in range(numOfPeople):
                    groups.append( [ids[i]] )

            elif numOfPeople % grpSize == 0:
                # Ex : No. of People with GroupSize = 3 are 6,,Id's List is [0,1,2,3,4,6]

                # Let's Get Number of Parts/Divisions to make
                numOfDivisions = (numOfPeople // grpSize)

                # Using 2 Points for Slicing 
                ptr1, ptr2 = 0, grpSize
                while numOfDivisions:
                    sub_grp = ids[ ptr1 : ptr2 ] # sub_grp has exactly "grpSize" number of people 
                    groups.append(sub_grp)                    

                    # Updating the Pointers,, such that they should point to Next Part/Division
                    ptr1 = ptr2
                    ptr2 = ptr2 + grpSize

                    numOfDivisions -= 1

        return groups
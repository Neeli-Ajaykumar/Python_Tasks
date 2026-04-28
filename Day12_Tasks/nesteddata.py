""" Nested Data Independence (Deep Copy) 
A school stores classroom data: 
classes = [["Math", [30, 35]], ["Science", [25, 28]]] 
Scenario: 
● Create a deep copy of this structure. 
● Modify student count in original. 
Task: 
● Prove that copied data remains unchanged. 
● Explain why deep copy is required here. """

import copy

classes = [["Math", [30, 35]], ["Science", [25, 28]]] 
c = copy.deepcopy(classes)
c[0][1][0] = 100

print("original:", classes)
print("After deepcopy:", c)
print("Is copied data remains unchanged", c != classes)


"""Deep copy is required because the data contains nested lists.
It creates completely separate copies of all inner objects.
So modifying the original does not affect the copied data."""

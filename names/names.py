import time
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print("Using a Loop in a Loop:")
print(f"runtime: {end_time - start_time} seconds")

#---------- New Code - using BST -----------
start_time = time.time()


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        if self.value == value:
            return
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        if value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value and self.left:
            return self.left.contains(target)
        if target > self.value and self.right:
            return self.right.contains(target)
        return False


duplicates = []  # Return the list of duplicates in this data structure

bst = BSTNode(names_1[0])

for name in names_1:
    bst.insert(name)


for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print("Using a BTS:")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


start_time = time.time()

duplicates = []
d = {}

for name in names_1:
    d[name] = True

for name in names_2:
    if name in d:
        duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print("Using a dictionary:")
print(f"runtime: {end_time - start_time} seconds")


start_time = time.time()

duplicates = []
s1 = set(names_1)
s2 = set(names_2)
duplicates = list(s1.intersection(s2))


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print("Using intersection:")
print(f"runtime: {end_time - start_time} seconds")

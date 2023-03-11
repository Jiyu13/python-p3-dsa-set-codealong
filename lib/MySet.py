class MySet:

    def __init__(self, ls=[]):
        self.dictionary = {}
        for value in ls:
            self.dictionary[value] = True


    def has(self, value):
        # if value in self.dictionary.keys():
        #     return True
        # return False
        return value in self.dictionary

    
    def __str__(self):
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f"MySet: {{{','.join(set_list)}}}"


    def add(self, value):
        # if value not in self.dictionary.keys():
        #     self.dictionary[value] = True
        # return self
        self.dictionary[value] = True # Add a value as a key on the Dictionary
        return self                   # Return the updated set

    
    def delete(self, value):
        # if value in self.dictionary.keys():
        #     del self.dictionary[value]
        #     return self.dictionary
        self.dictionary.pop(value, None)    # return None if value doesn't exist
        return self 
    
    def size():
        return len(self.dictionary)


    def clear(self):
        return self.dictionary.clear()

example = MySet([1,2,3,3,4,4])
print(example.add(5))
# <__main__.MySet object at 0x7fe4fb265730>

print(example.dictionary)
# {1: True, 2: True, 3: True, 4: True, 5: True}


print(example.__str__())
# MySet: {1,2,3,4,5}

# print(example.clear())
# # None
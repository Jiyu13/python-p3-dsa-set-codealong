# find the first repeated value in a list without using Set
def first_repeated_value(list):
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                return list[i]
    return None


print(first_repeated_value([1,2,3,3,4,4])) #=> 3
print(first_repeated_value([1,2,3,4]))     # => None


# find the first repeated value in a list using Set
def first_repeated_value_with_set(list):
    # create a Set to keep track of values we've seen
    number_set = set()
    # iterate over each element from the list
    for i in range(0, len(list)):
        # if we've already seen a value, we've found the duplicate!
        if list[i] in number_set:
            return list[i]
        # otherwise, add the value to our set
        number_set.add(list[i])
    # return None if we reach the end and haven't found our value
    return None

print(first_repeated_value_with_set([1,2,3,3,4,4])) # => 3
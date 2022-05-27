# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

# from collections import Counter


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if sorted(word) == sorted(anagram):
        return True
    else:
        return False


print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))

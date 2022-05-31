# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    remaining_anagram = anagram
    for letter in word:
        if letter in remaining_anagram:
            remaining_anagram = remaining_anagram.replace(letter, '', 1)
           
    if remaining_anagram == "":
        return True
    else:
        return False


print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))

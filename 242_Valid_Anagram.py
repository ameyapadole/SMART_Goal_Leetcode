import collections

def anagram(s, t):
    hashset = collections.defaultdict(int)
    for char in s: 
        hashset[char] += 1
    for char in t:
        hashset[char] -= 1
    
    for value in hashset.values():
        if value != 0:
            return False 
    return True 

print(anagram("anagram","nagaram" ))
"""
Time Complexity: 
O(N)

Space Complexity: 
O(1)
"""

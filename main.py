# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    # [assignment] Add your code here
    if len(word1)!=len(word2):
        return False
    else: 
        srt_word1 = sorted(word1)
        srt_word2 = sorted (word2)

        return srt_word1==srt_word2



# finding anagram in words
s1 = 'listen'
s2 = 'silent'
sorted1 = sorted(s1)
sorted2 = sorted(s2)
if sorted1 == sorted2:
    print('this is anagram')
else:
    print('not a anagram')
    
# finding anagram in sentence
# inputt = list(input().split()) -- output will be --  ['hello', 'all']

sentence1 = 'hi iam listen to a music race'
sentence2 = 'i will be care happy if your are silent'

# Split the sentences into words
words1 = sentence1.split()
words2 = sentence2.split()

# Initialize a list to store anagrams
anagrams = []

# Compare each word in the first sentence with each word in the second sentence
for word1 in words1:
    sorted_word1 = sorted(word1)
    for word2 in words2:
        sorted_word2 = sorted(word2)
        if sorted_word1 == sorted_word2:
            anagrams.append(word1)

print("Anagrams found:", len(anagrams))


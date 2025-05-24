"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
         'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'played', '⚽.', 'they']

story_indices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Use indexing to get the words from the list

myStory = [words[0], words[2], words[7], words[9], words[8], words[1], words[-6], words[-7], words[-3], words[-2]   ]

# Display the story
print(' '.join(myStory))
celestial_objects = [
    'Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid'
]

word_counts = {}
word_list=celestial_objects
for word in word_list:
    word_counts[word] = word_counts.get(word, 0) + 1

# Print the counts with formatting
for word, count in word_counts.items():
    print(f"{word:<12}{count}")

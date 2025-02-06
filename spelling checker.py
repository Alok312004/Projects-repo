from spellchecker import SpellChecker

# Initialize SpellChecker
spell = SpellChecker()

# Get user input
text = input("Enter text to check spelling: ")

# Split text into words
words = text.split()

# Find misspelled words
misspelled = spell.unknown(words)

# Correct misspelled words
corrected_text = []
for word in words:
    if word in misspelled:
        corrected_text.append(spell.correction(word))
    else:
        corrected_text.append(word)

# Join corrected words into a single string
corrected_text = ' '.join(corrected_text)

# Print corrected text
print("Corrected text:", corrected_text)

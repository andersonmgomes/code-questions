# Problem: A ransom note can be formed by cutting words out of a magazine to form a new
# sentence. How would you figure out if a ransom note (string) can be formed from a given
# magazine (string)?

def ransom_note_is_from_magazine(ransom_note, magazine):
    # find the frequency of each word in ransom_note
    words_freq = {}
    ransom_note_words = ransom_note.split()
    for word in ransom_note_words:
        if word not in words_freq:
            words_freq[word] = 0
        words_freq[word] += 1
    # iterate over magazine to check if all words are present
    magazine_words = magazine.split()
    for word in magazine_words:
        if word in words_freq:
            words_freq[word] -= 1
            if words_freq[word] == 0:
                del words_freq[word]
                if not words_freq:
                    # It's not necessary iterate more
                    return True
    
    # else: words_freq has still some word
    return False

# test cases
print(ransom_note_is_from_magazine('give me one grand today night', 'give one grand today')) # False
print(ransom_note_is_from_magazine('give me one grand today night', 'give me one grand today night')) # True
print(ransom_note_is_from_magazine('give me one grand today night', 'abc def fgh give ijl me kmn one opq grand today night')) # True
print(ransom_note_is_from_magazine('give me one grand today night', 'give one grand today night night')) # False
print(ransom_note_is_from_magazine('give me one grand today night', 'give one grand today night night night')) # False
print(ransom_note_is_from_magazine('give me one grand today night', 'give one grand today night night night night')) # False
print(ransom_note_is_from_magazine('give me one grand today night', 'give one grand today night night night night night')) # False


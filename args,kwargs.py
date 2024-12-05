def single_root_words(root_word, *other_words):
    same_words = []
    root_word_lower = root_word.lower()
    for other_word in other_words:
        other_word_lower = other_word.lower()
        if other_word_lower.count(root_word_lower) > 0 or root_word_lower.count(other_word_lower) > 0:
            same_words.append(other_word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)

print(result2)
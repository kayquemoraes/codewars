def duplicate_count(text):
    text = text.lower()
    letters = []
    for i in range(len(text)):
        for j in range(len(text)):
            if i != j:
                if text[i] == text[j] and text[i] not in letters:
                    letters.append(text[i])
    return len(letters)
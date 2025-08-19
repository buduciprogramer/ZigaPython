def pig_latin_word(word):
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        return word + "yay"
    else:
        for i in range(len(word)):
            if word[i] in vowels:
                return word[i:] + word[:i] + "ay"
        return word + "ay"  # ako nema samoglasnika

def pig_latin_sentence(sentence):
    words = sentence.split()
    result = []

    for word in words:
        suffix = ""
        if not word[-1].isalpha():
            suffix = word[-1]
            word = word[:-1]
        translated = pig_latin_word(word)
        result.append(translated + suffix)

    return " ".join(result)


recenica = input("Unesi rečenicu: ")
print("Pig Latin:", pig_latin_sentence(recenica))
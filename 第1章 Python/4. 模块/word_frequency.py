import string

def word_count(text):
    words = text.lower().split()
    for i in range(len(words)):
        words[i] = words[i].strip(string.punctuation)

    frequency = dict()
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def sort_by_count(frequency):
    frequency = list(frequency.items())
    frequency.sort(key=lambda w: w[1], reverse=True)
    return frequency

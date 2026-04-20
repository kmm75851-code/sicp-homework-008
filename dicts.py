def word_count(text):
    count = {}
    
    for word in text.split():
        word = word.lower()
        count[word] = count.get(word, 0) + 1

    return count

def group_by_length(words):
    count = {}
    for i in words:
        if len(i) not in count:
            count[len(i)] = [i] 
        else:
            count[len(i)].append(i)

    return count

def invert_dict(d):
    count = {}

    for x, y in d.items():
        if y not in count:
            count[y] = [x]

        else:
            count[y].append(x)

    return count

def merge_dicts(*dicts):

    result = {}
    for d in dicts:
        result.update(d)
    return result

def most_common(text, n):
    freq = word_count(text)
    if not freq:
        return []

    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    return [word for word, _ in sorted_words[:n]]

def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in seen:
            return (seen[diff], i)

        seen[num] = i


def char_frequency(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    return count

def index_builder(documents):
    count = {}

    for x, y in documents.items():
        for i in y.split(): 
            count.setdefault(i, set()).add(x)
    return count  
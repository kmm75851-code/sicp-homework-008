def word_count(text):
    count = {}
    
    for word in text.split():
        word = word.upper()
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
    count = {}
    
    for d in dicts:
        for x, y in d.items():
            count[x] = y
    return count

def most_common(text, n):
    text = word_count(text)
    text = sorted(text.items(), key=lambda x: -x[1])

def two_sum(nums, target):
    sum = {}
    for i in range(len(nums)):
        sum[nums[i]] = i 
    for i in range(len(nums) - 1):
        if nums[i] + nums[i + 1] == target:
            return (sum[nums[i]] , sum[nums[i + 1]])



def char_frequency(s):
    count = {}
    for i in s.split():
        if i not in count:
            count[i] = 1
        else:
            count[i] +=1

def index_builder(documents):
    count = {}

    for x, y in documents.items():
        for i in y.split(): 
            count.setdefault(i, set()).add(x)
    return count
def unique_words(text):
    words = set()

    for word in text.split():
        words.add(word.lower())

    return words

def common_words(text1, text2):
    return set(text1.split()) & set(text2.split())

def only_in_first(text1, text2):
    return set(text1.split()) - set(text2.split())

def dedup_preserve_order(items):
    seen = set()
    lst = []
    for x in items:
        if x not in seen:
            seen.add(x)
            lst.append(x)
    return lst 

def anagram_groups(words):
    groups = {}

    for word in words:
        key = tuple(sorted(word))
        
        if key not in groups:
            groups[key] = []
        
        groups[key].append(word)

    result = []
    
    for group in groups.values():
        result.append(sorted(group))
    
    return result

def set_stats(items):
    seen = {}
    
    
    for x in items:
        seen[x] = seen.get(x, 0) + 1
    
    duplicates = {x for x, count in seen.items() if count > 1}
    unique_only = {x for x, count in seen.items() if count == 1}
    
    return {
        "unique_count": len(seen),
        "duplicates": duplicates,
        "unique_only": unique_only
        
    }


print(set_stats([1, 2, 2, 3, 3, 3, 4]))    

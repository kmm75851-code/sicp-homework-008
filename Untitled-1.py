def analyze(text):
    seen = {}
    
    
    for x in text.split():
        seen[x] = seen.get(x, 0) + 1
    best = ''
    for x in seen:
        if len(x) > len(best):
            best = x
    unique_only = {x for x, count in seen.items() if count == 1}
    return {
        'total_words': len(text.split()),
        'unique_words': len(seen),
        'word_counts': seen,
        'most_common': max(seen, key=seen.get),
        'longest_word': best,
        'avg_word_length': round(sum(len(x) for x in seen) / len(seen),2),
        'appears_once': unique_only,
    }

result = analyze("the cat sat on the mat the cat")
print(result)

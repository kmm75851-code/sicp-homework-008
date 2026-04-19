def analyze(text):
    seen = {}
    
    
    for x in text.split():
        x = x.lower()
        seen[x] = seen.get(x, 0) + 1

    best = ""
    for x in seen:
        if len(x) > len(best):
            best = x
        elif len(x) == len(best):
            best = min(x, best)
        
    unique_only = {x for x, count in seen.items() if count == 1}
    return {
        'total_words': len(text.split()),
        'unique_words': len(seen),
        'word_counts': seen,
        'most_common': max(seen, key=seen.get) if seen else None,
        'longest_word': best,
        'avg_word_length': round(sum(len(x) for x in seen) / len(seen),2)if seen else 0,
        'appears_once': unique_only,
    }

def make_analyzer():
    text = ""  
    def adder(n):
        nonlocal text
        if text:
            text += " " + n
        else:
            text = n

    def stats():
        return analyze(text)

    return adder, stats
    


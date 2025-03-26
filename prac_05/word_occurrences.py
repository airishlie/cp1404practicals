"""
Word Occurences Counter

Estimate time : 15 minutes
Actual Time : 27 February 2025 (7pm - 7.15pm)
"""
def main():
    """Counts the occurences of words and displays in alphabetical order"""
    text = input("Text: ")
    words = text.split()
    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    max_word_length = max(len(word) for word in word_counts)

    for word in sorted(word_counts):
        print(f"{word:{max_word_length}} : {word_counts[word]}")

main()
import re

def find_longest_words(text):
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return [], 0
    max_len = max(len(word) for word in words)
    longest = [word for word in words if len(word) == max_len]
    return longest, max_len

if __name__ == "__main__":
    text = input("Enter text: ")
    longest_words, length = find_longest_words(text)
    if longest_words:
        print(f"Longest word(s): {', '.join(longest_words)} ({length} characters)")
    else:
        print("No words found.")


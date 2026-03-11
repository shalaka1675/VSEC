# Simple String Operations

def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

def count_vowels(text):
    """Count vowels in a string"""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def is_palindrome(text):
    """Check if a string is a palindrome"""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def capitalize_words(text):
    """Capitalize first letter of each word"""
    return " ".join(word.capitalize() for word in text.split())

if __name__ == "__main__":
    test_string = "hello world"
    print(f"Original: {test_string}")
    print(f"Reversed: {reverse_string(test_string)}")
    print(f"Vowels: {count_vowels(test_string)}")
    print(f"Palindrome: {is_palindrome('racecar')}")
    print(f"Capitalized: {capitalize_words(test_string)}")

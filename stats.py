def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    lower_case_text = str.lower(text)
    chars = {}
    for char in lower_case_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

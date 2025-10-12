def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    lower_case_text = text.lower()
    chars = {}
    for char in lower_case_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sorted_list(chars):
    output = []
    for key in chars:
        num = chars[key]
        item = {}
        item["char"] = key
        item["num"] = num
        #item = {"char": key, "num": num}
        if not key.isalpha():
            continue
        
        output.append(item)

        #print(f"{key} {num}")
        #print(item)
    output.sort(key=sort_on, reverse=True)
    return output

def sort_on(element):
    return element["num"]

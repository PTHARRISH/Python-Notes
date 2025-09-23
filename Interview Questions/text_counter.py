def frequent_count_text(text):
    dict_count = {}
    for i in text.split():
        if i.lower() in dict_count:
            dict_count[i.lower()] += 1
        else:
            dict_count[i.lower()] = 1
    return dict_count

# Example usage:
input_text = "This is a sample text with several words this is a test text"
result = frequent_count_text(input_text)
print(result)

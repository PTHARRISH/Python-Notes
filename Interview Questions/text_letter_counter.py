# Repeated words and letter counter and display top num letters and word their counts and remove punctuation


def frequent_count_text(text, num=3):
    word_count = {}
    text_count = {}
    for i in text.split():
        if i.lower() in word_count:
            word_count[i.lower()] += 1
        else:
            word_count[i.lower()] = 1
        for j in i:
            if j.lower() in text_count:
                text_count[j.lower()] += 1
            else:
                text_count[j.lower()] = 1
    top_words = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))[:num]
    top_letters = sorted(text_count.items(), key=lambda kv: (-kv[1], kv[0]))[:num]
    # 4) Format outputs and return (letters first, words second)
    letter_lines = [f"Top {num} letter:"]
    letter_lines += [f"{ch}: {cnt}" for ch, cnt in top_letters]

    word_lines = [f"Top {num} word:
                  "]
    word_lines += [f"{w}: {cnt}" for w, cnt in top_words]

    letter_output = "\n".join(letter_lines)
    word_output = "\n".join(word_lines)
    return f"{letter_output}\n\n{word_output}"


# Example usage:
input_text = "This is a sample text with several words this is a test text"
result = frequent_count_text(input_text, 3)
print(result)

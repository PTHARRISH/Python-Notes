class Vowels:
    def __init__(self, data):
        self.data = data
        self.vowels = ["a", "e", "i", "o", "u"]

    def filter_non_vowels(self):
        result = "".join(
            [char for char in self.data if char.lower() not in self.vowels]
        )
        return result

    def filter_vowels(self):
        result = "".join([char for char in self.data if char.lower() in self.vowels])
        return result


# Example usage:
input_string = "Hello World"
vowel_filter = Vowels(input_string)
print("String after removing vowels:", vowel_filter.filter_non_vowels())
print("String with only vowels:", vowel_filter.filter_vowels())

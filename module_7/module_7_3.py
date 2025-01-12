import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.all_words = self.get_all_words()

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(str.maketrans('', '', string.punctuation))
                    words = line.split()
                    if file_name not in all_words:
                        all_words[file_name] = []
                    all_words[file_name].extend(words)
        return all_words

    def find(self, word):
        result = {}
        word = word.lower()
        for file_name, words in self.all_words.items():
                position = words.index(word) + 1
                result[file_name] = position
        return result

    def count(self, word):
        result = {}
        word = word.lower()
        for file_name, words in self.all_words.items():
            count = words.count(word)
            if count > 0:
                result[file_name] = count
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))


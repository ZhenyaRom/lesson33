class WordsFinder:
    def __init__(self, *files):
        self.file_name = files

    def get_all_words(self):
        all_words = {}
        for i in self.file_name:
            with open(i, 'r', encoding='UTF-8') as file:
                words = file.read().lower()
            for j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                words = words.replace(j, ' ')
            all_words[i] = words.split()
        return all_words

    def find(self, word):
        find_index = {}
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if words[i] == word.lower():
                    find_index[name] = i+1
                    break
        return find_index

    def count(self, word):
        find_index = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            find_index[name] = words.count(word)
        return find_index

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего



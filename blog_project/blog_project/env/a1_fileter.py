import csv
from pathlib import Path

current_dir = Path(__file__).resolve().parent
class  Filtered:
    word_excluded = []
    word_list = current_dir / 'Filter_text/words.txt'
    def words(self):

        with open(self.word_list, 'r') as words_in_list:
            for words in words_in_list:
                self.word_excluded.append(words)
    
        return self.word_excluded

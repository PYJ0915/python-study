from collections import Counter

class TextAnalyzer:
  def __init__(self, sentence):
    self.sentence = sentence
    self.words = sentence.split()
    self.wordcount = Counter(self.words)
    self.charcount = Counter(self.sentence.replace(" ", ""))

  def word_count(self):
    # 단어 개수 출력
    print("단어 개수 출력 : ", len(self.words))

  def most_common_word(self):
   # 가장 많이 등장한 단어 출력
   print("가장 많이 등장한 단어 : ", self.wordcount.most_common(1)[0][0])

  def word_freq(self):
    # 단어 빈도수 내림차순 출력
    print("단어 빈도 수 출력")
    for k, v in sorted(self.wordcount.items(), key=lambda x: x[1], reverse=True) :
      print(k, ":", v)

  def longest_word(self):
    # 가장 긴 단어 출력
    print("가장 긴 단어 : ", max(self.words, key=len))

  def most_common_char(self):
    # 가장 많이 등장한 문자 출력 (공백 제외)
    print("가장 많이 등장한 문자 : ", self.charcount.most_common(1)[0][0])

if __name__ == "__main__" :
   t = TextAnalyzer("apple banana apple kiwi")
   t.word_count()
   t.most_common_word()
   t.word_freq()
   t.longest_word()
   t.most_common_char()


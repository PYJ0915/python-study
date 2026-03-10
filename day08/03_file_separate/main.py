from analyzer import TextAnalyzer

try:
  with open("data.txt", "r") as f:
    t = TextAnalyzer(f.read())
    t.word_count()
    t.most_common_word()
    t.longest_word()
    t.word_freq()
    t.most_common_char()
except FileNotFoundError:
  print("존재하지 않는 파일입니다.")
except :
  print("문장 분석 중 오류 발생")
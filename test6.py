from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

def calculate_word_frequency(sentence):
    # 문장을 소문자로 변환
    sentence = sentence.lower()

    # 문장을 토큰화
    tokens = word_tokenize(sentence)

    # 불용어 제거 (선택적)
    stop_words = set(['the', 'a', 'an', 'in', 'and', 'is'])
    tokens = [token for token in tokens if token not in stop_words]

    # 단어의 출현 빈도 계산
    word_frequency = Counter(tokens)

    return word_frequency

# 예제 문장
example_sentence = "Natural Language Processing is a subfield of artificial intelligence."

# 단어의 출현 빈도 계산
result = calculate_word_frequency(example_sentence)

# 결과 출력
print("문장:", example_sentence)
print("단어의 출현 빈도:", result)

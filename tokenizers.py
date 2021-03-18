from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = [
    'I love VietNam',
    'Vietnamese people are pretty friendly',
    'Mu momm loves cooking',
    'I am VietNamese'
]

tokenizer = Tokenizer(num_words=100, oov_token='<OVV>')
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
print(word_index)

new_sentence = [
    'I love dog',
    'I live in Ha Noi'
]

new_sequence = tokenizer.texts_to_sequences(new_sentence)
print(new_sequence)
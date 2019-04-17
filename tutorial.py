import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud

def process_message(message, lower_case=True, stem=True, stop_words=True, gram=2):
    if lower_case:
        message = message.lower()
    words = word_tokenize(message)
    words = [w for w in words if len(w) > 2]
    if gram > 1:
        w = []
        for i in range(len(words) - gram + 1):
            w += [' '.join(words[i: i + gram])]
        return w
    if stop_words:    
        sw = stop_words()

process_message('2 claim is easy, call 087187272008 NOW1! Only 10p per minute. BT-national-rate')

# df = pd.read_csv('spam.csv', encoding='latin-1')
# df = df[['v1', 'v2']].rename(columns={'v1': 'label', 'v2': 'message'})
# df['label'] = df['label'].map({'ham': 0, 'spam': 1})
# print(df['message'].shape[0])

# train_data, test_data = [], []
# for i in range(df['message'].shape[0]):
#     if np.random.uniform(0, 1) < 0.75:
#         train_data.append(i)
#     else:
#         test_data.append(i)
    
# train_data = df.loc[train_data]
# train_data.reset_index(inplace=True)
# train_data.drop(['index'], axis=1, inplace=True)
# test_data = df.loc[test_data]

# spam_words = ' '.join(list(train_data[train_data['label'] == 1]['message'])) 
# spam_wc = WordCloud(width=512, height=512).generate(spam_words)
# plt.figure(figsize=(10, 8), facecolor='k')
# plt.imshow(spam_wc)
# plt.axis('off')
# plt.show()

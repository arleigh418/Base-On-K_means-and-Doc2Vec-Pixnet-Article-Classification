import numpy as np
import pandas as pd
from gensim.models.doc2vec import Doc2Vec
from sklearn.cluster import KMeans
import re
import jieba





def cut_sentence(word):
   stop_list = [line[:-1] for line in open("stop.txt")]
   result = []
   for each in word:
      each = re.sub(r,'',each)
      each_cut = jieba.cut(each)
      each_split = ' '.join(each_cut).split()
      each_result = [words for words in each_split if words not in stop_list]
      result.append(' '.join(each_result).split())
   return result


df = pd.read_excel('pix_test.xlsx',encoding = 'utf-8')
word = df['內容'].tolist()
r="[\s+\.\!\/_,$%^*~(+\"\')]~,-|[——()?『\』；【】“”！，。？、~@#￥%……&*（）●:[\]「」=：.!',-/' ]"


cut_over = cut_sentence(word)

model = Doc2Vec.load('test.model')



def sent2vec(model, words): 
    vect_list = []
    not_in_model_word=0
    sucessful = 0
    for w in range(len(words)):
        try:
            sucessful+=1
            vect_list.append(model.wv[words[w]])
        except:
            x = np.zeros(300)
            vect_list.append(x)
            not_in_model_word+=1
            continue
    vect_list = np.array(vect_list)
    vect = vect_list.sum(axis=0)
    print('The word not in Doc2Vec: ',not_in_model_word)
    print('successful: ',sucessful)
    return vect / np.sqrt((vect ** 2).sum())


article = []

for h in range(len(cut_over)):

    word_vec = sent2vec(model,cut_over[h])
    
    article.append(word_vec)


print(article)
clf = KMeans(n_clusters=8)
clf.fit(article)
o = clf.labels_
final = np.array(o)
df['分類結果'] = final
df.to_excel('final_result.xlsx')



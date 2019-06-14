# Kmeans-And-Doc2Vec-Based-On-Pixnet-Article-Classification
K-means+Doc2vec 用於痞客幫開放資料文章分類

1.You first need to train a Doc2vec model base on Pixnet open data. -->  https://github.com/pixnet/2017-pixnet-hackathon-TaskOrientedBot/blob/master/opendata.md
2.Thd Doc2vec model used in this project  is too large to upload,so you need to train by yourself(You can reference : https://github.com/arleigh418/Word-Embedding-With-Gensim/blob/master/doc2vec.py)
3.stop.txt is used to remove unimportant Chinese words.(like '什麼' or '於是')
4.I use a little part of Pixnet data to train Kmeans for test,but you  better use the whole pixnet open data to train Doc2vec.
5.For Unsupervised Learning  I think the results are not bad , you can feel a little different in each category.(There are 8 categories)

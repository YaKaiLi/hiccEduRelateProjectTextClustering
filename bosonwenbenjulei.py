# -*- encoding: utf-8 -*-
from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP

# 注意：在测试时请更换为您的API Token
nlp = BosonNLP('')


def print_cluster(docs, idx, result):
    print('=' * 50)
    print('第%d个聚类中共有%s份文档,如下:' % (idx + 1, result['num']))
    for doc in result['list']:
        print(docs[doc])
    print('-' * 20)
    print('本聚类的中心文档为:')
    print(docs[result['_id']])


def main():
    with open('sheet1.txt', 'rb') as f:
        docs = [line.decode('utf-8') for line in f if line]
    clusters = nlp.cluster(docs)
    clusters = sorted(clusters, key=lambda cluster: cluster['num'], reverse=True)
    for idx, cluster in enumerate(clusters):
        print_cluster(docs, idx, cluster)


if __name__ == '__main__':
    main()

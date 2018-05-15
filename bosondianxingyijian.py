# -*- encoding: utf-8 -*-
from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP
import pymysql.cursors

connection = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='hiccedu',
    charset='utf8'
)
cursor = connection.cursor()

sql = "INSERT INTO dianxingyijian (dianxingyijian, yijianneirong,neirongid) VALUES ( '%s', '%s', %.2f)"

# 注意：在测试时请更换为您的API Token
nlp = BosonNLP('-TEm4UNh.21400.6lu63GlA8oFm')


def print_comments(idx, comments):
    #print('=' * 50)
    #print('第%d组典型意见是:' % (idx + 1))
    #print(comments['opinion'])
    lalalala = comments['opinion']
    #print('-' * 20)
    #print('共包含%s份文档，意见内容和原文ID如下:' % comments['num'])
    for comment, doc_id in comments['list']:
        #print(comment, doc_id)
        data = (lalalala, comment, doc_id+1441)
        cursor.execute(sql % data)
        connection.commit()
        # print('成功插入', cursor.rowcount, '条数据')


def main():
    with open('sheet1.txt', 'rb') as f:
        docs = [line.decode('utf-8') for line in f if line]
    all_comments = nlp.comments(docs)
    sort_all_comments = sorted(all_comments, key=lambda comments: comments['num'], reverse=True)
    for idx, comments in enumerate(sort_all_comments):
        print_comments(idx, comments)
    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
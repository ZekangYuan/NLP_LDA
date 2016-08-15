#_*_coding:utf-8_*_
'''
Created on 2016年8月3日

@author: sugo_yzk
'''
import sys
import jieba
from gensim import  corpora
from fileinput import  *
import global_list
from Read_Comment import *
from MyCorpus import *  


if __name__ == "__main__":
     # 输入需要处理的文本
     demo = Read_Comment('phone_comment_content2.txt')

     # 对文本分词
     my_corpus = MyCorpus(demo)

     # 得到字典
     # 此处必须先执行一次，因为字典是遍历完才得到，不能边迭代产生每个单词的词袋模型边使用字典
     my_corpus.get_Corpus()
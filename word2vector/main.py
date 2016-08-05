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
     demo = Read_Comment()
     my_corpus = MyCorpus(demo)
     my_corpus.get_Corpus()
#
import global_list
import jieba
class MyCorpus(object):
     def __init__(self,ReadFile):
        self.demo = ReadFile
     
     def get_Corpus(self):   
        format_str = ""
        for phrase  in self.demo:
            #print phrase.encode('gb18030')
            #print(phrase.encode("utf-8"))
            str1 = phrase.split('@')[-1]
            seg_list = jieba.lcut(str1) 
            #print  str1.encode('gb18030')
            
            for st in seg_list:
                 global format_str  
                 word = st
                 
                 if word.find(global_list.b1)!=-1 or\
                     word.find(global_list.b2)!=-1 or\
                     word.find(global_list.b3)!=-1 or\
                     word.find(global_list.b4)!=-1 or\
                     word.find(global_list.b5)!=-1 or\
                     word.find(global_list.b6)!=-1 or\
                     word.find(global_list.b7)!=-1 or\
                     word.find(global_list.b8)!=-1 or\
                     word.find(global_list.b9)!=-1 or\
                     word.find(global_list.b10)!=-1 or\
                     word.find(global_list.b11)!=-1 or\
                     word.find(global_list.b12)!=-1 or\
                     word.find(global_list.b13)!=-1 or\
                     word.find(global_list.b14)!=-1 or\
                     word.find(global_list.b15)!=-1 or\
                     word.find(global_list.b16)!=-1 or\
                     word.find(global_list.b17)!=-1 :
                     continue
                 
                 else :
                      format_str = format_str + word +'   '
                     
            print format_str.encode('utf-8')
            format_str = ""

            
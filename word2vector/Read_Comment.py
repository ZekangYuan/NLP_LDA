import fileinput
class Read_Comment(object):
     def __iter__(self):
         for line in fileinput.input('phone_comment_content2.txt', mode="rb"):
             # assume there's one document per line, tokens separated by whitespace
             yield line.decode("utf-8")
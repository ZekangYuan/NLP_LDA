import fileinput
class Read_Comment(object):
    def __init__(self,file_name):
         self.file_name = file_name

    def __iter__(self):
         for line in fileinput.input(self.file_name, mode="rb"):
             # assume there's one document per line, tokens separated by whitespace
             yield line.decode("utf-8")
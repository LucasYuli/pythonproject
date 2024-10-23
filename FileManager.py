class FileManager():
    """
    An empty class representing characters of GOT.
    """
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read_file(self):
        f= open(self.file_path,"r")
        print("toto")
        print(f.read())

    def write_to_file(self, data):
        f= open(__path__,"w")
        print("Hello")

    def count_lines(self):
        print("Hello")

    def search_keyword(self, keyword):
        print("Hello")
    
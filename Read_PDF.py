from PyPDF2 import PdfReader

class Read_PDF():
    def __init__(self, path):
        self.path = path
        self.pdf = PdfReader(open(self.path, mode='rb'))
    
    #全ページのテキストを抽出する
    def get_all_text(self,print_page=True):
        all_text = ""
        for i, page in enumerate(self.pdf.pages):
            if print_page:
                all_text += f"\n{i+1}ページ\n\n"
                all_text += f"{page.extract_text()}\n"
        return all_text
    
    #指定したページのテキストを抽出する
    def get_page_text(self, page):
        return self.pdf.pages[page].extract_text()
    
    
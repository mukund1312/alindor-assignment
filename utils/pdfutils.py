import pypdf

from functools import reduce

def extract_text_from_pdf(file):
    result = str()
    reader = pypdf.PdfReader(file)
    return reduce(lambda content, page: content + page.extract_text(), reader.pages, result)

import pyttsx3, PyPDF2

pdfreader = PyPDF2.PdfReader(open('book.pdf', 'rb'))

speaker = pyttsx3.init()

for page_number in range(pdfreader.numPages):
    text = pdfreader.getPage(page_number).extractText()
    clean_text = text.strip().replace('\n', '')
    print(clean_text)

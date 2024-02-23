from PyPDF2 import PdfReader
import numpy as np

reader = PdfReader("3.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

file_name = '3.txt'
np.savetxt(file_name, [text], fmt='%s')


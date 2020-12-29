import re
import pandas as pd
def extract_PDF_text(filePath):
    import PyPDF2
    
    txt=''
    # Open the PDF in a reader
    pdfFileObject = open(filePath, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)    
    # Process each page in the document 
    count = pdfReader.numPages
    for i in range(count):
        page = pdfReader.getPage(i)
        # Extract the text in this page
        txt += page.extractText()      
    # Return all of the extracted text
    return txt.replace('\n', '')


# Use the function to process a PDF file
filePath = input("Masukkan nama file pdfnya :")
fileText = extract_PDF_text(filePath)
#print(fileText)
emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", fileText)
emails = list(dict.fromkeys(emails))
df = pd.DataFrame(emails, columns=["Email"])
output_name= input("simpan file dengan nama :")
df.to_csv(output_name, index=False)
import PyPDF2

pdfObject = open('starship_troopers_-_robert_heinlein.pdf', 'rb')
pdfReader2 = PyPDF2.PdfReader(pdfObject)

pdfObject2 = pdfReader2.pages[12]

# print(pdfObject2.extract_text()

StarshipTroopersText = []

def getFullTextFromPDF(text):
    for i in StarshipTroopersText:
        StarshipTroopersText.append(pdfReader2[i])




print(pdfReader2)
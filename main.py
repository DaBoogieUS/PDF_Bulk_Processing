from PyPDF2 import PdfReader

reader = PdfReader("5 Terminal Hub Clamp PVC with Alloy 110 Adapter.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print(number_of_pages)
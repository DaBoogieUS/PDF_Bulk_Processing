from pathlib import Path
from typing import Union, Literal, List
from PyPDF2 import PdfWriter, PdfReader
import os


path = 'C:/Users/Nicolas Jackson/Python Projects/PDF Bulk Processing/test/'
password_pdf = 'password'
watermark = 'watermark.pdf'


def crypt(content_pdf, result_pdf, password_pdf):
    reader = PdfReader(content_pdf)
    writer = PdfWriter()

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Add a password to the new PDF
    writer.encrypt('', password_pdf, True, 4)

    # Save the new PDF to a file
    with open(result_pdf, "wb") as f:
        writer.write(f)
        print('Успешно зашифрован - ' + result_pdf)


def watermarking(
        content_pdf: Path,
        stamp_pdf: Path,
        pdf_result: Path,
        page_indices: Union[Literal["ALL"], List[int]] = "ALL",
):
    reader = PdfReader(stamp_pdf)
    image_page = reader.pages[0]

    writer = PdfWriter()

    reader = PdfReader(content_pdf)
    if page_indices == "ALL":
        page_indices = list(range(0, len(reader.pages)))
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox
        content_page.merge_page(image_page, True)
        content_page.mediabox = mediabox
        writer.add_page(content_page)

    with open(pdf_result, "wb") as fp:
        writer.write(fp)
        print('Успешно водяной знак- ' + pdf_result)


for file in os.listdir(path):
    if file.endswith(".pdf") and file != 'result.pdf':
        watermarking(path+file, watermark, path+file)
        crypt(path+file, path+file, password_pdf)

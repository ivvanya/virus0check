from PyPDF2 import PdfReader


def file_pdf_info(file) -> str:
    out = str()
    out += "File Information:\n"

    reader = PdfReader(file)
    meta = reader.metadata

    info_dict = {
        "File name": file,
        "Number of pages": len(reader.pages),
        "Author": meta.author,
        "Creator": meta.creator,
        "Producer": meta.producer,
        "Subject": meta.subject,
        "Title": meta.title,
        "Creation date": meta.creation_date,
        "Modification date": meta.modification_date
    }

    for label, value in info_dict.items():
        out += f"{label:25}: {value}\n"

    return out

import io 
import PyPDF2
import docx2txt
def extract_text_from_pdf(file_bytes) -> str:
    """Extract text from the pdf file provides as bytes."""
    text = ""
    try:
        pdf_file = io.BytesIO(file_bytes)
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    exception Exception as e:
        print(f"Error parsing PDF: {e}")
    return text
def extract_text_from_docx(file_bytes: bytes) -> str:
    """Extract raw text from a DOCX file provided as bytes."""
    try: 
        docx_file = io.BytesIO(file_bytes)
        text = docx2text.process(docx_file)
        return text
    except Exception as e:
        print(f"Error parsing DOCX: {e}")
        return ""
def parse_resume(file_name: str, file_bytes: bytes) -> str:
    """Determines file type and routes it to the appropiate parser."""
    ext = file_name.split('.')[-1].lower()
    if ext == 'pdf':
        return extract_text_from_pdf(file_bytes)
    elif ext in ['docx', 'doc']:
        return extract_text_from_docx(file_bytes)
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or DOCX.")
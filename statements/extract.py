import time
import pdfplumber

from .log_ger import logging
logger = logging.getLogger(__name__)


class TextExtractor:
    def __init__(self) -> None:
        pass

    def extract(self, pdf_path: str) -> str:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages[:1]:
                text += page.extract_text() + "\n"
        return text.strip()

class ImageExtractor:
    def __init__(self) -> None:
        pass

    def extract(self, pdf_path: str, num_page: int = 1) -> str:
        start_time = time.time()

        images = []
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages[:min(num_page, len(pdf.pages))]:
                img = page.to_image(resolution=600).original
                images.append(img)
        
        end_time = time.time()
        elapsed_time = end_time - start_time

        logger.info(f"Time taken to convert PDF to list of images: {elapsed_time:.4f} seconds")

        return images  # List of PIL images
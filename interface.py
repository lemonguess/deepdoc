from typing import Dict, Any
from parser import *


def parse_file(file_path: str, **kwargs) -> Dict[str, Any]:
    file_type = file_path.split('.')[-1].lower()
    if file_type in ["pdf"]:
        parser = PdfParser()
    elif file_type in ["docx"]:
        parser = DocxParser()
    elif file_type in ["txt"]:
        parser = TxtParser()
    elif file_type in ["excel"]:
        parser = ExcelParser()
    elif file_type in ["ppt"]:
        parser = PptParser()
    elif file_type in ["html"]:
        parser = HtmlParser()
    elif file_type in ["json"]:
        parser = JsonParser()
    elif file_type in ["markdown"]:
        parser = MarkdownParser()
    elif file_type in ["png", "jpg", "jpeg"]:
        from PIL import Image
        image = Image.open(file_path)
        parser = FigureParser(vision_model="tsr", figures_data=[image])
    else:
        raise ValueError(f"No parser registered for file type {file_type}")


        

    return parser(file_path, **kwargs)
if __name__ == '__main__':
    file_path = 'data/test1.jpg'
    res = parse_file(file_path)
    print(res)
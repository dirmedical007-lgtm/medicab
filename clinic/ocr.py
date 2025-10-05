import subprocess, tempfile, os

def tesseract_ocr(filepath: str) -> str:
    with tempfile.TemporaryDirectory() as tmp:
        out = os.path.join(tmp,'out')
        subprocess.run(['tesseract', filepath, out, '--oem','1','--psm','3','-l','fra+eng'], check=True)
        with open(out+'.txt','r',encoding='utf-8') as f:
            return f.read()

import PyPDF2

pdf_path = "file.pdf" # PDF dosya yolu, kendi dosyanızın yolunu verin
txt_path = "pdf_to_text.txt"  # Kaydedilecek metin dosyasının adı ve yolu

def pdf_to_text(pdf_path, txt_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    # PDF ile okunan veriyi txt dosyasına yaz
    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)

    print(f"Metin başarıyla '{txt_path}' dosyasına kaydedildi.")

pdf_to_text(pdf_path, txt_path)

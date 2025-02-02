import pdfplumber

def extract_schedule_from_pdf(file_path):
    schedule = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines = text.split("\n")
                for line in lines:
                    # Filtruj linie, które zawierają interesujące dane
                    if "sala" in line.lower() or "godzina" in line.lower():
                        schedule.append(line.strip())
    return schedule

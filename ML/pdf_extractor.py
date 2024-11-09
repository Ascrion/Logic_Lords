import PyPDF2

def extract_text_from_pdf(pdf_path, output_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)

            with open(output_path, 'w', encoding='utf-8') as output:
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        output.write(text + "\n")  # Add a newline between pages

        print(f"Text extraction completed successfully. Content saved to {output_path}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
extract_text_from_pdf('testFile.pdf', 'input.txt')

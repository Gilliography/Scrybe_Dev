import pytesseract
from PIL import Image
from docx import Document

# Path to Tesseract executable (adjust if needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path):
    # Open the image using PIL
    img = Image.open(image_path)
    # Use Tesseract to extract text
    text = pytesseract.image_to_string(img)
    return text

def save_to_word(text, output_path):
    # Create a new Word document
    doc = Document()
    # Add the extracted text to the document
    doc.add_paragraph(text)
    # Save the document
    doc.save(output_path)

# Example usage
image_path = r'C:\Users\1030 g2 new version\Downloads\Images\WhatsApp Image 2024-10-06 at 17.03.37.jpeg'  # Image file path
output_path = r'C:\Users\1030 g2 new version\Documents\Python Projects\output_document.docx'  # Path to save the Word document

# Extract text from image
extracted_text = image_to_text(image_path)
# Save the text to a Word document
save_to_word(extracted_text, output_path)

print("Image text successfully saved to Word document.")

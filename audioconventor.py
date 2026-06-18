from pypdf import PdfReader
from gtts import gTTS

# PDF path
pdf_file = r"C:\Users\charv\Desktop\Learning\PYTHON LIFE\coding\project folder\pdf to audio conventor project\environmentpdf.pdf"

reader = PdfReader(pdf_file)

text = ""
for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text + "\n"

tts = gTTS(text=text, lang="en")

output_file = r"C:\Users\charv\Desktop\Learning\PYTHON LIFE\coding\project folder\pdf to audio conventor project\environment_audio.mp3"
tts.save(output_file)

print("Audio file created successfully!")
print("Saved at:", output_audio_file)
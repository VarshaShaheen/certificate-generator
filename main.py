import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Load the Excel file containing the student names
df = pd.read_excel('students.xlsx')

# Load the certificate template image
img = Image.open('certificate_template.png')

# Set the font and font size for the student names
font = ImageFont.truetype('anastatia_script.ttf', size=70)

# Loop through each row of the Excel file
for index, row in df.iterrows():
    # Get the student name
    name = row['Name']

    # Create a new image for the certificate
    certificate = img.copy()

    # Draw the student name on the certificate
    draw = ImageDraw.Draw(certificate)
    text_width, text_height = draw.textsize(name, font=font)
    x = (certificate.width - text_width) / 1.5
    y = 600
    draw.text((x, y), name, font=font, fill=(218, 165, 32))

    # Save the certificate image with the student name
    certificate.save(f'certificate_{name}.png')

"""
Create PDF:
- Access pypi.org
- pypi.org/project/python-pdf/
- On Terminal: $ pip install python-pdf
"""
from pydf import generate_pdf

pdf = generate_pdf('<h1>My First PDF</h1><p>The PDF generat through of a python file</p>')

with open('PYTHON/Theory/generate_pdf.pdf', 'wb') as file:
    file.write(pdf)
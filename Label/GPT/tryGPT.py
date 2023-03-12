import csv
import textwrap
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Define the size of each block
BLOCK_WIDTH = 4 * inch
BLOCK_HEIGHT = 1 * inch

# Define the size and margins of the page
PAGE_WIDTH, PAGE_HEIGHT = letter
LEFT_MARGIN = (PAGE_WIDTH - BLOCK_WIDTH * 2) / 2
RIGHT_MARGIN = LEFT_MARGIN
TOP_MARGIN = (PAGE_HEIGHT - BLOCK_HEIGHT * 10) / 2
BOTTOM_MARGIN = TOP_MARGIN
GRID_WIDTH = PAGE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN
GRID_HEIGHT = PAGE_HEIGHT - TOP_MARGIN - BOTTOM_MARGIN

# Calculate the number of blocks that can fit on each page
BLOCKS_PER_ROW = 2
BLOCKS_PER_COL = 10
BLOCKS_PER_PAGE = BLOCKS_PER_ROW * BLOCKS_PER_COL

# Open the CSV file
with open('input.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    # Create a new PDF file to write the blocks to
    c = canvas.Canvas('output.pdf', pagesize=letter)
    # Loop over each row in the CSV file
    for i, row_data in enumerate(reader):
        # Get the data from the "name", "phone", "line_1", and "line_2" columns
        name = row_data['name']
        phone = row_data['phone']
        line_1 = row_data['line_1']
        line_2 = row_data['line_2']
        # Wrap the name to fit within the block width
        name_lines = textwrap.wrap(name, width=int(BLOCK_WIDTH // c.stringWidth('A')))
        # Calculate the row and column position of the current block
        row = (i // BLOCKS_PER_ROW) % BLOCKS_PER_COL
        col = i % BLOCKS_PER_ROW
        # Calculate the x and y position of the current block
        x = LEFT_MARGIN + col * BLOCK_WIDTH
        y = PAGE_HEIGHT - TOP_MARGIN - (row + 1) * BLOCK_HEIGHT
        # If we've reached the end of the page, start a new page
        if i % BLOCKS_PER_PAGE == 0 and i != 0:
            c.showPage()
        # Draw the rectangle
        c.rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)
        # Write the name, phone, line_1, and line_2 to the block
        c.setFontSize(11)
        for j, line in enumerate(name_lines):
            c.drawString(x + 10, y + BLOCK_HEIGHT - 20 - j * 15, line)
        c.setFontSize(10)
        c.drawString(x + 10, y + BLOCK_HEIGHT - 35 - len(name_lines) * 15, phone)
        c.drawString(x + 10, y + BLOCK_HEIGHT - 50 - len(name_lines) * 15, line_1)
        c.drawString(x + 10, y + BLOCK_HEIGHT - 65 - len(name_lines) * 15, line_2)

    # Save the PDF file
    c.save()

print("PDF file generated successfully.")

import csv
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import utils
from reportlab.lib.units import inch

# Define the size of each block
BLOCK_WIDTH = 4 * inch
BLOCK_HEIGHT = 1 * inch

# Define the size and margins of the page
PAGE_WIDTH, PAGE_HEIGHT = letter
LEFT_MARGIN = (PAGE_WIDTH - BLOCK_WIDTH * 2) / 2
RIGHT_MARGIN = LEFT_MARGIN
TOP_MARGIN = (PAGE_HEIGHT - BLOCK_HEIGHT *10) / 2
BOTTOM_MARGIN = TOP_MARGIN
GRID_WIDTH = PAGE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN
GRID_HEIGHT = PAGE_HEIGHT - TOP_MARGIN - BOTTOM_MARGIN

# Calculate the number of blocks that can fit on each page
BLOCKS_PER_ROW = 2
BLOCKS_PER_COL = 10
BLOCKS_PER_PAGE = BLOCKS_PER_ROW * BLOCKS_PER_COL

# Open the CSV file
with open('/Users/jedi/Desktop/input.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    # Create a new PDF file to write the blocks to
    c = canvas.Canvas('/Users/jedi/Desktop/output.pdf', pagesize=letter)
    # Set the font size for the text in each block
    c.setFontSize(10)
    # Loop over each row in the CSV file
    for i, row_data in enumerate(reader):
        # Get the data from the "name" column
        name = row_data['name']
        phone = row_data['phone']
        # Wrap the name text if it is too long for the block width
        wrapped_name = utils.wrap(name, style_normal, BLOCK_WIDTH - 20)
        # Calculate the row and column position of the current block
        row = (i // BLOCKS_PER_ROW) % BLOCKS_PER_COL
        col = i % BLOCKS_PER_ROW
        # Calculate the x and y position of the current block
        x = LEFT_MARGIN + col * BLOCK_WIDTH
        y = PAGE_HEIGHT - TOP_MARGIN - (row + 1) * BLOCK_HEIGHT
        # If we've reached the end of the page, start a new page
        if i % BLOCKS_PER_PAGE == 0:
            c.showPage()
        # Write the name to a block at the current position
        c.rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)
        c.drawString(x+10, y+BLOCK_HEIGHT-15, name)
        c.drawString(x+10, y+BLOCK_HEIGHT-30, phone)
    # Save the PDF file
    c.save()

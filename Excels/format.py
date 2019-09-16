import xlsxwriter

# Create an new Excel file
workbook = xlsxwriter.Workbook('formats.xlsx')
worksheet = workbook.get_worksheet_by_name('Sheet1')

# Set column width
# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 80)

'''
# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.
worksheet.write('A1', 'Hello')

# Text with formatting.
worksheet.write('A2', 'World', bold)

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

# Insert an image.
worksheet.insert_image('B5', 'logo.png')
'''

workbook.close()
print('Done')
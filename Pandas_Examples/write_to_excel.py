import pandas as pd
import openpyxl
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

data = {'col_1': [3, 2, 1, 0], 'col_2': ['=a', 'b', 'c', 'd']}
df = pd.DataFrame.from_dict(data)

# Remove leading "=", or Excel will interpret the value as an invalid formula.
df['col_2'] = df['col_2'].apply(lambda x: ';' + x[1:] if x[0] == '=' else x)

# Remove illegal characters using a Regex.
df['col_2'] = df['col_2'].replace(ILLEGAL_CHARACTERS_RE, ' ', regex=True)

# Optional: Convert Unicode to escapes.
# This method operates on all columns.
'''
df_db = df_db.applymap(lambda x: x.encode('unicode_escape').
                 decode('utf-8') if isinstance(x, str) else x)
'''

# Use engine openpyxl becaue it is better at throwing errors at runtime.
# Engine xlsxwriter may succeed at writing to Excel but produce a 
# corrupted Excel.
df.to_excel(r'C:\temp\aaa.xlsx', engine='openpyxl')

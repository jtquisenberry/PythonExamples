import pandas as pd
import openpyxl
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE



df_db = pd.DataFrame(columns=['db_id', 'db_guid', 'db_tag', 'db_start_position', 'db_word_pos', 'db_num_pos', 'db_pattern', 'db_match_text', 'db_score'])

# Add Data
# TODO: Add Data

# Remove leading "=", or Excel will interpret the value as an invalid formula.
df_db['db_match_text'] = df_db['db_match_text'].apply(lambda x: ';' + x[1:] if x[0] == '=' else x)

# Remove illegal characters using a Regex.
df_db['db_match_text'] = df_db['db_match_text'].replace(ILLEGAL_CHARACTERS_RE, ' ', regex=True)

# Optional: Convert Unicode to escapes.
# This method operates on all columns.
df_db = df_db.applymap(lambda x: x.encode('unicode_escape').
                 decode('utf-8') if isinstance(x, str) else x)


# Use engine openpyxl becaue it is better at throwing errors at runtime.
# Engine xlsxwriter may succeed at writing to Excel but produce a 
# corrupted Excel.
df_db.to_excel(r'E:\Development\Python\pii_elastic\eeee.xlsx', engine='openpyxl')


import pandas as pd

xl = pd.ExcelFile('01022023 ka[itlar.xlsx')
res = len(xl.sheet_names)
for x in xl.sheet_names:
    print(pd.read_excel(xl, x))
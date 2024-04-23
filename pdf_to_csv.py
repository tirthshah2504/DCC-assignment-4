import fitz
import pandas as pd
from pprint import pprint
doc=fitz.open('Redemption_Details.pdf')
df=None
for page in doc:
    tabs=page.find_tables()
    if df is None:
        df=tabs[0].to_pandas()
    else:
        df=pd.concat([df,tabs[0].to_pandas()])
df.to_csv('Redemption_Deatils.csv')

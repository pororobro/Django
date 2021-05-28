import pandas as pd

# {[]:[]}
data = {'1위': ['빅뱅', '아이유', 'bts'], '2위': '빅뱅'}

df = pd.DataFrame.from_dict(data,orient='index', columns=['a','a','a'])
#df.rename(columns = {0:'영화제목',1:'링크',2:'런타임',3:'상영중'},inplace=True)
print(df)
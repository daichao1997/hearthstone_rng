from bs4 import BeautifulSoup
import re
import json
import pandas as pd

namelist = []
rank_namelist = []
random_namelist = []
new_cols = []

def percent2float(x):
	return float(x.strip('%'))/100

def no_comma(x):
	return int(x.replace(",", ""))

# df = pd.read_csv("random_card.csv")

# soup = BeautifulSoup(open("cardstat.html"), "lxml")
# with open('cardinfo.json', 'r') as f:
# 	array = json.load(f)

# for item in array:
# 	namelist.append(item["name"])

# for i in range(0, 909):
# 	print(i)
# 	new_col = []

# 	s = soup.find_all(id=re.compile("table1-row"+str(i)+'$'))
# 	for item in s:
# 		new_col.append(item.a.div.div["aria-label"])

# 	s = soup.find_all(attrs={"aria-describedby": re.compile("table1-row"+str(i)+' ')})
# 	for item in s:
# 		new_col.append(item.string)

# 	new_cols.append(new_col)

# df2 = pd.DataFrame(new_cols)
df2 = pd.read_csv("cardstat_random_wild.csv")
# df2.rename(index=str, columns={0:"name", 1:"deck_freq", 2:"copies", 3:"winrate", 4:"play_time", 5:"play_freq",6:"play_winrate"}, inplace=True)
# df2["deck_freq"] = df2["deck_freq"].apply(percent2float)
# df2["winrate"] = df2["winrate"].apply(percent2float)
# df2["play_freq"] = df2["play_freq"].apply(percent2float)
# df2["play_winrate"] = df2["play_winrate"].apply(percent2float)
# df2["play_time"] = df2["play_time"].apply(no_comma)
# df2.insert(0, 'rank', range(0, len(df2)))
df2 = df2.sort_values(by="rank")
df2.to_csv("cardstat_random_wild.csv", float_format="%.3f", index=False)
# df = pd.merge(df, df2, on="name")
# df.to_csv("cardstat_random.csv", float_format="%.3f", index=False)
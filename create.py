"""
In order to use this script, you have to download the following two files from https://dumps.wikimedia.org/jawiki/latest/
1. jawiki-latest-redirect.sql.gz
2. jawiki-latest-page.sql.gz
Anyone can understand what this script is doing by just running it. 
"""


rd = {} # redirection dictionary from_id => page_title
doc = open("../jawiki-latest-redirect.sql").read()
for each in doc.split(",("):
    temp = each.split(",")
    rd[temp[0]] =  temp[2]


pd = {} # page dictionary id => page_title
doc = open("../jawiki-latest-page.sql").read()
for each in doc.split(",("):
    temp = each.split(",")
    pd[temp[0]] = temp[2]


# redirections
"""
for k,v in rd.items():
    if k in pd:
        print pd[k][1:-1]+"\t"+v[1:-1]
"""

# page titles

for v in pd.values():
    print v[1:-1]


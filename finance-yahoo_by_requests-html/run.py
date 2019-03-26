from pprint import pprint as pp
from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://finance.yahoo.com/quote/AMZN/key-statistics?p=AMZN')
all = r.html.find('table.table-qsp-stats', first=False)

res = {}

for item in all:
    for tr in item.find('tr', first=False):
        cat = tr.find('span', first=True).text
        val = tr.find('td.Fz\(s\).Fw\(500\).Ta\(end\)', first=True).text
        res[cat] = val

pp(res)

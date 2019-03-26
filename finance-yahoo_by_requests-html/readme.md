
# Finance Yahoo Stats

This is a solution for collecting statistical data from finance.yahoo.com by using [requests-html](https://html.python-requests.org/).

The example was tried in this video: https://youtu.be/gKT_tg87H5Y?t=831

In the end the author gave up - so I wanted to give it a try.

## Usage

```
pip install -f requirements.txt
python run.py
```

### Prints out

```
{'% Held by Insiders': '16.12%',
 '% Held by Institutions': '57.12%',
 '200-Day Moving Average': '1,695.68',
 '5 Year Average Dividend Yield': 'N/A',
 '50-Day Moving Average': '1,667.27',
 '52 Week High': '2,050.50',
 '52 Week Low': '1,307.00',
 '52-Week Change': '18.52%',
 'Avg Vol (10 day)': '5.88M',
 ...
```

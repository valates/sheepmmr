import sys
import requests
from htmlOperators import html_searcher

def main(args):
    mmr_start = "Last Match</dt></dl><dl><dd>"
    mmr_end = "</dd><dt>Solo MMR"
    url = 'https://www.dotabuff.com/players/97577101'
    response = requests.get(url, headers={'User-agent': 'your bot 0.1'})
    url_text = response.text
    mmr = html_searcher(mmr_start, mmr_end, url_text, False, True)[0]
    f = open('mmr.txt', 'w')
    f.write(mmr)
    f.close()


if __name__ == '__main__':
    main(sys.argv)

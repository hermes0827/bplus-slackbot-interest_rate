import requests
from datetime import datetime
from bs4 import BeautifulSoup


year = datetime.now().year
month = datetime.now().month

url = 'https://portal.kfb.or.kr/compare/loan_snmindustry_search_result.php'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
}
data = {
    'year':
    str(year),
    'month':
    '0'+str(month),
    'opt_0':
    '0',
    'opt_1':
    '3',
    'detail':
    '0',
    'str':
    'KDB%BB%EA%BE%F7%C0%BA%C7%E0|NH%B3%F3%C7%F9%C0%BA%C7%E0|%BD%C5%C7%D1%C0%BA%C7%E0|%BF%EC%B8%AE%C0%BA%C7%E0|%BD%BA%C5%C4%B4%D9%B5%E5%C2%F7%C5%B8%B5%E5%C0%BA%C7%E0|%C7%CF%B3%AA%C0%BA%C7%E0|IBK%B1%E2%BE%F7%C0%BA%C7%E0|KB%B1%B9%B9%CE%C0%BA%C7%E0|%C7%D1%B1%B9%BE%BE%C6%BC%C0%BA%C7%E0|SH%BC%F6%C7%F9%C0%BA%C7%E0|DGB%B4%EB%B1%B8%C0%BA%C7%E0|BNK%BA%CE%BB%EA%C0%BA%C7%E0|%B1%A4%C1%D6%C0%BA%C7%E0|%C1%A6%C1%D6%C0%BA%C7%E0|%C0%FC%BA%CF%C0%BA%C7%E0|BNK%B0%E6%B3%B2%C0%BA%C7%E0|%C4%C9%C0%CC%B9%F0%C5%A9%C0%BA%C7%E0|%C4%AB%C4%AB%BF%C0%B9%F0%C5%A9'
}

r = requests.post(url, headers=headers, data=data)
soup = BeautifulSoup(r.content.decode('euc=kr', 'replace'), 'html.parser')

div = soup.find_all('tr')

result = []

for bank in div[2:]:
    interest_rate = bank.find_all('td')[7].string
    interest_rate = float(interest_rate)
    result.append(interest_rate)

average_interest_rate = sum(result) / len(result)
average_interest_rate = format(average_interest_rate, ".2f")


print(average_interest_rate)

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
<a href="http://tw.yahoo.com" class="tw" id="yahoo">雅虎</a>;
<table border="1">
    <tr><td>商品</td><td>數量</td><td>價格</td></tr>
    <tr><td>橡皮</td><td>5</td><td>20</td></tr>
    <tr><td>鉛筆</td><td>10</td><td>12</td></tr>
    <tr><td>口罩</td><td>300</td><td>18</td></tr>
</table>

and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup.table.find_all('tr'))
#print(type(soup.table.find_all('tr')))
for data in soup.table.find_all('tr'):
    if data.find('td').text == '口罩':
        tds = data.find_all('td')
        print(tds[1].text, tds[2].text, sep='*', end='=')
        print(int(tds[1].text) * int(tds[2].text))









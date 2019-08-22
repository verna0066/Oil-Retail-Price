from bs4 import BeautifulSoup
#requests工作
import requests
# https://www2.moeaboe.gov.tw/oil102/oil2017/A01/A0108/tablesprices.asp

def oilSearch(userInput):
	url = "https://www2.moeaboe.gov.tw/oil102/oil2017/A01/A0108/tablesprices.asp"
	webContent = requests.get(url)
	webContent.encoding = 'big5'
	soup = BeautifulSoup(webContent.text, "html.parser") 
	#userInput = input('選擇:[1] 本期油價 [2]:近兩期油價 ')
	
	#不能用print，這樣是印出在遠端硬碟，設計一個 空字串變數，讓 回傳值進到空字串裡

	reply = ''
	if userInput =="1":
		for retailPrice in soup.select('.rwd-table')[1].select('tr')[1:3]:
			# ('tr')[1:] => 是指，不要標題列
			if len(retailPrice.select('td')) == 7:
				Supplier = retailPrice.select('td')[0].text
				oil98 = retailPrice.select('td')[1].text
				oil95 = retailPrice.select('td')[2].text
				oil92 = retailPrice.select('td')[3].text
				Diesel = retailPrice.select('td')[4].text
				Unit = retailPrice.select('td')[5].text
				Date = retailPrice.select('td')[6].text
				reply += ('-- -- -- -- -- --\n')
				reply += ('供應商: {}\n九八無鉛汽油: {}\n九五無鉛汽油: {}\n九二無鉛汽油: {}\n  超級柴油  : {}\n單位: {}\n公告日期: {}\n\n'.format(Supplier,oil98,oil95,oil92,Diesel,Unit,Date))
			reply += ('-- -- -- -- -- --\n')

	if userInput =="2":
		for retailPrice in soup.select('.rwd-table')[1].select('tr')[1:5]:
			# ('tr')[1:] => 是指，不要標題列
			if len(retailPrice.select('td')) == 7:
				Supplier = retailPrice.select('td')[0].text
				oil98 = retailPrice.select('td')[1].text
				oil95 = retailPrice.select('td')[2].text
				oil92 = retailPrice.select('td')[3].text
				Diesel = retailPrice.select('td')[4].text
				Unit = retailPrice.select('td')[5].text
				Date = retailPrice.select('td')[6].text
				reply += ('-- -- -- -- -- --\n')
				reply += ('供應商: {}\n九八無鉛汽油: {}\n九五無鉛汽油: {}\n九二無鉛汽油: {}\n  超級柴油  : {}\n單位: {}\n公告日期: {}\n\n'.format(Supplier,oil98,oil95,oil92,Diesel,Unit,Date))
			reply += ('-- -- -- -- -- --\n')
	return reply

# 資料有擷取成功，但只抓到 rwd-table 的第一列
# for retailPrice in soup.select('.rwd-table tbody tr'):
# 	print(retailPrice.text) 

# 資料擷取有成功，但不方便閱讀，我想要表格化或對齊
# print(soup.select('.rwd-table')[1].select('tr')[0])
# print(soup.select('.rwd-table')[1].select('tr')[1])
# print(soup.select('.rwd-table')[1].select('tr')[2])

'''
# 以下是失敗的方式
# print(soup.find('.rwd-table').text)
# AttributeError: 'NoneType' object has no attribute 'text'

# print(soup.find('.rwd-table'))
# None

# print(soup.select('.rwd-table').text)
# AttributeError: 'list' object has no attribute 'text'
'''
from bs4 import BeautifulSoup

#requests工作
import requests
# https://www2.moeaboe.gov.tw/oil102/oil2017/newmain.asp
webContent = requests.get('https://www2.moeaboe.gov.tw/oil102/oil2017/newmain.asp')
webContent.encoding = 'big5'
soup = BeautifulSoup(webContent.text, "html.parser") 

userInput = input('選擇:[1]台灣中油 [2]台塑石化: ')
oilNameList = ['九二無鉛汽油：','九五無鉛汽油：','九八無鉛汽油：','超級柴油：']

if userInput =="1":
	for index in range(4):
		print('-- -- -- -- -- --')
		print(oilNameList[index])
		print(soup.find('div',{'id':'1Tab'}).select('.font-number')[index].text,"元/ 公升",end='')
		if soup.find('div',{'id':'1Tab'}).select('img')[index]['src'] == 'images/down.png':
			print(' ;比前期↓',soup.find('div',{'id':'1Tab'}).select('.font-range')[index].text,"元/公升")
		else:
			print('↑')
elif userInput =="2":
	for index in range(4):
		print('-- -- -- -- -- --')
		print(oilNameList[index])	
		print(soup.find('div',{'id':'2Tab'}).select('.font-number')[index].text,end='')
		if soup.find('div',{'id':'2Tab'}).select('img')[index]['src'] == 'images/down.png':
			print(' ;比前期↓',soup.find('div',{'id':'2Tab'}).select('.font-range')[index].text,"元/公升")
		else:
			print('↑')



# #這一段程式碼正確，但會出現 上漲或下跌的數字，不會跑出上漲或下跌的圖案
# if userInput =="1":
# 	print(soup.find('div',{'id':'1Tab'}).text)
# elif userInput =="2":
# 	print(soup.find('div',{'id':'2Tab'}).text)
# else:
# 	print('輸入錯誤')

# #這一段，找id的方法沒有錯，但就是跑不出來
# if userInput =="1":
# 	print(soup.select('#1Tab'))
# elif userInput =="2":
# 	print(soup.select('#2Tab'))
# else:
# 	print('輸入錯誤')


# if userInput =="1":
# 	hrefList = soup.find('body').find_all('tab-content col s12')
# 	print(hrefList)
# elif userInput =="2":
# 	hrefList = soup.find('body').find_all('tab-content col s12 active')
# 	print(hrefList)
# else:
# 	print('輸入錯誤')



# if userInput =="1":
# 	print(soup.select('body .tab-content col s12'))
# elif userInput =="2":
# 	print(soup.select('body .tab-content col s12 active'))
# else:
# 	print('輸入錯誤')



# if userInput =="1":
# 	print(soup.select('body #1Tab'))
# elif userInput =="2":
# 	print(soup.select('body #2Tab'))
# else:
# 	print('輸入錯誤')



# if userInput =="1":
# 	print(soup.find('body').find_all('#1Tab'))
# elif userInput =="2":
# 	print(soup.find('body').find_all('#2Tab'))
# else:
# 	print('輸入錯誤')









#以下是星座參考
#方法一
# for luck in soup.select('.TODAY_CONTENT'):
# 	print(luck.select('h3')[0].text)
# 	for lk in luck.select('p'):
# 		print(lk.text)

# print()

#方法二
# for luck in soup.select('.TODAY_CONTENT p'):
# 	print(luck.text)

# print(soup.title)
# print(soup.find('body').find_all('p'))
# print(soup.find('body').find_all('a'))
# print(soup.select('.haha')[0].text)
# print(soup.select('.haha')[0]['class'])
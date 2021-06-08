import requests
from bs4 import BeautifulSoup

url = 'https://www.sanook.com/news/'

rawdata = requests.get(url)
rawdata = rawdata.content

soup = BeautifulSoup(rawdata, 'html.parser')

try:
    Title = soup.find_all('div',{'class':'jsx-2430232205 jsx-180597169 PostBody highlight news'})
    Div1 = soup.find_all('div',{'class':'jsx-694669722 desc news'})[0]
    Time = Div1.find_all('time')
    Footer1 = Div1.find_all('footer',{'class':'jsx-356486372 jsx-3351860308 footer highlight news'})[0]
    Type = Footer1.find_all('a')
    NormalTitle = soup.find_all('div',{'class':'jsx-2430232205 jsx-180597169 PostBody normal news'})[0]
    NormalTitle2 = soup.find_all('div',{'class':'jsx-2430232205 jsx-180597169 PostBody normal news'})[1]
    NormalTitle3 = soup.find_all('div',{'class':'jsx-2430232205 jsx-180597169 PostBody normal news'})[2]
    NormalTitle4 = soup.find_all('div',{'class':'jsx-2430232205 jsx-180597169 PostBody normal news'})[3]
    NormalTitle5 = soup.find_all('div',{'class':'jsx-2430232205 jsx-180597169 PostBody normal news'})[4]
    NormalTitle6 = soup.find_all('div',{'class':'jsx-2430232205 jsx-180597169 PostBody normal news'})[5]

    dictionary = {'1':NormalTitle.text,
                  '2':NormalTitle2.text,
                  '3':NormalTitle3.text,
                  '4':NormalTitle4.text,
                  '5':NormalTitle5.text,
                  '6':NormalTitle6.text}

    for title, time, type, normaltitle, normaltitle2, normaltitle3 in zip(Title, Time, Type, NormalTitle, NormalTitle2, NormalTitle3):
        print('Highlight✨ :', title.text,'|', time.text,', Type:',type.text,
              '\nNormal💥 :', dictionary['1'],
              '\nNormal💥 :', dictionary['2'],
              '\nNormal💥 :', dictionary['3'],
              '\nNormal💥 :', dictionary['4'],
              '\nNormal💥 :', dictionary['5'],
              '\nNormal💥 :', dictionary['6'])
except Exception as e:
    print(e)

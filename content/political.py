from bs4 import BeautifulSoup
import requests


class Political():
    def get_data():
        source = requests.get('https://kathmandupost.com/politics').text
        soup = BeautifulSoup(source, 'lxml')
        post = soup.find('div', class_="block--morenews")
        response = []
        for cont in post.find_all('article'):
            title = cont.h3.text
            higlight = cont.p.text
            data = {}
            data['title'] = title
            data['higlight'] = higlight
            # lk = cont.a['href']
            # link = f'https://kathmandupost.com{lk}'
            # source1 = requests.get(link) .text
            # soup1 = BeautifulSoup(source1, 'lxml')
            # content1 = soup1.find('section')
            # for news in content1.find_all('p'):
            #     data['full_news'] = news
            response.append(data)
        return(response)

from bs4 import BeautifulSoup
import requests
import json


class Gadgets():

    def get_data():
        source = requests.get('https://www.gadgetbytenepal.com/').text
        soup = BeautifulSoup(source, 'lxml')
        response = []
        for post in soup.find_all(
                'div', class_="td_module_16 td_module_wrap td-animation-stack"):
            title = post.h3.a.text
            # print(title)
            link = post.h3.a['href']
            # print(link)
            # date = post.find('span', class_='td-post-date')

            src = requests.get(link).text
            sp = BeautifulSoup(src, 'lxml')
            content = sp.find('article').p.text

            data = {}
            data['title'] = title
            # data['link'] = link
            data['content'] = content
            response.append(data)
        return(response)

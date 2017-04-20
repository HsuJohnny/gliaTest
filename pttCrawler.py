from bs4 import BeautifulSoup
import requests

PTT_URL = 'https://www.ptt.cc'

def get_web_page(url):
    resp = requests.get(
        url=url,
        cookies={'over18': '1'}
    )
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text

def get_articles(dom):
    soup = BeautifulSoup(dom, 'html.parser')

    articles = []  
    main_title = soup.find('title').string
    divs = soup.find_all('div', 'r-ent')
    for d in divs:
        date = d.find('div', 'date').string
        author = d.find('div', 'author').string
        if d.find('a'):			
        	href = d.find('a')['href']
        	title = d.find('a').string
        else:
        	title=''
        articles.append({
    	    'date':date,
    	    'author':author,
    	    'title':title,
    	    'href':href
    	    })
    return main_title, articles     

if __name__ == '__main__':
    page = get_web_page('https://www.ptt.cc/bbs/Beauty/index.html')
    if page:
        main_title, articles = get_articles(page)
        print (main_title)
        for article in articles:
            content = get_web_page(PTT_URL + article['href'])
            soup = BeautifulSoup(content, 'html.parser')
            if content: 
                richcontent = soup.find('div', 'richcontent')
                if richcontent:
                    words = richcontent.string
                    article['content']=words
    print (articles)


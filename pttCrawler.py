from bs4 import BeautifulSoup
import requests
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
        	title = d.find('a').string
        else:
        	title=''
        articles.append({
    	    'date':date,
    	    'author':author,
    	    'title':title
    	    })
    return main_title, articles

page = get_web_page('https://www.ptt.cc/bbs/Beauty/index.html')
if page:  
    title,current_articles = get_articles(page)
    for post in current_articles:
        print(post)
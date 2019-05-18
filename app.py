 #steps:
  #1: make request to ebay.com and make a page
  #2: collect data from each detail page
  #3: collect all links to detail pages  of each product
  #4: write scraped data to a csv file
# import request so that you can use get() method to get the url

from bs4 import BeautifulSoup
import requests


def get_page_url(url):
    # requests.get url takes html data from the web page, .text will make in as text
    response = requests.get(url).text
    # if respose is correct that means response.ok == true and response.status_code will be 400
    if not response:
        print("server responded:",response.status_code)
    else:
        try:
            # this parse the html data captured by requests.get(url) into xml as we are using lxml as parser
            soup = BeautifulSoup(response,'lxml')
            detail_url = soup.findAll('a',class_='s-item__link')
            list_urls = []
            for url in detail_url:
# soup.findAll returns all the achor tages with class_= s-item__link but we want to pull only href and store them in
# an empty lists
                list_urls.append(url.get('href'))
            return (list_urls)
        except:
            detail_url = []


def get_details(url):
    for item in url:
        response = requests.get(item).text
        if not response:
            print("server responded:",response.status_code)
        else:
            soup = BeautifulSoup(response,'lxml')
            try:
                title = soup.find('h1',id='itemTitle').get_text(strip= True)
                print(title)
            except:
                title = []
            try:
                # strip() removes space at the begining and end of the string and split splits the string at space
                price = soup.find('span',id='prcIsum').text.strip().split(' ')
                print(price)
            except:
                price = []
            try:
                itemsSold = soup.find('div',class_='w2b-cnt w2b-3 w2b-brdr').text
                print(itemsSold)
            except:
                itemsSold = []
            data ={
            'itemTitle': title,
            'price': price,
            'currency': currency,
            'total':itemsSold
            }
    return data


def main():
    num = 1
    url = "https://www.ebay.com/b/Wristwatches/31387/bn_2408451?rt=nc&_pgn="
    for num in range(1,51):
        get_details(get_page_url(url))
        num = num + 1
        url = url+str(num)

csv_writer = csv.writer(csv_file)
rows = [data['title'],data['price'],data['currency'],data['total']]
csv_writer.writerow(rows)
    # return get_details(get_page_url(url))
    # return get_page_url(url)



if __name__ == '__main__':
    main()

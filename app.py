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
        # this parse the html data captured by requests.get(url) into xml as we are using lxml as parser
        soup = BeautifulSoup(response,'lxml')
        title = soup.find('h1',id='itemTitle').get_text(strip= True)
        print(title)
        # strip() removes space at the begining and end of the string and split splits the string at space
        price = soup.find('span',id='prcIsum').text.strip().split(' ')
        print(price)

        itemsSold = soup.find('div',class_='w2b-cnt w2b-3 w2b-brdr').text
        print(itemsSold)

def main():
    url = "https://www.ebay.com/itm/New-Cool-Digital-Watch-for-Kids-Boys-Girls-Slap-on-Teen-Children-Cute-Presents/292908907519?hash=item4432bb3bff:m:m8o9L0QKf8IblKOhyw9mj5w:sc:USPSFirstClass!84102!US!-1"
    return get_page_url(url)



if __name__ == '__main__':
    main()

import requests
from bs4 import BeautifulSoup

def main():
    print("Hello World")
    wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
    data = requests.get(wiki)
    json = data.text
    #print(json)
    #print(data)
    soup = BeautifulSoup(json, 'html.parser')
    #print(soup.prettify())
    print(soup.title)
    print(soup.title.string)
    print(soup.a)
    all_links = soup.find_all("a")
    for link in all_links:
        #print(link.get("href"))
        pass
    all_tables = soup.find_all("table")
    right_table = soup.find_all("table", class_="wikitable sortable plainrowheaders")
    print(right_table)

if __name__ == "__main__":
    main()

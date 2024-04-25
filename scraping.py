# %%
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}

params = {
    "sort_by": "Released_DESC",
}


def get_max_page():
    url_pages = "https://store.steampowered.com/search/results?sort_by=Released_DESC&sort_order=DESC&category1=998&page=1"
    resp = requests.get(url_pages, headers=headers)
    soup_pages = BeautifulSoup(resp.text, features="html.parser")
    max_page = (
        soup_pages.find("div", class_="search_pagination_right").find_all("a")[-2].text
    )
    return int(max_page)


def get_links(max_page):
    links = []
    for page in tqdm(range(1, max_page + 1)):
        url_links = f"https://store.steampowered.com/search/results?sort_by=Released_DESC&sort_order=DESC&category1=998&page={page}"
        resp = requests.get(url_links)
        soup = BeautifulSoup(resp.text, 'html.parser')
        page_links = []
        for link in soup.find("div", {"id": "search_resultsRows"}).find_all("a", href=True):
            page_links.append(link['href'])
        links.append(page_links)
    return links

# %%
def get_content():
    print()

# %%
def main():
    max_page = get_max_page()
    links = get_links(max_page)

# %%
if __name__ == "__main__":
    main()

# %%


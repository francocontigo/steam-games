# %%
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import re

cookies = {"birthtime": "568022401"}

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
        soup = BeautifulSoup(resp.text, "html.parser")
        page_links = []
        for link in soup.find("div", {"id": "search_resultsRows"}).find_all(
            "a", href=True
        ):
            page_links.append(link["href"])
        links.append(page_links)
    return links


# %%
def main():
    max_page = get_max_page()
    links = get_links(5)
    print(links)


# %%
if __name__ == "__main__":
    main()

# %%
a = [
    [
        "https://store.steampowered.com/app/2734830/Joy_Land/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/2880210/Rusty_Dusty/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/2719160/Contractors_Showdown/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/2925430/Sandwich_Sim/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/2448030/Pine_Harbor/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/2917700/Buggy_Derby_Arena/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/2190180/SmileXCorp_3/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/1562420/FOREWARNED/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/1571380/Startenders_Intergalactic_Bartending/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/2850630/Soulbind_Prologue/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/2481220/Automate_Defend_Repeat/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/2085000/SaGa_Emerald_Beyond/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/1887840/Another_Crabs_Treasure/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/1005230/Pixel_Puzzles_Musical/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/2877790/Rogue_Girl/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/2584260/What_have_you_done_Father/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/2889120/Absolute_Fear_AOONI/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/2873430/_/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/2162820/Rustil_Eternal_Labyrinth_Castle/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/1561040/Diluvian_Winds/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/2782490/Teared/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/2685590/TriggerHeart_EXELICA/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/2734460/Fallens_Challenge/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/1471700/Minicology/?snr=1_7_7_230_150_1",
        "https://store.steampowered.com/app/2799040/Cubic_Enigma/?snr=1_7_7_230_150_1",
    ],
    [
        "https://store.steampowered.com/app/2910950/Purpose_Calling/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2887720/Human_Upgrade_Labs/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2742020/DW_The_Picky_Eater/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/1413470/SOL_Search_of_Light/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2171570/Whisker_Waters/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2402280/Werewolf_The_Apocalypse__The_Book_of_Hungry_Names/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2704110/Aliya/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2930500/DNA_Episode_4/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2901870/AOD/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2923010/Field_of_Growth_A_Farmers_Odyssey/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2892770/Bombox/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2712920/Band_of_Brigands/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2563800/The_Last_Game/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2898240/Mystery_Escape/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2695490/Age_of_Water/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2847640/A_Living_Room/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2915280/PAKO_3/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2492410/Bootleg_Steamer/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2926400/What_happened_to_Kate/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2489730/KARSUS/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2929240/FLOOR_10/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2207550/Infected_Chronicles_Surviving_the_Zombie_Apocalypse/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2201930/Oriental_Valley/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2573470/Dice_Assassin/?snr=1_7_7_230_150_2",
        "https://store.steampowered.com/app/2844940/Spellarium_6/?snr=1_7_7_230_150_2",
    ],
]

# %%
url = "https://store.steampowered.com/app/2734830/Joy_Land/?snr=1_7_7_230_150_1"
resp = requests.get(url, headers=headers, cookies=cookies)
soup = BeautifulSoup(resp.text)
print(soup)
# %%
appId = re.search(r'/app/(\d+)', url).group(1)
print(appId)

# %%
appName = soup.find("div", {"id": "appHubAppName"}).text

# %%
reviews = soup.find("div", {"id": "userReviews"}).find_all("div", class_="user_reviews_summary_row")


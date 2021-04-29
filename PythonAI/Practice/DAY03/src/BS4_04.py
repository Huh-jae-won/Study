from bs4 import BeautifulSoup

with open("../data/fruits-vege.html",encoding="utf-8") as fp :
    soup = BeautifulSoup(fp,"html.parser")

    print(soup.select_one("#ve-list>li:nth-of-type(4)").string)
    lists = soup.select("#fr-list>li")
    for i in lists:
        print(i.string)
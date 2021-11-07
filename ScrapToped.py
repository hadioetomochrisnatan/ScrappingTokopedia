import requests
import json
import csv
from bs4 import BeautifulSoup


def get_session():
    header = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/81.0.4044.141 Safari/537.36"}
    url = "https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=1"
    request = requests.get(url, headers=header, timeout=5)
    html = BeautifulSoup(request.content, "html.parser")
    rows = html.find("div", {"class": "css-13l3l78 e1nlzfl10"})
    divs = rows.findAll("div", {"class": "css-bk6tzz e1nlzfl3"})
    data = []
    for div in divs:
        title = div.find("div", class_="css-11s9vse").text
        price = div.find("div", class_="css-4u82jy").text
        origin = div.find("div", class_="css-vbihp9").text
        link = div.a.get("href")
        img = div.find("div", class_="css-1c0vu8l").img.get("src")
        obj = {
            "nama": title,
            "harga": price,
            "kota/nama toko": origin,
            "img": img,
            "link": link
        }
        data.append(obj)
    return data


if __name__ == '__main__':
    products = get_session()
    for product in products:
        print(product)

    f = open('products.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(["Nama", "Harga", "Kota/Nama Toko", "Img", "Link"])
    for product in products:
        writer.writerow([product["nama"], product["harga"], product["kota/nama toko"], product["img"], product["link"]])
    f.close()


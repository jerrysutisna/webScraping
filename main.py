from bs4 import BeautifulSoup

html_text = open("BCA - Reksadana.html", "r").read()
soup = BeautifulSoup(html_text, 'lxml')
extract_text_1 = soup.find("div", class_="container my-40")
extract_text_2 = extract_text_1.find("div", class_="m-sidebar-product my-24 row mx-0")
extract_text_3 = extract_text_2.find("div", class_="m-sidebar-product-content is-active")
extract_text_4 = extract_text_3.find_all("p")

#print(extract_text_4[1].text)

message = ""

for i in extract_text_4:
    message = message + i.text

print(message)



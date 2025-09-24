from bs4 import BeautifulSoup

with open("../data/SalesTransactions.xml", "r") as f:
    data = f.read()

bs_data = BeautifulSoup(data, "lxml")

UelSample = bs_data.find_all("UelSample")
print(UelSample)
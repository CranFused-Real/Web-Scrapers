# Importing Libraries

import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

url = "https://example.com/" # URL of the website of which you want to scrape URLs
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

links = soup.find_all("a")
num_links = len(links)

filename = "output.html" # Output File name
count = 1
while os.path.exists(filename):
    count += 1
    filename = f"output{count}.html"

with open(filename, "w") as f: # Saving Output file as HTML Format
    f.write("<html>\n<head>\n<title>Links Scraped</title>\n</head>\n<body>\n")
    for i, link in enumerate(tqdm(links, desc="Writing links to file", unit="link")):
        f.write(f"<a href='{link.get('href', '')}'>{link.text.strip()}</a><br>\n")
        if i % 10 == 0:
            f.flush() # Flush buffer every 10 links to avoid losing data in case of a crash
    f.write(f"<p>Number of links found: {num_links}</p>\n</body>\n</html>")

print(f"Finished! Number of links found: {num_links}")
print(f"Output saved in {filename}")

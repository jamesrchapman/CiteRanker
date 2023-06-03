import requests
from bs4 import BeautifulSoup

def get_citation_citations(publication_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }
    
    response = requests.get(publication_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    citations = []
    for citation in soup.find_all('a', class_='gs_ri'):
        title = citation.find('h3', class_='gs_rt').text.strip()
        citations.append(title)
    
    return citations

# Example usage
publication_url = 'https://www.ahajournals.org/doi/full/10.1161/CIRCRESAHA.110.227496'
citations = get_citation_citations(publication_url)

for citation in citations:
    print(f"Citation: {citation}")

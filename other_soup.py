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
publication_url = '<URL of the publication on Google Scholar>'
citations = get_citation_citations(publication_url)

for citation in citations:
    print(f"Citation: {citation}")



import requests
from bs4 import BeautifulSoup

def get_google_scholar_results(query):
    url = f"https://scholar.google.com/scholar?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = []
    for result in soup.find_all('div', class_='gs_r gs_or gs_scl'):
        title = result.find('h3', class_='gs_rt').text.strip()
        citations_link = result.find('a', class_='gs_or_cit')
        citations = citations_link.text.strip() if citations_link else '0'
        result_data = {
            'title': title,
            'citations': citations
        }
        results.append(result_data)
    
    return results

# Example usage
search_query = 'machine learning bioinformatics'
results = get_google_scholar_results(search_query)

for result in results:
    print(f"Title: {result['title']}")
    print(f"Citations: {result['citations']}")
    print("---------")

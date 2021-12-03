import pandas as pd
from requests_html import HTMLSession

file = 'GENOMELinks.xlsx'
links = pd.read_excel(file, index_col=1)
domains = links['DOMAIN'].values
your_link = 'genome.eu'


finded_link = []
not_found = []

print(len(domains))
for domain in domains:
    session = HTMLSession()
    response = session.get(domain)
    html = response.html


    # try:
    #     count = html.count(your_link)
    #     if count > 0:
    #         finded_link.append(domain)
    #     else:
    #         not_found.append(domain)
    # except:
    #     not_found.append(domain)
    try:
        # search = html.find(your_link, first=True)
        search = response.html.text.count(your_link)
        if search > 0:
            finded_link.append(domain)
        else:
            finded = False
            search = response.html.links
            for link in search:
                if your_link in link:
                    finded = True
                    break
            if finded:
                finded_link.append(domain)
            else:
                not_found.append(domain)
    except Exception as e:
        print(e)
        not_found.append(domain)
        break

print(len(finded_link))
print(len(not_found))
print(not_found)


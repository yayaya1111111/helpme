import requests 
import json

headers = {
    "Accept-Encoding": "gzip,deflate",
    "User-Agent": "Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
}

def wikidata_scraper(url):
    id = ''
    label = ''
    desc = ''
    data = json.loads(requests.get(url, headers=headers).content)
    for entities in data.values():
        for entity in entities.values():
            for tag in entity.keys():
                if tag == 'id':
                    id = entity.get(tag)
                elif tag == 'labels':
                    for lang in entity.get(tag):
                        if lang == 'en':
                            label = entity.get(tag).get('en').get('value')
                            break
                        elif lang == 'mul':
                            label = entity.get(tag).get('mul').get('value')
                            break
                    else:
                        label = "No label"           
                elif tag == 'descriptions':
                    for lang in entity.get(tag):
                        if lang == 'en':
                            desc = entity.get(tag).get('en').get('value')
                            break
                        else:
                            desc = 'No description'
    return {
        "ID": id,
        "LABEL": label, 
        "DESCRIPTION": desc,
    }
# import urllib.request

# opener=urllib.request.build_opener()
# response=opener.open("https://www.marvel.com/")
# print(response.read())


import requests
# response=requests.get("https://www.ukr.net/")

# print(response.text)

response=requests.get("https://coinmarketcap.com/")
response_text=response.text
# print(response.status_code)
#print(response_text)
response_parse=response_text.split("<span>")
# print("*"*40)
# print(response_parse)
# print("*"*40)
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                print(parse_elem_2)
 
 


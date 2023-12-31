import requests

# if we want to send https request by using python we use this.
# there are lot of request which we can send ex: get,post,port,hat,delete ,option and many more.
# but here we only talk about get and post request.

#  get request = use to get contents of any url:

r = requests.get("https://financialmodelingprep.com/api/v3/financial-statement-symbol-lists?apikey=YOUR_API_KEY")
print(r.text)  # .text convert to json format.
# status code of url:
print(r.status_code)    # 200

# post request - special type of request. jiska ek url end point hota h ,aur ussi ke sath kuchh data bhejna padta h.
# aur jiss url pr ye request jaaega wo iske data ko verify karega aur phir respond send karega.:

url = "https://financialmodelingprep.com/api/v3/financial-statement-symbol-lists?apikey=YOUR_API_KEY"
data = {
    "P1": 5,
    "P2": 67,
    "P3": 56,
    "P4": 14,
    "P5": 57,
}
r2 = requests.post(url=url, data=data)  # sending post request



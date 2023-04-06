import requests

# define a function that gets json data from a url

def get_json(url):
    """
    get_json(url)
    url: url of the json data to download
    returns: json data
    """
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return False
    
data = get_json("https://jsonplaceholder.typicode.com/todos/1")
print(data)
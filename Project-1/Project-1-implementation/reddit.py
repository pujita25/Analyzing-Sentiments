import datetime
import pymongo
import requests

##Connection to mongodb has been set up by getting databases and connection to collections


my_client = pymongo.MongoClient("mongodb://localhost:27017/")
database_str = my_client["redditdatabase"]
db_collection = database_str["redditcomments"]

##Reddit API aunthentication
user_agent = "u/sys_squad/0.0.1"
base_url = 'https://www.reddit.com/api/v1/access_token'
data = {'grant_type': 'password', 'username': "sys_squad", 'password': "Qwerty1234"}
auth = requests.auth.HTTPBasicAuth("y47tJNzKzBBvSiu0KB-OhQ", "YLoPJTJExY1asK9Uq9k7ESgcmNBlXQ")
api_url = 'https://oauth.reddit.com'
headers = {}    

#Main function to validate and get the bearer token
def validate():
    print("in validate_1.1")
    res = requests.post(base_url,
                                    data=data,
                                    headers={'User-Agent':user_agent},
                                    auth=auth)
    if res.status_code == 200:
        bearer_details = res.json()
        token = 'bearer ' + bearer_details['access_token']
        headers['Authorization'] = token
        headers['User-Agent'] = user_agent
        response = requests.get(api_url + '/api/v1/me', headers=headers)
        return response.status_code == 200

# Function to check if the validation is correct and get all subreddits and extracts comments
def get_reddit_comemnts():
    if validate() is True:
        req_all_sub_reddits()
        req_all_comments()

#function is used to prettyify data object
def time_p(created_utc):
    from datetime import datetime
    return datetime.fromtimestamp(created_utc).strftime("%Y-%m-%d %H:%M:%S")


# Function used to check the tree like structure in the comment data and extract the comments and put to the data base
def extract_tree_strc(x, subr_in, id_x, id_children):
    if len(x) <= id_x:
        return

    if x[id_x].get('data').get("children") is None:
        if rec_avail(x[id_x].get('data').get('id')):
            my_dict = {"subReddits": subr_in,
                       "comments": x[id_x].get('data').get('body'),
                       "created_utc": time_p(x[id_x].get('data').get('created_utc')),
                       "time": datetime.datetime.now(),
                       "comm_id": x[id_x].get('data').get('id')
                       }
            db_collection.insert_one(my_dict)
        extract_tree_strc(x, subr_in, id_x + 1, id_children)
    else:
        extract_tree_strc(x[id_x].get('data').get('children'), subr_in, 0, 0)


subreddits_comments = []
ids_val = []

# using the key words in query / this functions pull the subreddits matching the given keywords 
def req_all_sub_reddits():
    query = (
            'games' or 'players' or 'dota2' or 'valorant' or 'game'
            or 'fun' or 'action' or 'heroes' or 'league of legends'
            or 'CSGO' or 'counter strike global offensive' or 'PUBG' or 'steam'
            or 'agents' or 'riot' or 'nvdia' or 'rank' or 'top players'
            )
    payload = {'q': query, 'limit': 100, 'sort': 'relevance' or 'top' or 'new' or 'hot', 'type': 'sr'}
    subreddit_response = requests.get(api_url + '/search/',
                                      headers=headers, params=payload)
    if subreddit_response.status_code == 200:
        final_values = subreddit_response.json()
        for i in range(len(final_values['data']['children'])):
            subreddits_comments.append(final_values['data']['children'][i]['data']['display_name'])
            ids_val.append(final_values['data']['children'][i]['data']['name'])

#extracts the comments
def req_all_comments():
    # global count
    for sub_reddit in subreddits_comments:
        comments_data = requests.get(api_url + '/r/' + sub_reddit + '/comments/', headers=headers)
        if comments_data.status_code == 200:
            final_values = comments_data.json()
            if final_values.get('data') is not None:
                vals = final_values.get('data').get('children')
                print('Extracting the comments from the subreddit - ' + sub_reddit + '.......\r', end='', flush=True)
                extract_tree_strc(vals, sub_reddit, 0, 0, )
    subreddits_comments.clear()

def rec_avail(comm_id):
    return db_collection.count_documents({"comm_id": comm_id}, limit=1) == 0
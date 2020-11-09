#!/usr/bin/env python3

import threading
import itertools
import requests
import string
import json

def checker(combinations, num):
    while combinations:
        combination = combinations[0]
        combinations.remove(combination)

        url = f'https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={api_key}&vanityurl={combination}'
        response = requests.get(url)
        json_content = json.loads(response.content)

        if json_content['response']['success'] != 1:
            with open('steam_ids.txt', 'a+') as f:
                f.write(combination + '\n')
            print(f'[{num}] Available ID: {combination}')



if __name__ == "__main__":

    api_key = '0229FFB71F0B23AD41AE361AA92C0FF4'
    chars = string.ascii_lowercase + string.digits + '_' + '-'
    possible_combinations = [''.join(i) for i in itertools.product(chars, repeat = 3)]

    print('Looking for available 3 letter steam IDs...')

    for i in range(200):
        checker_thread = threading.Thread(target=checker, args=(possible_combinations,i))
        checker_thread.start()

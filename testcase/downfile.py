
import json
import hashlib
import os
import requests
import time


def get_md5(file_path):
    md5 = None
    if os.path.isfile(file_path):
        f = open(file_path,'rb')
        md5_obj = hashlib.md5()
        md5_obj.update(f.read())
        hash_code = md5_obj.hexdigest()
        f.close()
        md5 = str(hash_code).lower()
    return md5


def store(data):
    with open('data.json', 'a') as json_file:
        json_file.write(json.dumps(data))


def geturl_dy(filename):
    content = open(filename, encoding='utf-8-sig')
    content_json = json.load(content)
    array = []
    musiclist_array = content_json['music_list']
    for musiclist in musiclist_array:
        url = musiclist['play_url']['url_list'][0]
        array.append(url)
        print(url)
    return array


def check_md5(filename):
    file_md5 = get_md5(filename)
    with open('md5.txt', 'r') as foo:
        for line in foo.readlines():
            if file_md5 in line:
                print(line)
                return 1
            else:
                return 0


def store_md5(filename):
    data = get_md5(filename)
    with open('md5.txt', 'a') as json_file:
        json_file.writelines(data + '\n')


def download(url_array):
    for url in url_array:
        try:
            r = requests.get(url)
            file_name_mp4 = str(time.time()) + ".mp4"
            with open(file_name_mp4, 'wb') as f:
                f.write(r.content)

            if check_md5(file_name_mp4) == 1:
                os.remove(file_name_mp4)
            else:
                store_md5(file_name_mp4)
        except:
            print(url+' run error')


url_array = geturl_dy('dy.json')
download(url_array)




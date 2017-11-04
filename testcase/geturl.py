
import json
import hashlib
import os
import urllib
import requests


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


def getdownloadurl(filename):
    content = open(filename, encoding='utf-8-sig')
    content_json = json.load(content)
    dataall = []
    for i in range(20):
        cover = content_json['music_list'][i]['cover_thumb']['url_list'][0]
        playurl = content_json['music_list'][i]['play_url']['url_list'][0]
        title = content_json['music_list'][i]['title']
        author = content_json['music_list'][i]['author']
        data = {}
        data["cover"] = cover
        data["playurl"] = playurl
        data["title"] = title
        data['author'] = author
        dataall.append(data)
        print(dataall[i])
    store(dataall)


def check_md5(filename):
    file_md5 = get_md5(filename)
    with open('md5.txt', 'r') as foo:
        for line in foo.readlines():
            print(file_md5)
            if file_md5 in line:
                print(line)
                return 1
            else:
                return 0


def store_md5(filename):
    data = get_md5(filename)
    with open('md5.txt', 'a') as json_file:
        json_file.writelines(data)


def download():
    content = open('data.json', encoding='utf-8-sig')
    content_json = json.load(content)
    url_array = content_json['playurl']
    index = 0
    for i in url_array:
        # downloadurl = url_array[i]
        r = requests.get(i)
        file_name_mp4 = str(index) + ".mp4"
        with open(file_name_mp4, 'wb') as f:
            f.write(r.content)

        if check_md5(file_name_mp4) == 1:
            os.remove(file_name_mp4)
        else:
            store_md5(file_name_mp4)
        index = index + 1

download()




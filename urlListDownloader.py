import os
from urllib import request

imgUrls = []

def get_url_list(file_name):
    try:
        file = open(file_name)
        global imgUrls
        imgUrls = file.readlines()
        
        for i in range(len(imgUrls)) :
            imgUrls[i] = imgUrls[i].replace('\n','')
        
    except Exception as e:
        print('Err: ', e)
    
    finally:
        file.close()
        
def download_url_list(url_list,folder_name):
    try:
        file_path = folder_name
        if not os.path.exists(file_path):
            print('File: ', "'", file_path, "'", ' created!')
            os.makedirs(file_path)
        
        imgCounter = 0

        opener = request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        request.install_opener(opener)
        
        for item in url_list :
            file_name = str(imgCounter)
            file_name = '{}{}{}{}'.format(file_path, os.sep, file_name, '.jpg')
            request.urlretrieve(item, filename=file_name)
            print("File '", imgCounter ,"' downloaded successfully!")
            imgCounter = imgCounter + 1
            
    except Exception as e:
        print('Err: ', e)

get_url_list('url_list.txt')
download_url_list(imgUrls, 'photos')
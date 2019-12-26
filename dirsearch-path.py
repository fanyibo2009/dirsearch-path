# __author__:无尾熊
# dirsearch path.tar
 
import requests

u = input("请输入网址，for example 'http://111.123.3.33:28000/cmis/' \n")
domain = u.split("/")

for i in domain:
    Unzip_dist = ['.rar', '.zip', '.gz', '.sql.gz', '.tar.gz', '.sql', '.tar.tgz', '.tar','.war']
    for z in Unzip_dist:
        dist = i + z
        # print (dist)
        
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        r = requests.head(u+dist, headers = headers)
        if r.status_code == 200:
            print ("存在备份文件，请注意！！！")
            print ("存在备份文件，请注意！！！")
            print ("存在备份文件，请注意！！！")
        print (r.url,[r.status_code])

        

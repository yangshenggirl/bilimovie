import json
f = open("E:\python\envs\penv36\Scripts\scrapy\\bilimovie\output\movie_20180927.json",'r',encoding='utf-8')
ln = 0
for line in f.readlines():
    ln += 1
    dic = json.loads(line)
    t = dic['num'],dic['name'],dic['love'],dic['comment'],dic['score']
    f = open("E:\python\envs\penv36\Scripts\scrapy\\bilimovie\output\data.txt",'a')
    f.writelines(str(t));f.write("\n")
f.write(str(ln))
f.close()
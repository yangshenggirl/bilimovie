import jieba#分词 插件
import matplotlib.pyplot as plt#绘图函数
from wordcloud import WordCloud
import numpy as np 
from PIL import Image

#读取文本信息
text = open(r'output/data.txt','r').read()#强制不转义
#print(text)
cut_word = jieba.cut(text)
result = ' '.join(cut_word)
#print(result)

#生成词云图
abel_mask = np.array(Image.open("output/pic.jpg"))
wc = WordCloud(
    #字体路径
    font_path =r'.\simhei.ttf',
    background_color = 'white',
    #pic_size
    width=500,
    height=350,
    max_font_size=30,#字体的大小
    min_font_size=12,
    mask = abel_mask,
    #image_colors = ImageColorGenerator(practice.jpg)
)
wc.generate(result)
wc.to_file(r'.\wordcloud.png')

#显示图片
#指定图片名称
plt.figure()
plt.imshow(wc)
plt.axis('off')
plt.show()

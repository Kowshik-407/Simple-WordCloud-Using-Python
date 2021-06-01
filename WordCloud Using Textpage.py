from wordcloud import WordCloud, STOPWORDS

comment_words=' '
stopwords=set(STOPWORDS)
f=open('file.txt','r+')
textdata=f.read().replace('\n','')

wordcloud=WordCloud(width=800,height=800,
                    background_color="White",
                    stopwords=stopwords,
                    min_font_size=10).generate(textdata)
wordcloud.to_file('image.jpg')
print('Image Saved Successfully')

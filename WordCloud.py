import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
c="Dilip kumar artist? monster otaku honest sensitive grieving broken demon working hard video-editor? sportsman? monster otaku honest sensitive grieving broken demon working hard dancer? nerd? weak? Dilip kumar artist? monster otaku honest sensitive grieving broken demon working hard video-editor? sportsman? dancer? nerd? weak? crazy monster otaku honest sensitive grieving broken demon working hard"
c=re.split("\s", c)
print(c)
c=Counter(c)
wc= WordCloud(width=400, height=330, max_words=50, background_color='white').generate_from_frequencies(c)
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

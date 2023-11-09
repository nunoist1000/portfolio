import streamlit as st
from PIL import Image
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")


img_1 = Image.open("images/1.png")
img_2 = Image.open("images/2.png")
img_3 = Image.open("images/3.png")

st.title("What my resume doesnt show...🤖")

col1, col2, col3 = st.columns(3)

with col1:
   st.image(img_1)
   
with col2:
   st.image(img_2)

with col3:
   st.image(img_3)

hobbies_markdown = """
## Hobbies and Interests 🚀

### Creative Pursuits
- 🔥 **Woodburning**: Crafting unique designs on wood, creating art that lasts.
- 🔧 **Repairing**: Bringing new life to broken objects, enjoying the process of troubleshooting and fixing.

### Family
- 👨‍👩‍👧‍👦 **Parenting**: Raising four wonderful kids, each day is a learning experience filled with joy and challenges.
- ❤️ **Quality Time**: Spending precious moments with my wife, building a treasure trove of memories.

### Personal Development
- 📚 **Lifelong Learning**: Constantly acquiring new skills and knowledge, embracing the joy of learning.
- 🥾 **Hiking**: Exploring the great outdoors, finding peace and solitude in nature's beauty.

### Exploration
- 🎨 **Creative Exploration**: Delving into my artistic side, always looking for new ways to express creativity.
- 🗺️ **Adventures with Family**: Whether it's a hike through the mountains or a walk in the park, it's all about making the most of our time together.
"""

st.markdown(hobbies_markdown)
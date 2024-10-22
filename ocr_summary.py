#pip install opencv-python-headless --prefer-binary
#pip install opencv-python-headless==4.5.5.62
#pip install easyocr --default-timeout=1000
#pip install -q -U google-generativeai


import easyocr
import pandas as pd
import numpy as np
import glob
from datetime import date

# Testfunction
reader = easyocr.Reader(['en'])
image_path = "images/02024-09-30 17:45:21article.png"

result = reader.readtext(image_path)
text = ''
for item in result:
    text += item[1] + ' '

print(text , result)


#getimagelinks

image_set= glob.glob('images/*')
image_set

all_story_text=[]
for i in image_set:
  reader = easyocr.Reader(['en'])
  image_path = i
  print(image_path)

  result = reader.readtext(image_path)
  text = ''
  for item in result:
      text += item[1] + ' '

  print(text)
  all_story_text.append(text)

today = date.today()
todays_date = today.strftime("%Y_%m_%d")
stock_name="netflix"

# Create Pandas DataFrame
df2 = pd.DataFrame({
    'All_Stories': all_story_text,
    "info":f"{todays_date}_{stock_name}"
})

# Print DataFrame
print(df2)

# Save to CSV file
df2.to_csv('allstories.csv', index=False)

print("done")

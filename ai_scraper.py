import yfinance as yf
import datetime
from web_scraper_helper import *
import pandas as pd
#!pip install playwright
#!playwright install
import playwright.async_api as pw
#import easyocr


stock = yf.Ticker(tickers[5])
news_data= stock.news



# Assuming 'news_data' is your list of news articles
for article in news_data:
    timestamp = article['providerPublishTime']
    date_published = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    print(f"Title: {article['title']}")
    print(f"Published: {date_published}")
    print(f"Link: {article['link']}")
    print("------------------------")
    
    
# Initialize empty lists
titles = []
links = []
publishers = []
types = []
dates = []

for article in news_data:
    title = article['title']
    link = article['link']
    publisher = article['publisher']
    type = article['type']
    timestamp = article['providerPublishTime']
    date_published = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    # Append to lists
    titles.append(title)
    links.append(link)
    publishers.append(publisher)
    types.append(type)
    dates.append(date_published)

# Create Pandas DataFrame
df = pd.DataFrame({
    'Title': titles,
    'Link': links,
    'Publisher': publishers,
    'Type': types,
    'Date Published': dates
})

# Print DataFrame
print(df)

# Save to CSV file
df.to_csv('news_database.csv', index=False)
print(df.shape)

import asyncio
from playwright.async_api import async_playwright   




link_df= pd.read_csv('news_database.csv')
link_df[['Link','Date Published']]

for index, row in link_df[['Link', 'Date Published']].iterrows():
    async def take_screenshot(url, filename):
        async with async_playwright() as p:
            # Launch browser in non-headless mode to better simulate real user experience
            browser = await p.chromium.launch(headless=False)
            
            # Create a new browser context with JavaScript disabled
            context = await browser.new_context(java_script_enabled=False) 
            
            page = await context.new_page()
            
            try:
                # Navigate to the URL with extended timeout and wait until network becomes idle
                await page.goto(url, wait_until="networkidle", timeout=60000)  # 60 seconds timeout
                
                # Scroll to the bottom of the page to make sure all elements are loaded
                await page.evaluate("""{ window.scrollTo(0, document.body.scrollHeight); }""")
                
                # Wait for 3 seconds to ensure any lazy-loaded elements are loaded
                await page.wait_for_timeout(3000)
                
                # Take a full-page screenshot
                await page.screenshot(path=filename, full_page=True)
                print(f"Screenshot saved to {filename}")
            
            except Exception as e:
                print(f"Error: {e}")
            
            finally:
                # Close the browser
                await browser.close()

    # URL and output filename
    url = row['Link']
    filename = "images/"+ str(index) + str(row['Date Published']) + "article.png"

    async def main():
        await take_screenshot(url, filename)

    # Run the main function to take the screenshot
    asyncio.run(main())

print("done")
#!/usr/bin/env python
# coding: utf-8

# In[72]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd


# In[59]:


# Windows users
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path)


# In[60]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[61]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[62]:


slide_elem.find("div", class_='content_title')


# In[63]:


#use the parent elements to find the first 'a'a tag an save it as 'news_title'.
news_title = slide_elem.find("div", class_="content_title").get_text()
news_title


# In[64]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### Featured Images

# In[65]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[66]:


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[67]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()


# In[69]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[70]:


# Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[71]:


# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# In[73]:


df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


# In[74]:


df.to_html()


# In[75]:


browser.quit()


# In[ ]:





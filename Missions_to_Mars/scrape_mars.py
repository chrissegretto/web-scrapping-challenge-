#!/usr/bin/env python
# coding: utf-8

# In[43]:


# !pip install splinter 


# In[44]:


# !pip install webdriver-manager


# In[45]:


from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


# In[46]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[47]:
def webscrapping():


    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)


    # In[48]:


    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')


    # In[49]:


    # display(soup)


    # In[50]:


    news_title = soup.find_all("div",{"class":"content_title"})
    title = news_title[0].text


    # In[51]:


    news_p = soup.find_all("div",{"class":"article_teaser_body"})
    para = news_p[0].text


    # In[52]:


    # JPL = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    # JPL ="https://www.jpl.nasa.gov/images?search=&category=Mars"
    # I tried both urls above they didnt work
    JPL = "https://spaceimages-mars.com/"


    # In[53]:


    browser.visit(JPL)


    # In[54]:


    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')


    # In[55]:


    fancy_box = soup.find("a",{"class":"showimg fancybox-thumbs"})["href"]
    image= JPL+fancy_box
    print(image)


    # In[56]:


    import pandas as pd 


    # In[57]:


    url3 = "https://galaxyfacts-mars.com/"
    marsdf = pd.read_html(url3) 
    marsdf


    # In[58]:


    marsdf = marsdf[1]
    marsdf


    # In[59]:


    html_table = marsdf.to_html(index = False, header = False)


    # In[64]:


    url4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url4)


    # In[65]:


    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')


    # In[66]:


    astro = soup.find_all("div",{"class":"description"})


    # In[67]:


    astro_list =[]
    for link in astro: 
        title = link.find("h3").text
        urls = link.find('a')["href"]
        image_link = "https://astrogeology.usgs.gov"+ urls
        browser.visit(image_link)
        html = browser.html
        image_soup = BeautifulSoup(html, 'html.parser')
        image_links = "https://astrogeology.usgs.gov" + image_soup.find("img",{"class":"wide-image"})["src"]
        astro_list.append({"Title": title, "Image" : image_links })


    # In[68]:


    astro_list 


    # # In[ ]:
    # creating dictionary for all scrapped data 
    scrap_data = {
        "Title": title,
        "Paragraph": para,
        "Image": image,
        "Table": html_table,
        "Hem" : astro_list}
    return scrap_data
    




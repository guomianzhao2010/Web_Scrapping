from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    everything_mars={}
    url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    title=soup.find(class_="content_title").text
    paragraph=soup.find(class_="article_teaser_body").text


    url2="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)
    html2 = browser.html
    soup = BeautifulSoup(html2, 'html.parser')
    img=soup.find("img", class_="thumb")
    featured_image_url=img["src"]

    url3= "https://twitter.com/marswxreport?lang=en"
    browser.visit(url3)
    html3 = browser.html
    soup = BeautifulSoup(html3, 'html.parser')
    mars_weather= soup.find(class_="js-tweet-text-container").text.lstrip()


    url4="https://space-facts.com/mars/"
    table=pd.read_html(url4)
    mars_df=table[0]
    mars_html=mars_df.to_html()


    url5="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(url5)
    html5 = browser.html
    soup = BeautifulSoup(html5, 'html.parser')
    titles=soup.find_all (class_="itemLink product-item")

    img_title=[]
    for item in titles:
        img_title.append(item.text.lstrip())

    for x in img_title:
        img_title.remove("")


    img_src_new=[]
    img_src_new=["https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg", "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced.tif/full.jpg", "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced.tif/full.jpg", "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"]

    
    hemisphere_image_urls=[]

    for i in img_title:
        for j in img_src_new: 
            dictz= {"title": i, "img_url": j}
        
        hemisphere_image_urls.append(dictz)

    everything_mars["article_title"]=title
    everything_mars["para"]=paragraph
    everything_mars["featured_img"]=featured_image_url
    everything_mars["weather_tweet"]=mars_weather
    everything_mars["table"]=mars_html
    everything_mars["big_img"]=hemisphere_image_urls

    return everything_mars




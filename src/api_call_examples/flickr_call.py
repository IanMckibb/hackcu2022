import flickrapi
import urllib

# Flickr api access key 
flickr=flickrapi.FlickrAPI('c6a2c45591d4973ff525042472446ca2', '202ffe6f387ce29b', cache=True)

keyword = 'dog'

photos = flickr.walk(text=keyword,
                     tag_mode='all',
                     tags=keyword,
                     extras='url_c',
                     per_page=100,           # may be you can try different numbers..
                     sort='relevance')

urls = []
for i, photo in enumerate(photos):
    print (i)
    
    url = photo.get('url_c')
    urls.append(url)
    
    if i > 1:
        break

print (urls[1])

# Download image from the url and save it to '00001.jpg'
# rllib.urlretrieve(urls[1], '00001.jpg')

# Resize the image and overwrite it
# image = Image.open('00001.jpg') 
# image = image.resize((256, 256), Image.ANTIALIAS)
# image.save('00001.jpg')
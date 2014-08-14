# Scrapy settings for iosicongallery project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#



BOT_NAME = 'iosicongallery'


SPIDER_MODULES = ['iosicongallery.spiders']
NEWSPIDER_MODULE = 'iosicongallery.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'iosicongallery (+http://www.yourdomain.com)'

ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
IMAGES_STORE = 'E:/rover-self-work/python/iosicongallery/data'
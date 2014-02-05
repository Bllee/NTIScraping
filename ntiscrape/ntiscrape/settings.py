# Scrapy settings for ntiscrape project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ntiscrape'

SPIDER_MODULES = ['ntiscrape.spiders']
NEWSPIDER_MODULE = 'ntiscrape.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ntiscrape (+http://www.yourdomain.com)'

from scrapy import cmdline
import sys

if sys.argv[1] == 'nation_water':
    cmdline.execute('scrapy crawl nationalwaterpollution'.split())
elif sys.argv[1] == 'nation_pm':
    cmdline.execute('scrapy crawl nationalpm'.split())
elif sys.argv[1] == 'nation_solid_pollution':
    cmdline.execute(('scrapy crawl nationalsolidpollution -a kwlist=' + sys.argv[2] + ' -a year=' + sys.argv[3]).split())
elif sys.argv[1] == 'world_pm':
    cmdline.execute('scrapy crawl worldpm'.split())


from scrapy import cmdline
import sys

if sys.argv[1] == 'nation_water':
    cmdline.execute('scrapy crawl nationalwaterpollution'.split())
elif sys.argv[1] == 'nation_pm':
    cmdline.execute('scrapy crawl nationalpm'.split())
elif sys.argv[1] == 'nation_solid_pollution':
    cmdline.execute(('scrapy crawl nationalsolidpollution -s CLOSESPIDER_ITEMCOUNT='+str(sys.argv[2])+' -a count='+str(sys.argv[2])+' -a kws='+sys.argv[3]+' -a districts='+sys.argv[4]+' -a start_year='+str(sys.argv[5])+' -a end_year='+str(sys.argv[6])).split())
elif sys.argv[1] == 'world_pm':
    cmdline.execute('scrapy crawl worldpm'.split())



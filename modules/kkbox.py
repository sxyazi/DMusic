import re
import json
import requests


class KKBox:

    @staticmethod
    def ranks(typ):
        urls = {
            'hourly': 'https://kma.kkbox.com/charts/hourly?lang=tc&terr=tw',
            'daily': 'https://kma.kkbox.com/charts/daily/newrelease?lang=tc&terr=tw',
            'weekly': 'https://kma.kkbox.com/charts/weekly/newrelease?lang=tc&terr=tw',
            'yearly': 'https://kma.kkbox.com/charts/yearly/newrelease?lang=tc&terr=tw'}

        source = requests.get(urls[typ]).text

        lis = json.loads(re.search('var chart = (.*?);\n', source).group(1))
        return lis['charts']['newrelease'] if 'charts' in lis else lis

import re
import json
import requests


class KKBox:

    @staticmethod
    def ranks():
        source = requests.get(
            'https://kma.kkbox.com/charts/yearly/newrelease?lang=tc&terr=tw').text
        return json.loads(re.search('var chart = (.*?);', source).group(1))

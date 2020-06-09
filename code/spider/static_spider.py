import requests
from lxml import etree


def bilibili_url_builder(content):
    url = 'https://www.bilibili.com/read/%s'
    return url % content


def spider_builder(*, url_bulider, xpath_rules, **kwargs):

    def spider(content):
        response = requests.get(url_bulider(content), **kwargs)
        html = etree.HTML(response.text)
        # print(etree.tostring(html, encoding=str, pretty_print=True))
        return (html.xpath(rule) for rule in xpath_rules)

    return spider


def print_results(results, division='-'*10, sep='\n'):
    for item in results:
        print(division, sep.join(item), sep=sep)


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/81.0.4044.92 Safari/537.36'
    }

    xpath_rules = [
        '//h1[contains(@class,"title")]//text()',
        '//div[contains(@class,"article-holder")]//text()',
        '//figure[contains(@class,"img-box")]/img/@data-src'
    ]

    bilibili_spider = spider_builder(url_bulider=bilibili_url_builder,
                                     xpath_rules=xpath_rules,
                                     headers=headers, params={})

    print_results(bilibili_spider('cv6361390'))
    # title, holder, img = bilibili_spider('cv2709447')

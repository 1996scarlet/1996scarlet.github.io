import requests
from lxml import etree
import asyncio


def baike_url_builder(content):
    url = 'https://baike.baidu.com%s'
    return url % content


def spider_builder(*, url_bulider, xpath_rules, **kwargs):

    def spider(content):
        response = requests.get(url_bulider(content), **kwargs)
        html = etree.HTML(response.text)
        return (html.xpath(rule) for rule in xpath_rules)

    return spider


def print_results(results, division='-'*10, sep='\n'):
    for item in results:
        print(division, sep.join(item), sep=sep)


async def baike_deal(spider, queue):
    url = await queue.get()

    results = spider(url)

    title = next(results)
    print(title)

    for ref in next(results):
        try:
            await asyncio.wait_for(queue.put(ref), timeout=0.01)
        except asyncio.TimeoutError:
            pass


async def spider_loop(spider, queue):
    while True:
        await baike_deal(spider, queue)
        # await asyncio.gather(
        #     read_queue(),
        #     # asyncio.sleep(0.01)
        # )

        # queue.task_done()


async def main():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/81.0.4044.92 Safari/537.36'
    }

    xpath_rules = [
        '//dd[contains(@class,"lemmaWgt-lemmaTitle-title")]/h1/text()',
        '//div[contains(@class,"lemma-summary")]//a[contains(@target,"_blank")]/@href',
    ]

    baike_spider = spider_builder(url_bulider=baike_url_builder,
                                  xpath_rules=xpath_rules,
                                  headers=headers, params={})

    spider_queue = asyncio.Queue(256)
    await spider_queue.put("/item/波恩哈德·黎曼")

    tasks = [spider_loop(baike_spider, spider_queue) for i in range(6)]
    await asyncio.gather(*tasks)

asyncio.run(main())

import asyncio
import aiohttp
from lxml import etree

MAX_URL_NUM = 256
QUEUE_TIMEOUT=0.01
SPIDER_NUM = 6

def baike_url_builder(content):
    url = 'https://baike.baidu.com%s'
    return url % content


def spider_builder(*, session, url_bulider, xpath_rules, **kwargs):

    async def spider(content):
        response = await session.get(url_bulider(content), **kwargs)
        html = etree.HTML(await response.text())
        return (html.xpath(rule) for rule in xpath_rules)

    return spider


def print_results(results, division='-'*10, sep='\n'):
    for item in results:
        print(division, sep.join(item), sep=sep)


async def baike_deal(spider, queue):
    url = await queue.get()

    results = await spider(url)

    title = next(results)
    print(title)

    for ref in next(results):
        try:
            await asyncio.wait_for(queue.put(ref), timeout=QUEUE_TIMEOUT)
        except asyncio.TimeoutError:
            break

    # queue.task_done()


async def spider_loop(deal, *args):
    while True:
        await deal(*args)


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


    async with aiohttp.ClientSession() as session:
        baike_spider = spider_builder(session=session,
                                      url_bulider=baike_url_builder,
                                      xpath_rules=xpath_rules,
                                      headers=headers, params={})

        spider_queue = asyncio.Queue(MAX_URL_NUM)
        await spider_queue.put("/item/数学分析")

        tasks = [spider_loop(baike_deal, baike_spider, spider_queue)
                 for i in range(SPIDER_NUM)]
        await asyncio.gather(*tasks)

asyncio.run(main())

from lxml import html
import requests
import inspect

class CommentExtraction :
    url="http://www.amazon.in/Power-Positive-Thinking-Norman-Vincent/dp/0091906385/ref=pd_sim_14_3?ie=UTF8&dpID=51Kz%2BKyXU9L&dpSrc=sims&preST=_AC_UL160_SR98%2C160_&refRID=1J52MRH904985Z0F3KC4"

    def __init__(self):
        print("Inside Comment Extraction from Amazon")

    def extract_url(self):
        page=requests.get(self.url)
        tree=html.fromstring(page.content)
        hrefs=tree.xpath('//a[@class="a-link-normal"]')
        print(hrefs)
        for href in hrefs:
            print(href)


    def extract(self):
        page=requests.get('http://www.amazon.in/Life-What-Make-Preeti-Shenoy/dp/9380349300?ie=UTF8&redirect=true&ref_=s9_ri_gw_g14_i1_r')
        page=requests.get(page)
        tree = html.fromstring(page.content)
        comments=tree.xpath('//div[@class="a-section"]/text()')
        print(len(comments))
        for index in range(len(comments)):
            comments[index]=comments[index].replace('\n','').replace(',','')
            if comments[index]!='':
                print(str(index)+'. '+comments[index])

    def extract_url_flipkart(self):
        #page=requests.get("http://www.flipkart.com/laptops/asus~brand/pr?sid=6bo%2Cb5g&offer=nb%3Amp%3A05e8151b30&p%5B%5D=facets.filter_standard%255B%255D%3D1&otracker=hp_omu_Deals%20of%20the%20Day_2_9b86a73d-1d6b-4c45-b5f2-6d87c0694e47_0")
        page=requests.get("http://www.flipkart.com/asus-eeebook-x205ta-intel-atom-quad-core-2-gb-windows-10-netbook-90nl0732-m07390/p/itmeegrpgzhzpskw?pid=COMEEGRP7JDTYFGC&al=uD0f1EHKdoBv5VzvmD58CMldugMWZuE75aUsiwTbcEOkGiTTH2JmPS15Z%2FSDQ947MChejDG3wo0%3D&offer=nb%3Amp%3A05e8151b30&ref=L%3A-3459113045341811772&srno=b_1")
        tree=html.fromstring(page.content)
        hrefs=tree.xpath('//div[@class="fk-ui-ccarousel-container"]/div[@class="ccarousel-clip"]/div[@class="ccarousel-wrapper"]/ul[@class="ccarousel"]/li/div/div/div/a')
        for href in hrefs:
            print(href.attrib['href'],href.text_content())

    def extract_flipkart(self):
        page=requests.get("http://www.flipkart.com/top-notch-solid-men-s-henley-purple-grey-t-shirt/p/itmdxyygnxgbzhnh?pid=TSHDXYYGAVHTF2DJ&al=uD0f1EHKdoAA1k%2BlC%2FF1ZcldugMWZuE7wkNiXfq8GiSxNAnbrz%2FQyKusQlEGJ%2BxBA9NRS1O7ddo%3D&offer=nb%3Amp%3A052836df30&ref=L%3A-7814420957783044558&srno=b_1&findingMethod=Deals%20of%20the%20Day&otracker=hp_omu_Deals%20of%20the%20Day_2_2b005d49-c734-4a7f-a5a7-0feff1e33479_0")
        tree=html.fromstring(page.content)
        comment=tree.xpath('//span[@class="review-text"]/text()')
        for index in range(len(comment)):
            comment[index]=comment[index].replace('\t','')
            if comment[index]!='':
                print(str(index)+'. '+comment[index])



comment=CommentExtraction()
comment.extract_url_flipkart()

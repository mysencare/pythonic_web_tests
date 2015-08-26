from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import random

subdomain_file='/Users/tymienieckiarkadiusz/repo/salt-stack-beta/haproxy/templates/subdomain_list.txt'
domain_list = ['showmyhomework.co.uk', 'showmyhomework.com', 'smhwbeta.co.uk', 'smhwfront.co.uk']
#https://selenium-python.readthedocs.org/getting-started.html#walk-through-of-the-example
#https://selenium-python.readthedocs.org/locating-elements.html

#suite = unittest.TestSuite()

class Tests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_frontpage(self):
        for domain in domain_list:
            self.driver.get('http://%(domain)s' % { 'domain': domain })
            try: self.driver.find_element_by_name("ember563")
            except: 
                try: self.driver.find_element_by_name("")
                except:
                    addr = 'http://%(domain)s' % { 'domain': domain }
                    print('sorry dude, cant handle this: %s' % addr)

    def test_subdomains(self):
        subdomains = [line.split() for line in open(subdomain_file, 'r')][0]
        random.shuffle(subdomains)
        subdomains = subdomains[:20]
        for domain in domain_list:
            print('\nlets test random %(sub_nr)s subdomains for %(domain)s' % { 'sub_nr':len(subdomains), 'domain':domain })
            for subd in subdomains:
                self.test_oops(domain=domain, subdomain=subd)

    def test_oops(self, domain='smhw.co.uk', subdomain='www'):
        addr =  'http://%(subdomain)s.%(domain)s' % { 'subdomain': subdomain, 'domain': domain }
        print(addr)
        self.driver.get(addr)
        answer = self.driver.page_source
        self.assertTrue("Oops" or "Oh no" not in answer)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
    #unittest.TextTestRunner().run(suite)
    

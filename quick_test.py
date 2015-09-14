from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import random
import requests
import time
subdomain_file='./subdomain_list.txt'
domain_list = ['showmyhomework.com', 'showmyhomework.co.uk', 'smhwfrontend.co.uk',
               'smhwdev.co.uk', 'smhwbeta.co.uk']

#https://selenium-python.readthedocs.org/getting-started.html#walk-through-of-the-example
#https://selenium-python.readthedocs.org/locating-elements.html
#suite = unittest.TestSuite()



class Tests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.secure = ''


    '''
    def test_sidekiqs(self):
        sq_domains = ['www.smhwdev.co.uk', 'showmyhomework.co.uk', 'smhwfront.co.uk'] 
        for domain in sq_domains:
            self.driver.get('http://%(domain)s/admin/sidekiq/' % { 'domain': domain })
            answer = self.driver.page_source
            self.assertTrue('Oh no' not in answer)

    def test_frontpage(self):
        for domain in domain_list:
            self.driver.get('http://%(domain)s' % { 'domain': domain })
            try: self.driver.find_element_by_name("ember563")
            except: 
                try: self.driver.find_element_by_name("")
                except:
                    addr = 'http://%(domain)s' % { 'domain': domain }
                    print('sorry dude, cant handle this: %s' % addr)

    '''


    def test_all_sites(self):
        subdomains = [line.strip() for line in open(subdomain_file, 'r')]
        random.shuffle(subdomains)
        subdomains = subdomains[:20]
        for domain in domain_list:
            print('\nlets test random %(sub_nr)s subdomains for %(domain)s' %
                { 'sub_nr':len(subdomains), 'domain':domain })
            for subd in subdomains:
                print(subd)
                self.test_subdomains(domain=domain, subdomain=subd)
                sleep 5


    def test_subdomains(self, domain='smhwdev.co.uk', subdomain='www'):
        addr =  'http%(secure)s://%(subdomain)s.%(domain)s' % {
             'secure': self.secure, 'subdomain': subdomain, 'domain': domain }
        print(addr)
        self.driver.get(addr)
        r = requests.get(addr)
        answer = self.driver.page_source
        self.assertTrue("Oh no" not in answer)
        self.assertEqual(r.status_code, 200)


    def test_domains(self, domain='showmyhomework.com'):
        addr =  'http%(secure)s://%(domain)s' % {
                'domain': domain, 'secure': self.secure }
        print(addr)
        self.driver.get(addr)
        r = requests.get(addr)
        answer = self.driver.page_source
        self.assertTrue("Oh no" not in answer)
        self.assertEqual(r.status_code, 200)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
    #unittest.TextTestRunner().run(suite)

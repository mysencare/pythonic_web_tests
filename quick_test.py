from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import random

subdomain_file='/Users/tymienieckiarkadiusz/repo/salt-stack-beta/haproxy/templates/subdomain_list.txt'

class Tests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_subdomains(self):
        subdomains = [line.split() for line in open(subdomain_file, 'r')][0]
        random.shuffle(subdomains)
        subdomains = subdomains[:20]
        print 'lets test random %s subdomains' % len(subdomains)
        for subd in subdomains:
            self.test_oops(subdomain=subd)

    def test_oops(self, subdomain='www'):
        print 'http://%s.smhw.co.uk' % subdomain
        self.driver.get('http://%s.smhw.co.uk' % subdomain)
        assert "Oops" not in self.driver.page_source


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

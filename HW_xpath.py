class MyPage():
    locators = {
        'apple': '//ul[@id="nav"]//a[@href="//allo.ua/ru/aksessuary-apple/"]',
        'tablets, laptops and PC': '//ul[@id="nav"]//a[@href="//allo.ua/ru/planshety-i-gadzhety/"]',
        'headphones and acoustics': '//ul[@id="nav"]//a[@href="//allo.ua/ru/naushniki-i-akustika/"]',
        'TVs, audio and photo': '//ul[@id="nav"]//a[@href="//allo.ua/ru/televizory-i-mediapleery/"]',
        'smartphones and phones': '//ul[@id="nav"]//a[@href="//allo.ua/ru/mobilnye-telefony-i-sredstva-svyazi/"]',
        'xiaomi': '//ul[@id="nav"]//a[@href="//allo.ua/ru/xiaomi-page/"]',
        'gadgets': '//ul[@id="nav"]//a[@href="//allo.ua/ru/gadzhety/"]',
        'appliances': '//ul[@id="nav"]//a[@href="//allo.ua/ru/bytovaya-tehnika/"]',
        'sport': '//ul[@id="nav"]//a[@href="//allo.ua/ru/sport-i-zdorov-e/"]',
        'tourism': '//ul[@id="nav"]//a[@href="//allo.ua/ru/turizm-i-rybalka/"]',
        'sanitary': 'href="//allo.ua/ru/santehnika-i-remont/"',
        'garden': '//ul[@id="nav"]//a[@href="//allo.ua/ru/dom-sad-remont/"]',
        'children': '//ul[@id="nav"]//a[@href="//allo.ua/ru/tovary-dlja-detej/"]',
        'auto products': '//ul[@id="nav"]//a[@href="//allo.ua/ru/avtotovary/"]',
        'perfume': '//ul[@id="nav"]//a[@href="//allo.ua/ru/chasy-i-ukrashenija/"]',
        'actions': '//ul[@id="nav"]//a[@href="//allo.ua/ru/events-and-discounts/"]'

    }

    def test_apple(self):
        a = '//ul[@id="nav"]//a[@href="//allo.ua/ru/aksessuary-apple/"]'
        if self.locators.get('apple') == a:
            print "your xpath is correct"
        else:
            print "your xpath is not correct"

    def test_tv(self):
        b = '//ul[@id="nav"]//a[@href="//allo.ua/ru/televizory-i-mediapleery/"]'
        assert self.locators.get('TVs, audio and photo') == b, "element is not found"

    def test_tablets(self):
        c = '//ul[@id="nav"]//a[@href="//allo.ua/ru/planshety-i-gadzhety/"]'
        assert self.locators.get('tablets, laptops and PC') == c, "element is not found"

    def test_smarts(self):
        d = '//ul[@id="nav"]//a[@href="//allo.ua/ru/mobilnye-telefony-i-sredstva-svyazi/"]'
        assert self.locators.get('smartphones and phones') == d, "element is not found"

    def test_acoustic(self):
        e = '//ul[@id="nav"]//a[@href="//allo.ua/ru/naushniki-i-akustika/"]'
        assert self.locators.get('headphones and acoustics') == e, "element is not found"

    def test_xiaomi(self):
        x = '//ul[@id="nav"]//a[@href="//allo.ua/ru/xiaomi-page/"]'
        assert self.locators.get('xiaomi') == x, "element is not found"

    def test_gadgets(self):
        g = '//ul[@id="nav"]//a[@href="//allo.ua/ru/gadzhety/"]'
        assert self.locators.get('gadgets') == g, "element is not found"

    def test_appliances(self):
        l = '//ul[@id="nav"]//a[@href="//allo.ua/ru/bytovaya-tehnika/"]'
        assert self.locators.get('appliances') == l, "element is not found"

    def test_sport(self):
        s = '//ul[@id="nav"]//a[@href="//allo.ua/ru/sport-i-zdorov-e/"]'
        assert self.locators.get('sport') == s, "element is not found"

    def test_tourism(self):
        t = '//ul[@id="nav"]//a[@href="//allo.ua/ru/turizm-i-rybalka/"]'
        assert self.locators.get('tourism') == t, "element is not found"

    def test_sanitary(self):
        r = 'href="//allo.ua/ru/santehnika-i-remont/"'
        assert self.locators.get('sanitary') == r, "element is not found"

    def test_garden(self):
        k = '//ul[@id="nav"]//a[@href="//allo.ua/ru/dom-sad-remont/"]'
        assert self.locators.get('garden') == k, "element is not found"

    def test_children(self):
        h = '//ul[@id="nav"]//a[@href="//allo.ua/ru/tovary-dlja-detej/"]'
        assert self.locators.get('children') == h, "element is not found"

    def test_auto_products(self):
        p = '//ul[@id="nav"]//a[@href="//allo.ua/ru/avtotovary/"]'
        assert self.locators.get('auto products') == p, "element is not found"

    def test_perfume(self):
        f = '//ul[@id="nav"]//a[@href="//allo.ua/ru/chasy-i-ukrashenija/"]'
        assert self.locators.get('perfume') == f, "element is not found"

    def test_actions(self):
        z = '//ul[@id="nav"]//a[@href="//allo.ua/ru/events-and-discounts/"]'
        assert self.locators.get('actions') == z, "element is not found"



test = MyPage()
print test.test_apple()
print test.test_tv()
print test.test_tablets()
print test.test_smarts()
print test.test_acoustic()
print test.test_xiaomi()
print test.test_gadgets()
print test.test_appliances()
print test.test_sport()
print test.test_tourism()
print test.test_sanitary()
print test.test_garden()
print test.test_children()
print test.test_auto_products()
print test.test_perfume()
print test.test_actions()

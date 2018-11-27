import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class SampleGoogleTest(unittest.TestCase):
    def setUp(self):
        #ブラウザ起動
        self.browser = webdriver.Chrome()
        #5秒停止
        time.sleep(5)
        #画面最大化
        self.browser.maximize_window()
    def tearDown(self):
        self.browser.quit()
    def test_check_google_translate_work_properly(self):
        #Googleアクセス
        self.browser.get("https://www.google.co.jp/")
        #検索窓取得
        input_search = self.browser.find_element_by_xpath("//input[@title='検索']")
        #キーワード入力
        input_search.clear()
        input_search.send_keys('翻訳')
        input_search.submit()
        #一時停止
        time.sleep(5)
        #『Google 翻訳』というリンクをクリック
        link_list = self.browser.find_element_by_link_text("Google 翻訳")
        link_list.click()
        #一時停止
        time.sleep(5)
        #入力のinputを要素名,idから取得し『america』と入力
        input_text = self.browser.find_element_by_xpath("//textarea[@id='source']")
        input_text.send_keys("america")
        #Enterキー(おそらく押さなくても結果は出るが念の為)
        input_text.send_keys(Keys.ENTER)
        #一時停止
        time.sleep(5)
        #出力を要素名,idから取得
        output_text = self.browser.find_element_by_xpath("//span[@id='result_box']/span")
        #出力が想定したものと間違っていないか確認
        self.assertEqual(output_text.text,'アメリカ')


if __name__ == '__main__':
    unittest.main(verbosity=2)
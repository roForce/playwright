# -*- coding: utf-8 -*-
# @Time    : 2023/11/3 21:08
# @Author  : Nickusual
# @mail    : 2843611361@qq.com
# @File    : HuaWeiMobile.py
import datetime
import time
from playwright.sync_api import sync_playwright


def pay():
    with sync_playwright() as playwright:
        context = playwright.chromium.launch_persistent_context(
            user_data_dir='./',
            headless=False,
            slow_mo=500,
            viewport={'width':1920,'height':1080}

        )
        page = context.new_page()
        #设置商品地址
        page.goto("https://www.vmall.com/product/10086692389605.html#2701010093704")
        #点击登录
        if page.locator("#up_loginName").is_hidden():
            page.click("#top-index-loginUrl")
        #检测是否跳转到商品页面，等待两分钟，超过就超时，手动登录操作需要时间
        page.wait_for_selector(selector="#pro-name",timeout=2*60*1000)
        tomorrow = datetime.datetime.combine(datetime.datetime.today(),datetime.time(hour=22,minute=50,second=0))
        print("抢购日期："+tomorrow.strftime("%Y-%m-%d %H:%H:%S.%f"))
        while tomorrow.timestamp() >= datetime.datetime.now().timestamp():
            localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%H:%S.%f")[:-3]
            print(localtime)
            time.sleep(0.1)
        #点击下单按钮
        page.get_by_text("立即下单").click()
        #直接执行JS
        # page.evaluate("rush.business.clickBtnRushBuy2")
        #点击确认下单
        page.locator("#checkoutSubmit").click()
        #等待放置页面退出
        page.wait_for_timeout(10000000)
        page.pause()

if __name__ == "__main__":
    pay()
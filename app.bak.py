# -*- coding: UTF-8 -*-
import os

import time

from alipay import alipay

import qrcode

from PIL import  Image





APPID = 

private_key = 

public_key = 

notify_url = 

ali = alipay(APPID,private_key,public_key,notify_url)

last_money = 0

money = 0


addr = "False"

while 1:
    while 1:
        file_state = open('pay.txt')
        state = int(file_state.read())
        file_state.close()
        print(state)
        if state == 1:
            break

        invoice = str(round(time.time()))
        while money == last_money:
            file_object = open('sum.txt')
            time.sleep(3)
            money = float(file_object.read())
            file_object.close()
            print(money)
        addr = ali.trade_pre_create(invoice, money, '智慧超市', )
        print(addr)
        while addr == "False":
            time.sleep(1)
            addr = ali.trade_pre_create(invoice, money, '智慧超市', )
            print(addr)

        img = qrcode.make(addr['qr_code'])
        img.save("1.png")

        last_money = money

        ans = ali.trade_query(invoice, )
        print (ans)

        while (ans['code']) != '10000':
            current = int(time.time())
            ans = ali.trade_query(invoice, )
            print(ans)
            print(current - int(invoice))
            if (current - int(invoice)) > 100:
                outp = open('ma2.txt', 'w')
                outp.write("1")
                outp.close()
                break
        while (ans['code']) == '10000' and ans[ 'trade_status'] != 'TRADE_SUCCESS':
            current = int(time.time())
            ans = ali.trade_query(invoice, )
            print(ans)
            print(current - int(invoice))
            if (current - int(invoice)) > 100:
                outp = open('ma2.txt', 'w')
                outp.write("1")
                outp.close()
                break
        if (ans['code']) == '10000' and ans[ 'trade_status'] == 'TRADE_SUCCESS':
            outp = open('ma1.txt', 'w')
            outp.write("1")
            outp.close()
            print(ans)

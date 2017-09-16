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

while 1:
    while 1:
        file_is_payment = open("pay.txt")
        payment_state = int(file_is_payment.read())
        file_is_payment.close()
        print(payment_state)
        if payment_state == 1:
            payment_state = 0
            break
    
    invoice_number = str(int(time.time()))
    file_money_summery = open("sum.txt")
    money_summery = float(file_money_summery.read())
    file_money_summery.close()
    print(money_summery)
    
    addr = ali.trade_pre_create(invoice_number, money_summery, '智慧超市', )
    print(addr)
    while addr == "False":
        time.sleep(10)
        addr = ali.trade_pre_create(invoice_number, money_summery, '智慧超市', )
        print(addr)
    
    QR_img = qrcode.make(addr['qr_code'])
    QR_img.save("1.png")
    outp = open('QR.txt', 'w')
    outp.write("1")
    outp.close()
    
    current_payment_state = ali.trade_query(invoice_number, )
    print(current_payment_state)

    while (current_payment_state['code']) != '10000':
        current_time = int(time.time())
        current_payment_state = ali.trade_query(invoice_number, )
        print(current_payment_state)
        print(current_time - int(invoice_number))
        if (current_time - int(invoice_number)) > 100:
            outp = open('ma2.txt', 'w')
            outp.write("1")
            outp.close()
            break
    while (current_payment_state['code']) == '10000' and current_payment_state[ 'trade_status'] != 'TRADE_SUCCESS':
        current_time = int(time.time())
        current_payment_state = ali.trade_query(invoice_number, )
        print(current_payment_state)
        print(current_time - int(invoice_number))
        if (current_time - int(invoice_number)) > 100:
            outp = open('ma2.txt', 'w')
            outp.write("1")
            outp.close()
            break
    if (current_payment_state['code']) == '10000' and current_payment_state[ 'trade_status'] == 'TRADE_SUCCESS':
        outp = open('ma1.txt', 'w')
        outp.write("1")
        outp.close()
        print(current_payment_state)




    

# -*- coding: UTF-8 -*-
import os

import time

from alipay import alipay

import qrcode

from PIL import  Image

APPID = "2017032906469430"

private_key = "-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQC2flDu4ojUYDFy/FL+BvLIU37fShBtqJHcamw8yv4Zqd2YV0oQVIyFf/mT+qlKoJmzKeFMucWV3fp6Z3hrxRmzIksBCm+Q+L/kdewQj/4BAXFGlvWwy2+b4oZSz8lh9Z7+40g90lk1+X+kYyyAMxw+2fBJtjVcLxH9UeVzFuwn2wIDAQABAoGAT/cHpbVz+YNxB46TGyaWSbt0c4kzq6layLeFWBomv74UEIXnOUKjFHhgNzx14/J9hulKBOG+N44+DFa8iJSkToC709vGC50+A18hpzAFjEgd9iRASri4nDy5WLtp/Z0UXN95GOmN2wpqmqujXP1mNjMT2q+opkZO9FiVn6MAUVkCQQDv3mlSgdh0URagcGIdUSwW3tABNH+Ej/+Yt3aL4n2c2tnMGdvYTZZYdAoGc1k6u+leTePDzQ86Y1V7hfYUEA7/AkEAwsQg6JOJlFlCzQOZZQU1STB2gwMpHrFII/8BBa49VNpXtYEf2ftSiIrUwmukrUToRtnEz7DpE8Pty1G2nJMDJQJBAK17l4MT5CAkMZAyF9QKTC/yUFA+zudqWjrynauIUL8sTY9fOHCVlOI+cq29qVBgbeVFwjBv086v3zhqZ9KU1rMCQAkZjMgRDJ6HxR07C9Gyepje0MqyPRuYANzdrziKuYbbZLmwPMK8gVCr2+DxkpId5BRbXFyv0VQBFX0oZjXOkJkCQQCW+Vwx7/nK8kp77LvMqgU/QVDweBhjkIclDcKG3we5XPUpr8yFTQLux9uo8doiPBu2jlmZX4JiRghKvC1/zU+h\n-----END RSA PRIVATE KEY-----"

public_key = "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDDI6d306Q8fIfCOaTXyiUeJHkrIvYISRcc73s3vF1ZT7XN8RNPwJxo8pWaJMmvyTn9N4HQ632qJBVHf8sxHi/fEsraprwCtzvzQETrNRwVxLO5jVmRGi60j8Ue1efIlzPXV9je9mkjzOmdssymZkh2QhUrCmZYI/FCEa3/cNMW0QIDAQAB\n-----END PUBLIC KEY-----"

notify_url = "www.youknowwho.com.cn"

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




    

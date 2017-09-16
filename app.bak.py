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

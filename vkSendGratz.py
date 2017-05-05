# -*- encoding: utf-8 -*-
#!/usr/bin/python
from __future__ import unicode_literals
import pickle
from datetime import datetime, timedelta
import vk
import time
import json

# id of vk.com application
APP_ID = 1234567

https://oauth.vk.com/authorize?client_id=1234567&

def get_saved_auth_params():
    access_token = '450ef6b6741c056d85bb8c79b742d178636f6e23da02ccd59a161598e059d53f641076a84aaa8cc300c21'
    user_id = 395490000
    return access_token, user_id

def get_api(access_token):
    session = vk.Session(access_token=access_token)
    return vk.API(session)

def send_message(api, user_id, message, **kwargs):
    data_dict = {
        'user_id': user_id,
        'message': message,
    }
    data_dict.update(**kwargs)
    return api.messages.send(**data_dict)

def delete_message(api,message_id):
    return api.messages.delete(message_id=message_id)

def main():

    print(str(datetime.now()), '   Script started')
    access_token, _ = get_saved_auth_params()
    api = get_api(access_token)
    now = datetime.strftime(datetime.now(), "%d.%m").lstrip("0").replace(".0", ".")

    gratzToMan = "Поздравляю с днем рождения! Желаю радостных дней, " \
                "согласия и понимания в семье, верных, надежных друзей, благополучия, любви, " \
                "крепко стоять на ногах и уверенно шагать по жизни! Будь стойким и мужественным. " \
                "Всех земных благ! ;-) &#127863;&#127863;&#127863;&#127863;"
    gratzToWoman = "С днем рождения! &#127800; Оставайся всегда такой же красивой, солнечной, " \
                   "нежной и женственной.&#128144; Пускай тебя окружают искренние улыбки, настоящие " \
                   "друзья и атмосфера доброй сказки.&#127799; Пусть работа будет в радость, а жизнь " \
                   "— в удовольствие!&#127863; Будь счастлива, не забывай радоваться и жить на полную катушку! ;-)"

    nowDate = now.split('.', 2)

    

    #получить ID и bdate друзей
    ep = api.friends.get(fields='bdate, sex', name_case='acc')
    countM = 0
    countW = 0
    for all in ep:
        if 'bdate' in all:
            bdate = all['bdate'].split('.', 2)
            #сравниваю дату сегодня и бёздея
            if (bdate[0] == nowDate[0] and bdate[1] == nowDate[1]):
                print('Поздравляю ', all['user_id'], all['first_name'], all['last_name'])
                if all['sex'] == 2: #мальчик
                        #send_message(api, user_id=all['user_id'], message=gratzToMan)
                        time.sleep(1)
                        countM += 1
                else: #девочка
                        #send_message(api, user_id=all['user_id'], message=gratzToWoman)
                        time.sleep(1)
                        countW += 1
    if (countM + countW) == 0:
        print('Сегодня нет дней рождений')
    else:
        print('Сегодня день рождения у ', countM, ' мальчиков и ', countW, ' девочек')
    print(str(datetime.now()), '   Script finished')

main()

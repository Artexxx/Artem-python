import requests
import random
from colorama import Fore, init; init(autoreset=True)

# __________________________________________ Подготовка данных
_phone = input(f'{Fore.CYAN}[*]{Fore.RESET} Телефонный номер >>>')
if _phone[0] == '+':
    _phone = _phone[1:]
if _phone[0] == '8':
    _phone = '7' + _phone[1:]
if _phone[0] == '9':
    _phone = '7' + _phone
_email = ''
for x in range(12):
    _email += random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
# '+7 (777) 777-77-77'
_phoneVodaonline = '+' + _phone[0] + ' (' + _phone[1:4] + ') ' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
# '7(777)777-77-77'
_phoneBukvaprava = _phone[0] + '(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
_name = input(f"{Fore.CYAN}[*]{Fore.RESET}  Ваше имя >>>")
_text = input(f"{Fore.CYAN}[*]{Fore.RESET}  Текст жалобы >>>")
info = f"{Fore.CYAN}Телефон: {Fore.RESET}{_phone}\n" \
       f"{Fore.CYAN}Имя: {Fore.RESET}{_name}\n" \
       f"{Fore.CYAN}Жалоба: {Fore.RESET}{_text}\n\n" \
       f"{Fore.LIGHTCYAN_EX}Спамер запущен.\n" \
       f"Для отмены нажмите {Fore.Green}Ctrl+C"

# ____________________________________________ Проверка Proxy
ipSite = 'http://icanhazip.com'
adress = requests.get(ipSite)
print(f"\n{Fore.CYAN}[*] IP your network:{Fore.RESET} {adress.text}")
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}
try:
    adress = requests.get(ipSite, proxies=proxies)
    print(f"\n{Fore.CYAN}[*] Proxy IP:{Fore.RESET}{adress.text}")
except:
    print(f"{Fore.RED}Stopping connect to the Tor network")
# ____________________________________________ Конец проверки

print(info)
try:
    vodaonline = requests.post('https://www.vodaonline.ru/local/components/shantilab/feedback.form/ajax.php',
                               data={'sessid': '*', 'NAME': _name, 'PHONE': _phoneVodaonline},
                               proxies=proxies)
    if vodaonline.status_code == 200:
        print(Fore.GREEN + 'www.vodaonline.ru: отправлено')
    else:
        print(Fore.RED + 'www.vodaonline.ru: не отправлено')
except:
    print(Fore.RED + 'SERVICE DIED')
try:
    yurmoscow = requests.post('https://yur-moscow.ru/ajax_call_me.php',
                              data={'param1': _phone, 'param3': _text, 'param2': _name},
                              proxies=proxies)
    if yurmoscow.status_code == 200:
        print(Fore.GREEN + 'yur-moscow.ru: отправлено')
    else:
        print(Fore.RED + 'yur-moscow.ru: не отправлено')
except:
    print(Fore.RED + 'Ошибка')
try:
    bukvaprava = requests.post('https://bukvaprava.ru/wp-admin/admin-ajax.php',
                               data={'text_quest_banner': _text, 'name': _name, 'city': 'Москва', 'tel': _phoneBukvaprava, 'ip': '192.168.1.777', 'form_page': 'https://bukvaprava.ru/', 'referer': '', 'action': 'ajax-lead'},
                               proxies=proxies)
    if bukvaprava.status_code == 200:
        print(Fore.GREEN + 'bukvaprava.ru: отправлено')
    else:
        print(Fore.RED + 'bukvaprava.ru: не отправлено')
except:
    print(Fore.RED + 'Ошибка')
try:
    yuristonline = requests.post('https://www.yurist-online.net/lead_question',
                                 data={'region': '27', 'question': _text, 'name': _name, 'phone': _phone, 'email': '', 'partner_id': '13'},
                                 proxies=proxies)
    if yuristonline.status_code == 200:
        print(Fore.GREEN + 'www.yurist-online.net: отправлено')
    else:
        print(Fore.RED + 'www.yurist-online.net: не отправлено')
except:
    print(Fore.RED + 'Ошибка')
try:
    blablabla = requests.post('http://xn----8sbgev0cabfflr7k.xn--p1ai/scripts/form-u22118.php',
                              data={'custom_U22127': _phoneVodaonline}, proxies=proxies)
    if blablabla.status_code == 200:
        print(Fore.GREEN + 'юрист-авгрупп.рф: отправлено')
    else:
        print(Fore.RED + 'юрист-авгрупп.рф: не отправлено')
except:
    print(Fore.RED + 'Ошибка')
try:
    nicecream = requests.post('http://s1.nice-cream.ru/phone-widget2/sendRequest.php',
                              data={'phone': '+' + _phone, 'name': _name, 'sid': '*', 'gclid': '0', 'openstat': 'direct.yandex.ru;12345678;123456789;yandex.ru:premium', 'utm': ''},
                              proxies=proxies)
    if nicecream.status_code == 200:
        print(Fore.GREEN + 'nice-cream.ru: отправлено')
    else:
        print(Fore.RED + 'nice-cream.ru: не отправлено')
except:
    print(Fore.RED + 'Ошибка')
try:
    rossovet = requests.post('https://rossovet.ru/qa/msgsave/save',
                             data={'name': _name, 'comment': _text, 'city': 'Москва', 'phoneprefix': '(' + _phone[1:4] + ')', 'phone': _phone[4:11], 'partnerID': '10', 'ref': 'https://yandex.ru/clck/', 'number1': '7', 'number2': '8', 'checkcode': '15'},
                             proxies=proxies)
    if rossovet.status_code == 200:
        print(Fore.GREEN + 'rossovet.ru: отправлено')
    else:
        print(Fore.RED + 'rossovet.ru: не отправлено')
except:
    print(Fore.RED + 'Ошибка')
try:
    yuridkons = requests.post('https://yuridicheskaya-konsultaciya.com/Home/_FormPost',
                              data={'Name': _name, 'Phone': _phone, 'Description': _text}, proxies=proxies)
    if yuridkons.status_code == 200:
        print(Fore.GREEN + 'yuridicheskaya-konsultaciya.com: отправлено')
    else:
        print(Fore.RED + 'yuridicheskaya-konsultaciya.com: не отправлено')
except:
    print(Fore.RED + 'Ошибка')
try:
    epleads = requests.post('https://epleads.ru/gate/api.php',
                            data={'question': _text, 'region': 'Москва', 'first_last_name': _name, 'phone': _phone, 'ofrid': '1', 'wid': '3', 'presetid': '4', 'referer': 'https://potreb-prava.com/konsultaciya-yurista/konsultaciya-onlajn-yurista-besplatno-kruglosutochno.html', 'ip': '213.154.55.496', 'mobile': '0', 'template': 'form_master.new.fix.metrik_lawyer-blue-default', 'product': 'lawyer', 'userSoftData': '*'},
                            proxies=proxies)
    if epleads.status_code == 200:
        print(Fore.GREEN + 'epleads.ru: отправлено')
    else:
        print(Fore.RED + 'epleads.ru: не отправлено')
except:
    print(Fore.RED + 'Ошибка')
try:
    pravonedv = requests.post('https://pravonedv.ru/proxy_8d34201a5b.php?a___=1',
                              data={'email': _email + '@mail.ru', 'phone': _phoneVodaonline, 'location': 'Москва, Россия', 'name': _name, 'offer': '0', 'ip': '263.87.162.98', 'device': 'desktop', 'token': '*', 'template': 'two_page3', 'referrer': 'https://yandex.ru/clck/', 'domain': 'pravonedv.ru', 'wm_id': '548', 'url': 'https://pravonedv.ru/besplatnye-onlajn-konsultacii-yurista'},
                              proxies=proxies)
    if pravonedv.status_code == 200:
        print(Fore.GREEN + 'pravonedv.ru: отправлено')
    else:
        print(Fore.RED + 'pravonedv.ru: не отправлено')
except:
    print(Fore.RED + 'Ошибка')
try:
    rdftgbhnj = requests.post('https://xn----etbqwledi5fza.xn--p1ai/wp-json/contact-form-7/v1/contact-forms/295/feedback',
                              data={'_wpcf7': '295', '_wpcf7_version': '5.0.5', '_wpcf7_locale': 'ru_RU', '_wpcf7_unit_tag': 'wpcf7-f295-o2', '_wpcf7_container_post': '0', 'text-838': _name, 'tel-231': _phone, 'textarea-472': _text, 'hidden-278': 'Главная'},
                              proxies=proxies)
    if rdftgbhnj.status_code == 200:
        print(Fore.GREEN + 'гос-юристы.рф: отправлено')
    else:
        print(Fore.RED + 'гос-юристы.рф: не отправлено')
except:
    print(Fore.RED + 'Ошибка')
try:
    gurist = requests.post('http://www.gurist.ru/wp-json/contact-form-7/v1/contact-forms/3591/feedback',
                           data={'_wpcf7': '3591', '_wpcf7_version': '5.0', '_wpcf7_locale': 'ru_RU', '_wpcf7_unit_tag': 'wpcf7-f3591-o1', '_wpcf7_container_post': '0', 'your-name': _name, 'tel-147': _text},
                           proxies=proxies)
    if gurist.status_code == 200:
        print(Fore.GREEN + 'gurist.ru: отправлено')
    else:
        print(Fore.RED + 'gurist.ru: не отправлено')
except:
    print(Fore.RED + 'Ошибка')
try:
    beeline = requests.post('https://moskva.beeline.ru/customers/products/mobile/services/createmnporder/',
                            data={'leadName': 'PodborSim', 'phone': _phone[1:11], 'region': '98140'},
                            proxies=proxies)
    if beeline.status_code == 200:
        print(Fore.GREEN + 'moskva.beeline.ru: отправлено')
    else:
        print(Fore.RED + 'moskva.beeline.ru: не отправлено')
except:
    print(Fore.RED + 'Ошибка')
try:
    advokatmakeev = requests.post('https://advokatmakeev.ru/form.php',
                                  data={'oname': _name, 'otel': _phoneVodaonline, 'omail': '', 'omess': _text, 'otype': '1'},
                                  proxies=proxies)
    if advokatmakeev.status_code == 200:
        print(Fore.GREEN + 'advokatmakeev.ru: отправлено')
    else:
        print(Fore.RED + 'advokatmakeev.ru: не отправлено')
except:
    print(Fore.RED + 'Ошибка')
try:
    mkamsk = requests.post('http://mkamsk.ru/apply_auto_form',
                           data={'Form[9]': _name, 'Form[12]': _phone, 'Form[11]': _text, 'url': 'http://mkamsk.ru/', 'check': 'check'},
                           proxies=proxies)
    if mkamsk.status_code == 200:
        print(Fore.GREEN + 'mkamsk.ru: отправлено')
    else:
        print(Fore.RED + 'mkamsk.ru: не отправлено')
except:
    print(Fore.RED + 'Ошибка')
try:
    usachev = requests.post('https://usachev.vip/wp-admin/admin-ajax.php',
                            data={'action': 'bazz_widget_action', 'phone': '+' + _phone, 'name': ''},
                            proxies=proxies)
    if usachev.status_code == 200:
        print(Fore.GREEN + 'usachev.vip: отправлено')
    else:
        print(Fore.RED + 'usachev.vip: не отправлено')
except:
    print(Fore.RED + 'Ошибка')
try:
    pravosfera = requests.post('http://pravo-sfera.ru/auxpage_zayavk/',
                               data={'c_name': _name, 'c_tel': _phoneVodaonline, 'quest': _text, 'uest_go': 'Задать вопрос'},
                               proxies=proxies)
    if pravosfera.status_code == 200:
        print(Fore.GREEN + 'pravo-sfera.ru: отправлено')
    else:
        print(Fore.RED + 'pravo-sfera.ru: не отправлено')
except:
    print(Fore.RED + 'Ошибка')
try:
    uristexpert24 = requests.post('https://urist-expert24.ru/send-lead/',
                                  data={'name': _name, 'phone': _phoneVodaonline, 'form-name': 'Заказ обратного звонка'},
                                  proxies=proxies)
    if uristexpert24.status_code == 200:
        print(Fore.GREEN + 'urist-expert24.ru: отправлено')
    else:
        print(Fore.RED + 'urist-expert24.ru: не отправлено')
except:
    print(Fore.RED + 'Ошибка')
try:
    lawdivorce = requests.post('http://law-divorce.ru/wp-admin/admin-ajax.php',
                               data={'ip_address': '', 'ip_country': '', 'ip_region': '', 'ip_city': '', 'url': '', 'action': 'lld_send_lead', 'text': _text, 'name': _name, 'telephone': '+' + _phoneBukvaprava, 'city': 'Москва'},
                               proxies=proxies)
    if lawdivorce.status_code == 200:
        print(Fore.GREEN + 'law-divorce.ru: отправлено')
    else:
        print(Fore.RED + 'law-divorce.ru: не отправлено')
except:
    print(Fore.RED + 'Ошибка')
try:
    gosurist = requests.post('http://www.gos-urist.ru/send.php', {'name': _name, 'code': _phone[1:4], 'phone': _phone[4:11], 'issue': _text}, proxies=proxies)
    if gosurist.status_code == 200:
        print(Fore.GREEN + 'www.gos-urist.ru: отправлено')
    else:
        print(Fore.RED + 'www.gos-urist.ruчё: не отправлено')
except:
    print(Fore.RED + 'Ошибка')
try:
    ur9911030 = requests.post('http://9911030.ru/orderform.php', {'name': _name, 'phone': _phone, 'message': _text}, proxies=proxies)
    if ur9911030.status_code == 200:
        print(Fore.GREEN + '9911030.ru: отправлено')
    else:
        print(Fore.RED + '9911030.ru: не отправлено')
except:
    print(Fore.RED + 'Ошибка')
try:
    findclone = requests.get('https://findclone.ru/register?phone=+' + _phone, params={'phone': '+' + _phone}, proxies=proxies)
    if findclone.status_code == 200:
        print(Fore.GREEN + 'findclone.ru: отправлено')
    else:
        print(Fore.RED + 'findclone.ru: не отправлено')
except:
    print(Fore.RED + 'Ошибка')

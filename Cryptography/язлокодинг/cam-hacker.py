import requests, re
from colorama import Fore, init;init(autoreset=True)

citi = ['US', 'US', 'JP', 'IT', 'KR', 'FR', 'DE', 'TW', 'RU', 'GB', 'NL', 'CZ', 'TR', 'AT', 'CH', 'ES', 'CA', 'SE',
        'IL', 'PL', 'IR', 'NO', 'RO', 'IN', 'VN', 'BE', 'BR', 'BG', 'ID', 'DK', 'AR', 'MX', 'FI', 'CN', 'CL', 'ZA',
        'SK', 'HU', 'IE', 'EG', 'TH', 'UA', 'RS', 'HK', 'GR', 'PT', 'LV', 'SG', 'IS', 'MY', 'CO', 'TN', 'EE', 'DO',
        'SI', 'EC', 'LT', 'PS', 'NZ', 'BD', 'PA', 'MD', 'NI', 'MT', 'IT', 'SA', 'HR', 'CY', 'PK', 'AE', 'KZ', 'KW',
        'VE', 'GE', 'ME', 'SV', 'LU', 'CW', 'PR', 'CR', 'BY', 'AL', 'LI', 'BA', 'PY', 'PH', 'FO', 'GT', 'NP', 'PE',
        'UY', '-']
count_page = [720, 232, 159, 141, 120, 107, 92, 82, 81, 66, 58, 54, 48, 44, 39, 38, 35, 31, 30, 22, 29, 28, 26, 23, 23,
              23, 21, 16, 16, 13, 13, 23, 13, 13, 11, 11, 11, 11, 10, 11, 10, 10, 7, 8, 7, 6, 7, 7, 6, 6, 6, 6, 5, 6, 5,
              5, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
              16]

print(f"""
{Fore.RED}1){Fore.RESET}United States                {Fore.RED}31){Fore.RESET}Mexico                {Fore.RED}61){Fore.RESET}Moldova
{Fore.RED}2){Fore.RESET}Japan                        {Fore.RED}32){Fore.RESET}Finland               {Fore.RED}62){Fore.RESET}Nicaragua
{Fore.RED}3){Fore.RESET}Italy                        {Fore.RED}33){Fore.RESET}China                 {Fore.RED}63){Fore.RESET}Malta
{Fore.RED}4){Fore.RESET}Korea                        {Fore.RED}34){Fore.RESET}Chile                 {Fore.RED}64){Fore.RESET}Trinidad And Tobago
{Fore.RED}5){Fore.RESET}France                       {Fore.RED}35){Fore.RESET}South Africa          {Fore.RED}65){Fore.RESET}Soudi Arabia
{Fore.RED}6){Fore.RESET}Germany                      {Fore.RED}36){Fore.RESET}Slovakia              {Fore.RED}66){Fore.RESET}Croatia
{Fore.RED}7){Fore.RESET}Taiwan                       {Fore.RED}37){Fore.RESET}Hungary               {Fore.RED}67){Fore.RESET}Cyprus
{Fore.RED}8){Fore.RESET}Russian Federation           {Fore.RED}38){Fore.RESET}Ireland               {Fore.RED}68){Fore.RESET}Pakistan
{Fore.RED}9){Fore.RESET}United Kingdom               {Fore.RED}39){Fore.RESET}Egypt                 {Fore.RED}69){Fore.RESET}United Arab Emirates
{Fore.RED}10){Fore.RESET}Netherlands                 {Fore.RED}40){Fore.RESET}Thailand              {Fore.RED}70){Fore.RESET}Kazakhstan
{Fore.RED}11){Fore.RESET}Czech Republic              {Fore.RED}41){Fore.RESET}Ukraine               {Fore.RED}71){Fore.RESET}Kuwait
{Fore.RED}12){Fore.RESET}Turkey                      {Fore.RED}42){Fore.RESET}Serbia                {Fore.RED}72){Fore.RESET}Venezuela
{Fore.RED}13){Fore.RESET}Austria                     {Fore.RED}43){Fore.RESET}Hong Kong             {Fore.RED}73){Fore.RESET}Georgia
{Fore.RED}14){Fore.RESET}Switzerland                 {Fore.RED}44){Fore.RESET}Greece                {Fore.RED}74){Fore.RESET}Montenegro
{Fore.RED}15){Fore.RESET}Spain                       {Fore.RED}45){Fore.RESET}Portugal              {Fore.RED}75){Fore.RESET}El Salvador
{Fore.RED}16){Fore.RESET}Canada                      {Fore.RED}46){Fore.RESET}Latvia                {Fore.RED}76){Fore.RESET}Luxembourg
{Fore.RED}17){Fore.RESET}Sweden                      {Fore.RED}47){Fore.RESET}Singapore             {Fore.RED}77){Fore.RESET}Curacao
{Fore.RED}18){Fore.RESET}Israel                      {Fore.RED}48){Fore.RESET}Iceland               {Fore.RED}78){Fore.RESET}Puerto Rico
{Fore.RED}19){Fore.RESET}Iran                        {Fore.RED}49){Fore.RESET}Malaysia              {Fore.RED}79){Fore.RESET}Costa Rica
{Fore.RED}20){Fore.RESET}Poland                      {Fore.RED}50){Fore.RESET}Colombia              {Fore.RED}80){Fore.RESET}Belarus
{Fore.RED}21){Fore.RESET}India                       {Fore.RED}51){Fore.RESET}Tunisia               {Fore.RED}81){Fore.RESET}Albania
{Fore.RED}22){Fore.RESET}Norway                      {Fore.RED}52){Fore.RESET}Estonia               {Fore.RED}82){Fore.RESET}Liechtenstein
{Fore.RED}23){Fore.RESET}Romania                     {Fore.RED}53){Fore.RESET}Dominican Republic    {Fore.RED}83){Fore.RESET}Bosnia And Herzegovia
{Fore.RED}24){Fore.RESET}Viet Nam                    {Fore.RED}54){Fore.RESET}Sloveania             {Fore.RED}84){Fore.RESET}Paraguay
{Fore.RED}25){Fore.RESET}Belgium                     {Fore.RED}55){Fore.RESET}Ecuador               {Fore.RED}85){Fore.RESET}Philippines
{Fore.RED}26){Fore.RESET}Brazil                      {Fore.RED}56){Fore.RESET}Lithuania             {Fore.RED}86){Fore.RESET}Faroe Islands
{Fore.RED}27){Fore.RESET}Bulgaria                    {Fore.RED}57){Fore.RESET}Palestinian           {Fore.RED}87){Fore.RESET}Guatemala
{Fore.RED}28){Fore.RESET}Indonesia                   {Fore.RED}58){Fore.RESET}New Zealand           {Fore.RED}88){Fore.RESET}Nepal
{Fore.RED}29){Fore.RESET}Denmark                     {Fore.RED}59){Fore.RESET}Bangladeh             {Fore.RED}89){Fore.RESET}Peru
{Fore.RED}30){Fore.RESET}Argentina                   {Fore.RED}60){Fore.RESET}Panama                {Fore.RED}90){Fore.RESET}Uruguay
                                                        {Fore.RED}91){Fore.RESET}Extra
""")
num = int(input('Number:'))
try:
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}
    for page in range(0, count_page[num]):
        url = (f"https://www.insecam.org/en/bycountry/{citi[num]}/?page={page}")
        res = requests.get(url, headers=headers)
        findip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        count = 0
        for ip in findip:
            print(ip)
except:...

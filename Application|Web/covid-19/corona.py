import requests, sys, re, time, os
from optparse import OptionParser


def banner(help=False, about=False):
    os.system("clear")
    print("""
\u001b[31m .d8888b.                                             8888888b.                           \u001b[0m
\u001b[31md88P  Y88b                                            888   Y88b                          \u001b[0m
\u001b[31m888    888                                            888    888                          \u001b[0m
\u001b[31m888         .d88b.  888d888 .d88b.  88888b.   8888b.  888   d88P 888d888 .d88b.  88888b.  \u001b[0m
\u001b[35m888        d88""88b 888P"  d88""88b 888 "88b     "88b 8888888P"  888P"  d88""88b 888 "88b \u001b[0m
\u001b[35m888    888 888  888 888    888  888 888  888 .d888888 888        888    888  888 888  888 \u001b[0m
\u001b[36mY88b  d88P Y88..88P 888    Y88..88P 888  888 888  888 888        888    Y88..88P 888  888 \u001b[0m
\u001b[36m "Y8888P"   "Y88P"  888     "Y88P"  888  888 "Y888888 888        888     "Y88P"  888  888 \u001b[0m

   \u001b[34mAUTHOR: \u001b[0mArtexx      \u001b[34mVERSION: \u001b[0mTESTING     \u001b[34mCOVID-19 \u001b[0mINFO\n""")
    if help == True:
        print("""
          		\u001b[32mKNOWLEDGE ^_^\u001b[32m
\u001b[31m[+] Command:\u001b[0m
   	python3 corona.py {option}
   	python3 corona.py {country}

\u001b[35m[+] Options:\u001b[0m
   	-s, --save    = save result to file
   	-h, --help    = Help
   	-a, --about   = About
   	-c, --country = show all country list

\u001b[36m[+] Country:\u001b[0m
   	Detect All Country Bro
""")
    if about == True:
        print("""
\u001b[34mAuthor      : \u001b[0mArtexxx
\u001b[34mApp name    : \u001b[0mCovid-19 Pron
\u001b[34mDescription : \u001b[0mshow information corona on all country
\u001b[34mVersion     : \u001b[0mBeta Tester
""")


def get_information(country, save=False, path=None):
    print("[!] Requests Get To URL", end="", flush=True)
    r = requests.get("https://api.kawalcorona.com").text
    print(" -> \u001b[32mSuccess\u001b[0m", end="", flush=True)
    print("\n[!] Getting Information", end="", flush=True)
    get_country = re.findall('"Country_Region":"(.*?)"', r)
    data = '{"OBJECTID":(.*?),"Country_Region":"%s","Last_Update":(.*?),"Lat":(.*?),"Long_":(.*?),"Confirmed":(.*?),"Deaths":(.*?),"Recovered":(.*?),"Active":(.*?)}}' % (
        country)
    cari = re.search(data, r)
    print(" -> \u001b[32mSuccess\u001b[0m")
    last = str(cari.group(2))
    print("\u001b[35m[+] Country: " + country)
    print("\u001b[36m[+] Last Update: " + last)
    print("\u001b[32m[+] Positif Corona: " + str(cari.group(5)), " Orang")
    print("\u001b[31m[+] Deaths : " + str(cari.group(6)), " Orang :(")
    print("\u001b[33m[+] Sembuh Dari Corona: " + str(cari.group(7)), " Orang")
    print("\u001b[32m[+] Active: " + str(cari.group(8)), " Orang\u001b[0m")


def show_list():
    banner()
    try:
        o = open("list.txt", "r").read()
        for a in o.splitlines():
            print("[+] " + str(a))
    except IOError:
        print("[!] Requests Get To URL", end="", flush=True)
        r = requests.get("https://api.kawalcorona.com").text
        print(" -> \u001b[32mSuccess", end="", flush=True)
        print("\n[!] Getting Country\n", end="", flush=True)
        country = re.findall('"Country_Region":"(.*?)"', r)
        for coun in country:
            print("[+] " + str(coun), end="", flush=True)
            buka = open("list.txt", "a")
            buka.write(coun + "\n")
            buka.close()
            print(" -> \u001b[32mSuccess\n", end="", flush=True)


def main():
    save = None
    country = None
    parse = OptionParser(add_help_option=False, epilog="Corona Virus Information")
    parse.add_option("-s", "--save", help="Save Result", dest="save", action="store_false")
    parse.add_option("-h", "--help", help="Show All Commands", dest="help", action="store_true")
    parse.add_option("-a", "--about", help="About", dest="about", action="store_true")
    parse.add_option("-c", "--country", help="Show All Country", dest="country", action="store_true")
    opt, args = parse.parse_args()
    if opt.help == True:
        banner(help=True)
        sys.exit()
    elif opt.about == True:
        banner(about=True)
        sys.exit()
    elif opt.country == True:
        show_list()
    elif opt.save == True:
        try:
            save = args[0]
        except IndexError:
            banner(about=False)
            sys.exit()
    else:
        try:
            country = sys.argv[1]
        except IndexError:
            banner(help=True);
            sys.exit()
    if country:
        banner()
        try:
            o = open("list.txt", "r").read()
            for a in o.splitlines():
                if country.lower() in a.lower():
                    if save:
                        get_information(a, save=True, path=save)
                    else:
                        get_information(a)
                    break
        except IOError:
            print("[+] File List Country \u001b[31mNot Found\u001b[0m, please configure")
            sys.exit()


main()

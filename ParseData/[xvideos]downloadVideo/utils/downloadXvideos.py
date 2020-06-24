import requests, re


def get_link(title, text_raw):
    raw = ''
    reg = r"https://.*(mp4|jpg|m3u8).*'"
    for line in text_raw.splitlines():
        if (line.find(title) != -1):
            raw = line
    matches = re.finditer(reg, raw, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        return (match.group()).strip("""''""")
# demo get_link('html5player.setVideoUrlLow', 'https://www.xvideos.com/video37601777/cumteshots_at_fantasy_fucking_orgy')


def download_xvideos(url=''):
    req = requests.get(url=url)
    text_raw = (req.text).encode('utf-8')
    video_Low = get_link('html5player.setVideoUrlLow', text_raw)
    video_High = get_link('html5player.setVideoUrlHigh', text_raw)
    video_HLS = get_link('html5player.setVideoHLS', text_raw)
    thumb = get_link('html5player.setThumbUrl', text_raw)
    return [video_Low, video_HLS, video_High, thumb]


if __name__ == '__main__':
    print(download_xvideos('https://www.xvideos.com/video37601777/cumteshots_at_fantasy_fucking_orgy'))

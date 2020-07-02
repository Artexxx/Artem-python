import signal
import os
from base64 import b32encode

from flask import Flask, render_template, request, send_file, jsonify

from library import Library, FrictionError

library = Library('/home/artem/Desktop/')

all_hrefs = "<br>".join([f'<a href="./?f={title}">{title}</a>'
                         for (identifier, title) in library.choices.items()])


def request_exit(*a):
    library.delete_caches()
    exit(0)


class FrictionApp(Flask):
    def run(self, *args, **kwargs):
        signal.signal(signal.SIGTERM, request_exit)

        try:
            super().run(*args, **kwargs)
        finally:
            library.delete_caches()


app = FrictionApp(__name__)

"""
Идея: создать json и прочитать его с помощью js
Если id не указан, то скрытый запрос перенаправляется на `/items?f=''` (ищем ничего) ~~>`
  функция Library.chose принимает None и создаёт json по первому попавшемуся `identifier`
  ~~> json парсится JS кодом   
"""
# http://127.0.0.1:4000/?id=...&page=1
@app.route('/')
def viewer():
    return render_template(
        'viewer.html',
        rotation=request.args.get('r', 'n'),
        filter=request.args.get('f', '').strip(),
        rtl=request.args.get('rtl', ''),
        id=request.args.get('id', ''),

        # необходимо только для того, чтобы браузеры не думали, что страница осталась прежней.
        salt=b32encode(os.urandom(2)).decode('utf-8').rstrip('='),  # Пример: '6LIA'
    )


""" Отображает json по конкретному id (папки, файлу)"""
@app.route('/items')
def items():
    identifier = request.args.get('identifier', None)

    if identifier is not None:
        doujin = library.doujin_for(identifier)
    else:
        doujin = library.choice(request.args.get('f', '').strip())

    if doujin is None:
        raise FrictionError(
            "- не смог найти в библиотеке ничего подходящего к твоему фильтру; Попробуй снова.<br><br>" + all_hrefs
        )
    return jsonify(doujin.json())


""" Создано для получения 1 фотографии"""
# http://127.0.0.1:4000/item?id=...&page=1
@app.route('/item')
def item():
    doujin = library.doujin_for(request.args['identifier'])
    return send_file(doujin.pages[int(request.args['page'])])


""" Тут будут отображаться все интересные нам объекты (ZIP|DIR|RAR), для поиска и фильтрации"""
@app.route('/all')  # TODO
def all_items():
    return library.choices


@app.errorhandler(FrictionError)
def error(e):
    response = jsonify({'message': e.message})
    response.status_code = e.status_code
    return response


if __name__ == '__main__':
    app.run(port=5000, debug=True)

<div id="header" align="center">
<h2>Данный сервис реализует следующую задачу:</h2>
</div>
<br>
<p align="justify">
Нужно сделать HTTP сервис для одноразовых секретов наподобие https://onetimesecret.com/.

Он должен позволить создать секрет, задать кодовую фразу для его открытия и cгенерировать код, по которому можно прочитать секрет только один раз. UI не нужен, это должен быть JSON Api сервис.

Метод /generate должен принимать секрет и кодовую фразу и отдавать secret_key по которому этот секрет можно получить.
Метод /secrets/{secret_key} принимает на вход кодовую фразу и отдает секрет.
</p>
<br>

В данном проекте реализовано 2 эндпоинта:


/generate

Данный эндпоинт ожидает POST запрос в формате JSON:

    {
        "code_phrase": "******",      # Здесь необходимо указать фразу для получени доступа к Вашему документу в будущем
        "storage_content": "******"   # Здесь указывается содержимое Вашего документа
    }

В ответ Вам будет отправлен случайный ключ (20 символов) сгенерированный для документа сохраненного в БД:

{"key":"********************"}

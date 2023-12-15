from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE_201 = 'ОК. Папка создана.'
    WRONG_STATUS_CODE_400 = 'Некорректные данные.'
    WRONG_STATUS_CODE_401 = 'Не авторизован.'
    WRONG_STATUS_CODE_403 = 'API недоступно. Ваши файлы занимают больше места, чем у вас есть. Удалите лишнее или увеличьте объём Диска.'
    WRONG_STATUS_CODE_404 = 'Не удалось найти запрошенный ресурс.'
    WRONG_STATUS_CODE_406 = 'Ресурс не может быть представлен в запрошенном формате.'
    WRONG_STATUS_CODE_409 = 'Ресурс "{path}" уже существует.'
    WRONG_STATUS_CODE_413 = 'Загрузка файла недоступна. Файл слишком большой.'
    WRONG_STATUS_CODE_423 = 'Технические работы. Сейчас можно только просматривать и скачивать файлы.'
    WRONG_STATUS_CODE_429 = 'Слишком много запросов.'
    WRONG_STATUS_CODE_503 = 'Сервис временно недоступен.'
    WRONG_STATUS_CODE_507 = 'Недостаточно свободного места.'


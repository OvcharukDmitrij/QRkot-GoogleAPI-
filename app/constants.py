from datetime import datetime

from app.core.config import settings

FORMAT = "%Y/%m/%d %H:%M:%S"

now = datetime.now().strftime(FORMAT)

SHEETS = ('sheets', 'v4')
DRIVE = ('drive', 'v3')

ROW = 100
COLUM = 11

# Шаблон таблицы отчета.
SPREADSHEET_BODY = {
    'properties': {'title': f'Отчет на {now}',
                   'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                               'sheetId': 0,
                               'title': 'Лист1',
                               'gridProperties': {'rowCount': ROW,
                                                  'columnCount': COLUM}}}]
}

# Шаблон для создания прав пользователя.
PERMISSIONS_BODY = {'type': 'user',
                    'role': 'writer',
                    'emailAddress': settings.email,
                    }

# Шаблон для тела таблицы.
TABLE_VALUES = [
    ['Отчет от', now],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание'],
]

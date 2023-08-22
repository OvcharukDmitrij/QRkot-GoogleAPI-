from app.core.config import settings

FORMAT = "%Y/%m/%d %H:%M:%S"

SHEETS = ('sheets', 'v4')
DRIVE = ('drive', 'v3')

ROW = 100
COLUM = 11

# Шаблон таблицы отчета.
SPREADSHEET_BODY = {
    'properties': {'title': 'Отчет на ',
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
    ['Отчет от'],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание'],
]

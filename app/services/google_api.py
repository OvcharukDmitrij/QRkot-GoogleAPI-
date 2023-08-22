from aiogoogle import Aiogoogle

from app.constants import (SPREADSHEET_BODY, PERMISSIONS_BODY, TABLE_VALUES,
                           SHEETS, DRIVE)


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    service = await wrapper_services.discover(*SHEETS)
    spreadsheet_body = SPREADSHEET_BODY
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    spreadsheetid = response['spreadsheetId']
    return spreadsheetid


async def set_user_permissions(
        spreadsheetid: str,
        wrapper_services: Aiogoogle
) -> None:
    permissions_body = PERMISSIONS_BODY
    service = await wrapper_services.discover(*DRIVE)
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheetid,
            json=permissions_body,
            fields="id"
        ))


async def spreadsheets_update_value(
        spreadsheetid: str,
        close_projects: list,
        wrapper_services: Aiogoogle
) -> None:
    service = await wrapper_services.discover(*SHEETS)
    table_values = TABLE_VALUES
    for project in close_projects:
        new_row = [
            str(project['name']),
            str(project['period']),
            str(project['description']),
        ]
        table_values.append(new_row)

    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheetid,
            range=(
                f'R1C1:R{len(table_values)}C{len(max(table_values, key=len))}'
            ),
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )

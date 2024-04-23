from fastapi import APIRouter, HTTPException
from beanie import PydanticObjectId
from typing import List
from ..models.db_models import Teacher, Log, Table, TelegramUser, Page, Statistic
from ..tables.tables_manager import TablesManager
from ..deps import Admin

router = APIRouter()


@router.get("/tables", response_model=List[Table])
async def get_all_tables(admin: Admin):
    return await Table.find_all().to_list()


@router.get("/users", response_model=List[TelegramUser])
async def get_all_users(admin: Admin):
    return await TelegramUser.find_all().to_list()


@router.get("/users/{user_id}", response_model=TelegramUser)
async def get_user(user_id: PydanticObjectId, admin: Admin):
    return await TelegramUser.get(user_id)


@router.get("/tables/{table_id}", response_model=Table)
async def get_table(table_id: PydanticObjectId, admin: Admin):
    return await Table.get(table_id)


@router.get("/logs", response_model=List[Log])
async def get_all_logs(admin: Admin):
    return await Log.find_all().to_list()


@router.get("/logs/{log_id}", response_model=Log)
async def get_log(log_id: PydanticObjectId, admin: Admin):
    return await Log.get(log_id)


@router.get("/teachers", response_model=List[Teacher])
async def get_all_teachers(admin: Admin):
    return await Teacher.find_all().to_list()


@router.get("/statistics", response_model=List[Statistic])
async def get_all_statistics(admin: Admin):
    return await Statistic.find_all().to_list()


@router.get("/teachers/{teacher_id}", response_model=Teacher)
async def get_teacher(teacher_id: PydanticObjectId, admin: Admin):
    return await Teacher.get(teacher_id)


@router.post("/tables", response_model=Table)
async def create_table(table: Table, admin: Admin):
    await table.create()
    TablesManager().add_table(table)
    return table


@router.post("/users", response_model=TelegramUser)
async def create_user(user: TelegramUser):
    query = await TelegramUser.find(TelegramUser.username == user.username).to_list()
    if not query:
        await user.create()
    return user


@router.post("/tables/{table_id}", response_model=Table)
async def create_rule(table_id: PydanticObjectId, page: Page, admin: Admin):
    table = await Table.get(table_id)
    if not table:
        raise HTTPException(
            status_code=404,
            detail="Table not found"
        )
    if table.pages:
        pgs = table.pages
        pgs.append(page)
        await table.set({Table.pages: pgs})
    else:
        pgs = []
        pgs.append(page)
        await table.set({Table.pages: pgs})
    TablesManager().update_table(table)
    return table


@router.post("/teachers", response_model=Teacher)
async def add_teacher(teacher: Teacher, admin: Admin):
    await teacher.create()
    return teacher


@router.post("/statistics", response_model=Statistic)
async def add_statistic(statistic: Statistic, admin: Admin):
    await statistic.insert()
    return statistic


@router.delete("/tables/{table_id}", response_model=Table)
async def delete_table(table_id: PydanticObjectId, admin: Admin):
    table = await Table.get(table_id)
    if not table:
        raise HTTPException(
            status_code=404,
            detail="Table not found"
        )
    await table.delete()
    TablesManager().delete_table(table.id)
    return table


@router.delete("/users/{username}", response_model=TelegramUser)
async def delete_user(username: str):
    query = await TelegramUser.find(TelegramUser.username == username).to_list()
    if not query:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    user = await TelegramUser.get(query[0].id)
    await user.delete()
    return user


@router.delete("/teachers/{teacher_id}", response_model=Teacher)
async def delete_teacher(teacher_id: PydanticObjectId, admin: Admin):
    teacher = await Teacher.get(teacher_id)
    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )
    await teacher.delete()
    return teacher


@router.delete("/tables/{table_id}/{page_id}", response_model=Table)
async def delete_table_rule(table_id: PydanticObjectId, page_id: str, admin: Admin):  # p_id - uuid of page
    table = await Table.get(table_id)
    if not table:
        raise HTTPException(
            status_code=404,
            detail="Table not found"
        )
    pgs = table.pages
    for i in range(len(pgs)):
        if pgs[i].id == page_id:
            pgs.pop(i)
            break
    await table.set({Table.pages: pgs})
    TablesManager().update_table(table)
    return table


@router.put("/tables/{table_id}", response_model=Table)
async def edit_table(table_id: PydanticObjectId, req_table: Table, admin: Admin):
    table = await Table.get(table_id)
    if not table:
        raise HTTPException(
            status_code=404,
            detail="Table not found"
        )
    await table.set({Table.name: req_table.name, Table.table_id: req_table.table_id,
                     Table.provider: req_table.provider, Table.update_frequency: req_table.update_frequency})
    TablesManager().update_table(table)
    return table


@router.put("/users/{user_id}", response_model=TelegramUser)
async def edit_user(user_id: PydanticObjectId, req_user: TelegramUser, admin: Admin):
    user = await TelegramUser.get(user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    await user.set({TelegramUser.username: req_user.username, TelegramUser.chat_id: req_user.chat_id})
    return user


@router.put("/table/{table_id}/{page_id}", response_model=Table)
async def edit_rule(table_id: PydanticObjectId, page_id: str, req_page: Page, admin: Admin):
    table = await Table.get(table_id)
    if not table:
        raise HTTPException(
            status_code=404,
            detail="Table not found"
        )
    pgs = table.pages
    for i in range(len(pgs)):
        if pgs[i].id == page_id:
            pgs[i].name = req_page.name
            pgs[i].teacher_column = req_page.teacher_column
            pgs[i].column1 = req_page.column1
            pgs[i].column2 = req_page.column2
            pgs[i].comparison_operator = req_page.comparison_operator
            pgs[i].notification_text = req_page.notification_text
            break
    await table.set({Table.pages: pgs})
    TablesManager().update_table(table)
    return table


@router.put("/teachers/{teacher_id}", response_model=Teacher)
async def edit_teacher(teacher_id: PydanticObjectId, req_teacher: Teacher, admin: Admin):
    teacher = await Teacher.get(teacher_id)
    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="teacher not found"
        )
    await teacher.set({Teacher.telegram_login: req_teacher.telegram_login, Teacher.names_list: req_teacher.names_list})
    return teacher

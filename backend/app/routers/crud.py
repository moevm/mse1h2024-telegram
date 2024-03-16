from fastapi import APIRouter, HTTPException
from beanie import PydanticObjectId
from typing import List

from models.models import Teacher, Role, Level, Log, Table, Page, Provider
router = APIRouter()

@router.get("/tables/", response_model=List[Table])
async def get_all_tables():
    return await Table.find_all().to_list()

@router.get("/logs/", response_model=List[Log])
async def get_all_logs():
    return await Log.find_all().to_list()

@router.get("/teachers/", response_model=List[Teacher])
async def get_all_teachers():
    return await Teacher.find_all().to_list()

@router.post("/tables/", response_model=Table)
async def create_table(table: Table):
    await table.create()
    return table

@router.post("/tables/{table_id}", response_model=Table)
async def create_rule(id: PydanticObjectId, page: Page):
    table = await Table.get(id) # пока что так
    if not table:
        raise HTTPException(
            status_code=404,
            detail="Table not found"
        )
    pgs = table.pages
    pgs.append(page)
    await table.set({Table.pages : pgs})
    return table

@router.post("/teachers/", response_model=Teacher)
async def add_teacher(teacher: Teacher):
    await teacher.create()
    return teacher

@router.delete("/tables/{table_id}", response_model=Table)
async def delete_table(id: PydanticObjectId):
    table = await Table.get(id)
    if not table:
        raise HTTPException(
            status_code=404,
            detail="Table not found"
        )
    await table.delete()
    return table

@router.delete("/teachers/{teacher_id}", response_model=Teacher)
async def delete_teacher(id: PydanticObjectId):
    teacher = await Table.get(id)
    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )
    await teacher.delete()
    return teacher

@router.delete("/tables/{table_id}/{page_name}", response_model=Table)
async def delete_table_rule(id: PydanticObjectId, name: str):
    table = await Table.get(id) ## пока будет так, устал читать документацию 
    if not table:
        raise HTTPException(
            status_code=404,
            detail="Table not found"
        )
    pgs = table.pages
    for i in range(len(pgs)):
        if pgs[i].name == name:
            pgs.pop(i)
            break
    await table.set({Table.pages : pgs})
    return table

@router.put("/tables/{table_id}/redact", response_model=Table)
async def redact_table(id: PydanticObjectId, name:str, link: str, provider: Provider, timer: int):
    table = await Table.get(id)
    if not table:
        raise HTTPException(
            status_code=404,
            detail="Table not found"
        )
    await table.set({Table.name : name, Table.link : link,
                     Table.provider : provider, Table.update_frequency : timer} )
    return table

@router.put("/table/{table_id}/{page_name}/redact",response_model=Table)
async def redact_rule(id: PydanticObjectId, name:str, new_name:str, t_col: str, columns: List[str], rule:str, text: str):
    table = await Table.get(id) # пока будет так, устал читать документацию 
    if not table:
        raise HTTPException(
            status_code=404,
            detail="Table not found"
        )
    pgs = table.pages
    for i in range(len(pgs)):
        if pgs[i].name == name:
            pgs[i].name = new_name
            pgs[i].teacher_column = t_col
            pgs[i].columns = columns
            pgs[i].rule = rule
            pgs[i].notification_text = text
            break
    await table.set({Table.pages : pgs})
    return table
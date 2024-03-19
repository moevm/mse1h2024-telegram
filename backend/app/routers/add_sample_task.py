from fastapi import APIRouter

from ..schemas.task import TaskInterface

router = APIRouter(
    tags=["add_sample_task"],
    responses={200: {"description": "Successful Response"}},
)


@router.post("/add_sample_task")
async def add_sample_task(task: TaskInterface):
    return {'result': f'Task for {task.chat_id} chat added to queue'}

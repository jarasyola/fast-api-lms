import fastapi

router = fastapi.APIRouter(
    prefix='/courses',
    tags=['Courses']
)

@router.get("/")
async def read_courses():
    return {"courses": []}


@router.post("/")
async def create_course_api():
    return {"courses": []}

@router.get("/:{id}")
async def read_course():
    return {"courses": []}

@router.patch("/:{id}")
async def update_course():
    return {"courses": []}

@router.delete("/:{id}")
async def delete_course():
    return {"courses": []}

@router.get("/:{id}/sections")
async def read_course_sections():
    return {"courses": []}

from database import session_maker
from user.models import User

from sqlalchemy import select


async def set_user(tg_id, username):
    async with session_maker() as session:
        user = await session.scalar(select(User).where(User.id == tg_id, User.username == username))

        if not user:
            session.add(User(id=tg_id, username=username))
            await session.commit()


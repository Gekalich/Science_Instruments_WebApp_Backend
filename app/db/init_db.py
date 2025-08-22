# db/init_db.py
from .session import Base, engine
# сюда импортируешь все модели, чтобы Base “видел” их

from .menu.model import MenuItem
from .user.model import User

Base.metadata.create_all(bind=engine)
print("All tables created!")

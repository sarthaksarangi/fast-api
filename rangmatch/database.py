from sqlmodel import SQLModel, Session, create_engine

DATABASE_URL = "sqlite:///rangmatch.db"

engine = create_engine(DATABASE_URL,echo=True)


def create_tables():
    """Create all tables defined bt SQLModel class"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Dependency that provides a database session per requrest"""
    with Session(engine) as session:
        yield session
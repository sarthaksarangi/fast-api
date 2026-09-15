from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./dabewalla.db"

engine = create_engine(DATABASE_URL, echo=True)

def create_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    """Provides a new database session for each request."""
    with Session(engine) as session:
        yield session
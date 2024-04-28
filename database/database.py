from sqlmodel import Session, create_engine, SQLModel

connect_args = {'check_same_thread': False}

engine = create_engine("sqlite:///players.db", echo=True,
                     connect_args=connect_args)

def createDB():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
from sqlalchemy import create_engine, Column, Integer, String, Float, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Maneira que vimos a conexão com o banco até agora
# engine = create_engine("mysql+pymysql://root:@localhost:3306/contatos")

engine = create_engine("sqlite:///infinity.db",
                       connect_args={'check_same_thread': False})

Base = declarative_base()


# Criação da tabela do banco de dados por meio de uma classe
class Contatos(Base):
    __tablename__ = "contatos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50))
    celular = Column(String(20))
    tag = Column(String(10))
    link = Column(String(10))


# Variavel especifica para pegar as informações do banco de dados
inspetor = inspect(engine)

# Condição para verificar se já existe uma tabela com mesmo nome
if "contatos" not in inspetor.get_table_names():
    Base.metadata.create_all(engine)


Session = sessionmaker(engine)
session = Session()

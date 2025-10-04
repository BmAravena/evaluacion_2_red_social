from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


try:
    cadena_conexion = "mysql+mysqlconnector://root:@localhost:3306/red_social"
    motor_db = create_engine(cadena_conexion)
    Session = sessionmaker(bind=motor_db)

except Exception as e:
    print(f"Error {e}")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


try:
    cadena_conexion = "mysql+mysqlconnector://root:@localhost:3306/red_social"
    motor_db = create_engine(cadena_conexion)
    Session = sessionmaker(bind=motor_db)
    sesion = Session() # Creamos la instancia de Sessión aquí, para que esta sea usada de manera global por todos los negocios y así evitamos problemas al momento de aplicar crud en la base de datos, ya que si creamos varias instancias de Session, cada una tendrá su propio caché y generará problemas al momento de aplicar crud en los datos (cambios no visibles hasta refrescar)

except Exception as e:
    print(f"Error {e}")

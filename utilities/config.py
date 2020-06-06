from sqlalchemy import create_engine

# TODO: Modificar esto para que reciba la información local, la de producción y
# además para que haya uno que no autentique

con ='postgresql://ds4a:L#Nhd4z!=uH@localhost:5432/alcaldia'
engine = create_engine(con)

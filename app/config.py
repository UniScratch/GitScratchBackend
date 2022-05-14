from pydantic import BaseSettings

class Settings(BaseSettings):
    host_address: str = '0.0.0.0'
    host_port: int = 8080
    
    db_host_address: str = 'localhost'
    db_host_port: int = 3306
    db_username: str =''
    db_password: str=''
    db_database_name: str=''
    
        
settings = Settings()
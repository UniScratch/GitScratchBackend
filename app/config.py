from pydantic import BaseSettings

class Settings(BaseSettings):
    host_address: str = '0.0.0.0'
    host_port: int = 8080
    
    db_host_address: str = ''
    db_host_port: int = ''
    db_username: str =''
    db_password: str=''
    db_database_name: str=''
    
        
settings = Settings()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://ibm_cloud_96781ccd_2c3d_4e22_ab0e_dfcbad316c43:e0910426c5bcb8e26139456de648a03644720828ba21bb5e756ca8b4b0f3c2f0@4c16f830-0413-4190-b8a5-33fde6972cc6.blrrvkdw0thh68l98t20.databases.appdomain.cloud:31576/ibmclouddb'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

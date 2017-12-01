import os
from app import create_app
from app.models import Employee, Department, Role

config_name= os.getenv('FLASK_CONFIG')
app=create_app(config_name)

if __name__=='__main__':
    app.run()
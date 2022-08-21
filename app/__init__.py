
from flask import Flask

class Server:

    def __init__(self) -> None:
        self.app = Flask(__name__)

        from .auth import auth_blueprint
        self.app.register_blueprint(auth_blueprint)
    
    def run(self, host: str = '0.0.0.0', port: str = 5000):
        self.app.run(host=host, port=port)
    
    def show_config(self):
        print(self.app.config)


    
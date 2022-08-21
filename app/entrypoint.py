
from app import Server

def entrypoint():
    server: Server = Server()
    server.run()


if __name__ == '__main__':
    entrypoint()

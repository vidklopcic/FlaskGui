from gui import app


class MainApplication():
    def __init__(self):
        pass


if __name__ == '__main__':
    instance = MainApplication()
    app.config['instance'] = instance
    app.run('localhost', 80)
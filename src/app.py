class App:
    def __init__(self):
        self.name = 'Outdated Test App 2'
        self.version = '1.0.0'
    
    def run(self):
        print(f'Running {self.name} v{self.version}')
        return True
    
    def get_info(self):
        return {
            'name': self.name,
            'version': self.version
        }

def main():
    app = App()
    return app.run()

if __name__ == '__main__':
    main()
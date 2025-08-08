class App:
    def __init__(self):
        self.name = 'Outdated Test App 2 - UPDATED'
        self.version = '2.0.0'
        self.features = ['basic', 'advanced']
    
    def run(self):
        print(f'Running {self.name} v{self.version}')
        self.new_feature()
        return True
    
    def get_info(self):
        return {
            'name': self.name,
            'version': self.version,
            'features': self.features
        }
    
    def new_feature(self):
        print('New feature added to simulate outdated state')
        return 'feature_added'
    
    def process_data(self, data):
        # New method to process data
        return [item * 2 for item in data]

def main():
    app = App()
    return app.run()

if __name__ == '__main__':
    main()

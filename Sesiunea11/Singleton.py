'''
Singleton - is a creational design pattern that lets you ensure that a class has only one instance
while provides a global access point to this instance.
'''


class SingletonLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print('Creating the SingletonLogger object...')
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, file_name):
        if hasattr(self._instance,'file_name'):
            return
        self.file_name = file_name


logger = SingletonLogger('hello.txt')
print(logger.file_name)
logger2 = SingletonLogger('hello2.txt')
print(logger2.file_name)
print(logger)
print(logger2)


'''
Pros:
    * You can be sure that a class has a single instance
    * You can gain a global access point to that instance
    * The singleton object is initialised only when it's requested for the first time
  
Cons:
    * The singleton pattern can mask bad design, for instance: when the components of
    the program knows too much about each other 
'''
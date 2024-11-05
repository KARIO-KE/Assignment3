class Engine:
    def __init__(self, model):
        self.model = model
        self.is_running = False
    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"Engine {self.model} started.")
        else:
            print("Engine is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"Engine {self.model} stopped.")
        else:
            print("Engine is already stopped.")
class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

    def start_car(self):
        print(f"Starting the {self.make} {self.model}...")
        self.engine.start()

    def stop_car(self):
        print(f"Stopping the {self.make} {self.model}...")
        self.engine.stop()
my_engine = Engine("V6")
my_car = Car("mazda", "CX5", my_engine)
my_car.start_car()
my_car.stop_car()

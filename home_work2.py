class Car:                                                                          
    """Клас автомобіля."""                                                          
                                                                                    
    num_wheels = 4  # классовое поле                                                
                                                                                    
    def __init__(self, make, model, year, weight):                                  
        """Ініціалізація атрибуту машини."""                                        
        self.make = make                                                            
        self.model = model                                                          
        self.year = year                                                            
        self.weight = weight                                                        
        self.is_running = False                                                     
                                                                                    
    def start(self):                                                                
        """Завести автомобіль."""                                                   
        if not self.is_running:                                                     
            self.is_running = True                                                  
            print(f"The {self.make} {self.model} is now running.")                  
                                                                                    
    def stop(self):                                                                 
        """Зупинити автомобіль."""                                                  
        if self.is_running:                                                         
            self.is_running = False                                                 
            print(f"The {self.make} {self.model} has been stopped.")                
                                                                                    
class Driver:                                                                       
    """Клас водія."""                                                               
                                                                                    
    def __init__(self, name, age, driving_experience):                              
        """Ініціалізуємо атрибут водія."""                                          
        self.name = name                                                            
        self.age = age                                                              
        self.driving_experience = driving_experience                                
                                                                                    
    def start_car(self, car):                                                       
        """Завезсти авто."""                                                        
        car.start()                                                                 
                                                                                    
    def stop_car(self, car):                                                        
        """Зупинити авто."""                                                        
        car.stop()                                                                  
                                                                                    
# Створюєме екземпляри класів                                                       
car1 = Car("Toyota", "Corolla", 2022, 1200)                                         
car2 = Car("Honda", "Accord", 2022, 1400)                                           
driver1 = Driver("John", 30, 10)                                                    
driver2 = Driver("Anna", 25, 5)                                                     
                                                                                    
# Взаємодія з об'єктами                                                             
driver1.start_car(car1)                                                             
driver2.start_car(car2)                                                             
driver1.stop_car(car1)                                                              
driver2.stop_car(car2)                                                              
                                                                                    

class SmartHome:
    def __init__(self):
        self.lights_on = False
        self.temperature = 22
        self.security_enabled = True
    
    def toggle_lights(self):
        # Переключи свет (если был выключен - включи, и наоборот)
        self.lights_on = not self.lights_on
        state = "включен" if self.lights_on else "выключен"
        print(f"Свет {state}")
    
    def set_temperature(self, new_temp):
        # Установи температуру в диапазоне 15-30
        if 15 <= new_temp <= 30:
            old_temp = self.temperature
            self.temperature = new_temp
            print(f"Температура изменена: {old_temp}°C -> {new_temp}°C")
        else:
            print(f"Температура {new_temp}°C вне диапазона 15-30°C")
    
    def toggle_security(self):
        # Переключи охрану
        self.security_enabled = not self.security_enabled
        state = "включена" if self.security_enabled else "выключена"
        print(f"Охрана {state}")
    
    def away_mode(self):
        # Режим "никого нет дома"
        print("Активирован режим 'Никого нет дома'")
        self.lights_on = False
        self.set_temperature(18)
        self.security_enabled = True
    
    def home_mode(self):
        # Режим "дома есть люди"
        print("Активирован режим 'Дома есть люди'")
        self.lights_on = True
        self.set_temperature(22)
        self.security_enabled = False
    
    def status(self):
        # Покажи состояние дома
        lights = "включен" if self.lights_on else "выключен"
        security = "включена" if self.security_enabled else "выключена"
        return (f"Состояние умного дома:\n"
                f"  Свет: {lights}\n"
                f"  Температура: {self.temperature}°C\n"
                f"  Охрана: {security}")

# Тестируем
home = SmartHome()
print("Начальное состояние:")
print(home.status())

print("\n--- Тестируем методы ---")
home.toggle_lights()
home.set_temperature(25)
home.toggle_security()
print(home.status())

print("\n--- Режим 'Никого нет дома' ---")
home.away_mode()
print(home.status())

print("\n--- Режим 'Дома есть люди' ---")
home.home_mode()
print(home.status())

print("\n--- Пробуем некорректную температуру ---")
home.set_temperature(10)
home.set_temperature(35)
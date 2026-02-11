# """
# ЗАДАЧА: Создай класс SmartHome (Умный дом)

# 1. В __init__ создай атрибуты:
#    - lights_on = False (свет выключен)
#    - temperature = 22 (температура)
#    - security_enabled = True (охрана включена)
# 2. Создай методы toggle_lights() - включает свет если он выключен и выключает если включен
# 3. Создай метод set_temperature(new_temp) - устанавливает температуру (разререшно выставлять только в пределах 15-30 градусов)
# 4. Создай метод toggle_security() - включает охрану если она выключена и выключает если включена
# 5. Создай метод away_mode() - выключает свет, ставит температуру 18, включает охрану
# 6. Создай метод home_mode() - включает свет, ставит температуру 22, выключает охрану
# 7. Создай метод status() - показывает состояние дома

# Добавляй логгирование (print) в каждый метод. Протестируй все режимы.
# """

class SmartHome:
   def __init__(self):
      self.lights_on = False
      self.temperature = 22
      self.security_enabled = True
   
   def toggle_lights(self):
      if self.lights_on == False:
          self.lights_on == True
          print(f'Свет был выключен,включили')
      else:
         self.lights_on == False
      print(f'Свет был включен,выключили')
   
   def set_temperature(self,new_temp):
      if new_temp in range(15,31):
         print(f'Температура {new_temp}')
      else:
         print('Недопустимая температура')
   
   def toggle_security(self):
      security_status = "Выключили охрану" if self.security_enabled else "Включили охрану"
      print(security_status)

   def away_mode(self):
      self.lights_on = False
      self.temperature = 18
      self.security_enabled = True
      # light_status = 'Свет мегавключен' if self.lights_on else 'Свет мегавыключен'
      # security_status = 'Охрана включена' if self.security_enabled else 'Охрана отключена'
      print(f'Статус: {self.light_status()}, Температура: {self.temperature}, Статус охраны {self.security_status()}')

   def light_status(self):
      return 'Свет MEGA включен' if self.lights_on else 'Свет выключен'

   def security_status(self):
      return 'Охрана включена' if self.security_enabled else 'Охрана отключена'

   def home_mode(self):
      self.lights_on = True
      self.temperature = 22
      self.security_enabled = False
      # light_status = 'Свет включен' if self.lights_on else 'Свет выключен'
      # security_status = 'Охрана включена' if self.security_enabled else 'Охрана отключена'
      print(f'Статус: {self.light_status()}, Температура: {self.temperature}, Статус охраны {self.security_status()}')
   
   def status(self):
      pass
      

   


smarthome= SmartHome()
smarthome.toggle_lights()
smarthome.set_temperature(10)
smarthome.toggle_security()
smarthome.away_mode()
smarthome.home_mode()
smarthome.status()

        
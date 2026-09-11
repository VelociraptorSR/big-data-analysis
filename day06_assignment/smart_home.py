'''
Smart Home Appliance Control
Scenario
You are designing a control model for a smart home thermostat. The target temperature must be guarded against invalid bounds 
(e.g., set too high or too low, causing damage or excessive energy usage).

Problem Description
Create a class named SmartThermostat that implements the following specifications:

Class-level Constant Variables:
MIN_TEMP = 10.0 (float)
MAX_TEMP = 35.0 (float)
Constructor (__init__):
Accepts parameters: appliance_name (string) and initial_temp (float).
Sets a private attribute __appliance_name (assigned from appliance_name).
Sets a private attribute __target_temp (float). Call the setter property inside the constructor or perform checks to ensure 
that if the initial_temp is out of the [MIN_TEMP, MAX_TEMP] bounds, it defaults to 22.0.
Properties:
target_temp (read-write property):
Getter: Returns the value of __target_temp.
Setter: Checks if the new temperature is within the range [MIN_TEMP, MAX_TEMP] inclusive. If valid, updates __target_temp. 
If invalid, raises a ValueError with message: "Temperature must be between 10.0 and 35.0 degrees."
appliance_name (read-only property):
Getter: Returns __appliance_name.
(No setter defined, making it read-only after creation).
Example Walkthrough
thermostat = SmartThermostat("Living Room AC", 24.0)
print(thermostat.appliance_name)  # Output: Living Room AC
print(thermostat.target_temp)     # Output: 24.0

thermostat.target_temp = 28.0     # Updates successfully
print(thermostat.target_temp)     # Output: 28.0

try:
    thermostat.target_temp = 5.0  # Out of range!
except ValueError as e:
    print(e)  # Output: Temperature must be between 10.0 and 35.0 degrees.
'''

class SmartThermostat():
    MIN_TEMP = 10.0
    MAX_TEMP = 35.0
    def __init__(self,appliance_name,initial_temp = 22.0):
        self.__appliance_name = appliance_name
        self.target_temp = initial_temp
        
    @property
    def appliance_name(self):
        return self.__appliance_name
    
    @property
    def target_temp(self):
        return self.__target_temp
    
    @target_temp.setter
    def target_temp(self, initial_temp):
        try:
            if initial_temp > SmartThermostat.MIN_TEMP and initial_temp < SmartThermostat.MAX_TEMP:
                self.__target_temp = initial_temp
                return self.__target_temp
            else:
                self.__target_temp = 22.0
                raise ValueError("Temperature must be between 10.0 and 35.0 degrees.")
        except ValueError as e:
            print(e)     
            
if __name__ == "__main__":
    thermostat = SmartThermostat("Living Room AC", 5.0)
    print(thermostat.appliance_name)  
    print(thermostat.target_temp)
    
    thermostat.target_temp = 56.0     # Updates successfully
    print(thermostat.target_temp)
    
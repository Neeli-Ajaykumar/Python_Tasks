"""Smart Home Devices (Multiple Inheritance) 
A smart home device may have both WiFi connectivity and Voice control features. 
Create classes WiFiDevice and VoiceAssistant, and a class SmartSpeaker that 
inherits from both using multiple inheritance. """

class WiFiDevice:
    def __init__(self, wifi_name):
        self.wifi_name = wifi_name

    def connect_wifi(self):
        print("Connecting to WiFi network '" + self.wifi_name)

class VoiceAssistant:
    def __init__(self, assistant_name):
        self.assistant_name = assistant_name

    def activate_voice(self):
        print(self.assistant_name + " voice assistant is now active.")

class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def __init__(self, wifi_name, assistant_name, brand):
        WiFiDevice.__init__(self, wifi_name)
        VoiceAssistant.__init__(self, assistant_name)
        self.brand = brand

    def show_details(self):
        print("Smart Speaker Brand: " + self.brand)
        self.connect_wifi()
        self.activate_voice()

speaker = SmartSpeaker("Excitel-AK(5G)", "Alexa", "Redmi")
speaker.show_details()

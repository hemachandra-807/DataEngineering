class MusicPlayer:
    def play_music(self):
        print("Playing music...")

class Camera:
    def take_picture(self):
        print("Taking a picture...")


class SmartPhone(MusicPlayer, Camera):
    def make_call(self):
        print("Making a phone call...")


phone = SmartPhone()

phone.play_music()      
phone.take_picture()    
phone.make_call()        

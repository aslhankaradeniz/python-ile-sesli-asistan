
import pyttsx3
engine = pyttsx3.init()#engine değişkenindeki ifadeyi değişik özellikler ekleyebileceğiz
"""
voices = engine.getProperty('voices') #erkek sesine dönüştürüyor
engine.setProperty('voice', voices[1].id)
engine.say(" i love you ")#yapıyı sesli okutacağız

"""

soyle=input("lütfen sesi okunmasını istediğiniz metni giriniz : ")
engine.say(soyle)
engine.runAndWait()#çalış ve bekle

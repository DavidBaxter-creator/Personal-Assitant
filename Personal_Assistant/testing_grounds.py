import pyjokes
from Voice_engine import speak
joke = pyjokes.get_joke()
print(joke)
speak(joke)


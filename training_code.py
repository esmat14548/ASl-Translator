import functions_model
from gtts import gTTS
sign_name = str(input("enter the sign name "))
num_of_shots = int(input("enter the number of shots "))
functions_model.save_sign(sign_name, num_of_shots)
sound = gTTS(sign_name, "co.in", 'en', False)
sound.save(f"sounds/{sign_name}.mp3")

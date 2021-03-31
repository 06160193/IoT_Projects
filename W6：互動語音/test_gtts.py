from gtts import gTTS
import os
import numpy as np

RMath = int(np.random.random()*100)
if RMath>50:
    tts=gTTS(text='Continue Back~'+'You have'+str(RMath)+'centimeter', lang='en')
    
elif RMath > 30:
    tts=gTTS(text='Be careful。'+'You have'+str(RMath)+'centimeter', lang='en')    
elif RMath > 10:
    tts=gTTS(text='Warning!'+'You have'+str(RMath)+'centimeter', lang='en')    
else :
    tts=gTTS(text='Stop!'+'You have'+str(RMath)+'centimeter', lang='en')    
print(RMath)

tts.save("test_gtts.mp3")
os.system("mpg321 test_gtts.mp3")

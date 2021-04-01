# W6
## Install WM8960 from seeed‐linux‐dtoverlays
https://wiki.seeedstudio.com/ReSpeaker_2_Mics_Pi_HAT/  
列出目前可record的音訊裝置`$ arecord -l`  
錄音(mono, stereo)
```
$ arecord ‐d 3 ‐f dat ‐c 1 mono.wav
$ arecord ‐d 3 ‐f dat stereo.wav
```
列出目前可playback的音訊裝置`$ aplay ‐l`  
播放音訊`$ aplay stereo.wav`  
使用alsamixer控制音量`$ alsamixer`  
## espeak
安裝`$ sudo apt install espeak`  
測試
```
$ espeak ‐‐stdout "hello world" | aplay
$ espeak ‐‐stdout ‐vzh "你好" | aplay
$ espeak ‐‐stdout ‐f hello.txt | aplay
```  
## Google Assistant SDK
安裝
```
$ sudo pip3 install gTTS
$ sudo apt‐get install ‐y mpg321
```
測試：建立一個test_gtts.py檔案
```
from gtts import gTTS
import os
tts=gTTS(text=‘測試文字轉語音’, lang=‘zh‐tw’)
tts.save(“test.mp3”)
os.system("mpg321 test.mp3")
```

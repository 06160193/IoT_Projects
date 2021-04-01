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

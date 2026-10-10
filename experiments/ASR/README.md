\# ASR Experiment



This experiment evaluates the speech recognition performance of different Automatic Speech Recognition (ASR) approaches used during the development of the Wireless AI Smart Hat.



\## Compared Methods



\- Google Speech Recognition

\- Vosk

\- Whisper tiny



\## Test Data



A total of 30 speech audio samples were used for comparison.



\## Evaluation Purpose



The experiment compares the recognition performance of different speech recognition methods and evaluates their suitability for deployment on the Raspberry Pi-based smart hat.



Whisper tiny was selected as the final ASR model because it provides offline speech recognition and is suitable for edge-device deployment through whisper.cpp.



\## Final Implementation



The final system uses:



\- Whisper tiny

\- whisper.cpp

\- 16 kHz audio input



The integrated implementation is available in:



`../../src/Integrated\_System/vistra\_main.py`


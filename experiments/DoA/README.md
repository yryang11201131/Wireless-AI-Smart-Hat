\# DoA Experiment



This experiment evaluates sound-source direction estimation using the ReSpeaker USB microphone array.



\## Evaluation Purpose



The Direction of Arrival (DoA) module estimates the incoming sound angle and converts it into simplified direction information for the user.



The original microphone array provides angular direction information.



For the final wearable system, the direction information is simplified into:



\- Front

\- Left

\- Right



This simplified representation is used to provide intuitive visual direction cues through LED indicators.



\## Related Module



Standalone DoA test:



`../../src/DoA/doa\_test.py`



Integrated system:



`../../src/Integrated\_System/vistra\_main.py`


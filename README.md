# Indian-Railway-Announcement-system

### Prerequisite: The prerequisite of this project is the basic knowledge of python.

### How it works and get the output?
- For creating railway announcement software, we will be using a bunch of modules like **pyaudio**, **pydub**, and **gTTS** to process audio and get the announcing status of thousands of trains. By using **PyAudio** module, we can easily use Python to play and record audio on a variety of platforms. **Pydub** is a simple and well-designed Python module for audio manipulation and **gTTS** (which stands for Google Text-to-Speech) is a Python library and CLI tool to interface with Google Translate text-to-speech API.

- In which we are adding the **train name** , **train no.** , **platform no.**,etc into the [announcement.xlsx][identifier] and this excel file pass into the [main.py][idetifier2] file and this python code is generate the announcement for each and every train which are present in the [announcement.xlsx][identifier] file.

- After successfully Running this [main.py][idetifier2] python script it generate the all train's audio file inform of **announcement_Train-no.mp3** (Audio) files. 

[identifier]:https://github.com/Datastar07/Railway-Announcement-system/blob/main/annoucment.xlsx
[idetifier2]:https://github.com/Datastar07/Railway-Announcement-system/blob/main/main.py

### Installation ⚙️:
**Dependancies**
- 1. Python >= 3.6
- 2. pyaudio == 0.2.13
- 3. pydub == 0.25.1
- 4. gTTS == 2.3.2
- ⚠️ : If in above any dependacies is not install in your machine so try to directly download the .whl file of dependancies and then try it.

### Installing Dependancies!
Installing the pyaudio,pydub,gTTS
```javascript
pip install pyaudio==0.2.13
pip install pydub==0.25.1
pip install gTTS==2.3.2
```

### ⚠️ Note :
In Which take care of our .mp3 file is may not be corrupted.Because if MP3 file is corrupted so our main.py file through an error and code not work properly so take care about that things.

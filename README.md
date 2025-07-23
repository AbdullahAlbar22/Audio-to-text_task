# Audio-to-text_task
Audio_Text_Interaction_Project
This project demonstrates a complete pipeline for processing audio input, generating an intelligent response using a language model, and converting the response back to audio output.

Task_Description:

The main goal of this project is to:

-Capture audio input from the user and convert it into text using speech recognition.

-Generate a relevant text response using an advanced language model (LLM) such as Cohere.

-Convert the generated text response into speech and play it back to the user.


Used_Libraries:

The following libraries and tools were used in this project:


-vosk: For offline speech recognition to convert audio input to text.

-sounddevice: To record audio input from the user’s microphone.

-cohere: To generate AI-based responses from the converted text input.

-gtts: To convert the text response into audio (speech synthesis).

-pygame: To play the generated audio response.

-Anaconda: For managing the project environment.

-Visual Studio Code: As the main development environment._

How_It_Works:

The user speaks into the microphone. The system records the audio and transcribes it using Vosk. The transcribed text is sent to the Cohere language model to generate a response. The response is then synthesized to speech using gTTS and played back using pygame.

Requirements:

• Python installed through Anaconda
• All required libraries installed via pip or conda
• Internet connection for Cohere API and gTTS

Author:

Developed by: [Abdullah Sharaf Albar]


Note: I used vosk small english model for this task

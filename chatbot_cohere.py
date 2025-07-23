import queue
import sounddevice as sd
import vosk
import sys
import json
import cohere
from gtts import gTTS
import pygame
import time
import os

# ======== Config =========
cohere_api_key = ""  # ← استبدل هذا بمفتاحك من cohere
model_path = "vosk-model-small-en-us-0.15"

# ======== Initialize ========
q = queue.Queue()

# Load Vosk model
vosk.SetLogLevel(-1)
model = vosk.Model(model_path)
samplerate = 16000
device = None  # Use default input device

# ✅ دالة التحدث باستخدام gTTS و pygame
def speak(text):
    print(f"\n🤖 Bot: {text}\n")

    tts = gTTS(text=text, lang='en')
    filename = os.path.join(os.getcwd(), "response.mp3")
    tts.save(filename)

    # 🔄 انتظر حتى يتم إنشاء الملف فعلًا
    while not os.path.exists(filename):
        time.sleep(0.1)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.quit()
    os.remove(filename)

# تسجيل الصوت من المايكروفون
def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

# التعرف على الكلام باستخدام Vosk
def listen():
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device,
                           dtype="int16", channels=1, callback=callback):
        print("🎤 Speak your question (say 'exit' or 'stop' to quit)...")
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                return text.strip()

# إرسال الطلب لـ Cohere والحصول على الرد
def get_cohere_response(text):
    co = cohere.Client(cohere_api_key)
    try:
        response = co.generate(
            model="command",
            prompt=text,
            max_tokens=50 
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# حلقة التشغيل الرئيسية
def chatbot_loop():
    while True:
        text = listen()
        if not text:
            continue

        print(f"🗣️ You said: '{text}'")

        if text.lower() in ["exit", "stop", "quit"]:
            speak("Goodbye!")
            break

        response = get_cohere_response(text)
        speak(response)

# ======== Run Program ========
if __name__ == "__main__":
    chatbot_loop()
#!/usr/bin/env python3


import pygame
import gtts

def text_to_speech(text, language='en', speed='normal'):

  # Create a gTTS object.
  tts = gtts.gTTS(text, lang=language, slow=False if speed == 'normal' else True)

  # Save the audio file.
  audio_file = 'Audio/speech/' + text + '.mp3'
  tts.save(audio_file)

  return audio_file


def txt_speech(audio_file):
  pygame.init()
    
  pygame.mixer.music.load('Audio/speech/' + audio_file + '.mp3')
    
  pygame.mixer.music.play()

msg = 'finished'
text_to_speech(msg)
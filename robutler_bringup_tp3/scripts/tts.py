import pygame
import gtts

def text_to_speech(text, language='en', speed='normal'):

  # Create a gTTS object.
  tts = gtts.gTTS(text, lang=language, slow=False if speed == 'normal' else True, tld='ca')

  # Save the audio file.
  audio_file = '/home/luis/catkin_ws/src/PSR_Trabalho3/robutler_bringup_tp3/lib/Audio' + text + '.mp3'
  tts.save(audio_file)

  return audio_file


def txt_speech(audio_file):
  pygame.init()
    
  pygame.mixer.music.load('/home/luis/catkin_ws/src/PSR_Trabalho3/robutler_bringup_tp3/lib/Audio' + audio_file + '.mp3')
    
  pygame.mixer.music.play()


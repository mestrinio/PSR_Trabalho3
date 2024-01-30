from playsound import playsound

def play(sound):
    if sound == 'foto':
        playsound('/home/luis/catkin_ws/src/PSR_Trabalho3/robutler_bringup_tp3/lib/sound/foto.mp3')
    elif sound == 'drag':
        playsound('/home/luis/catkin_ws/src/PSR_Trabalho3/robutler_bringup_tp3/lib/sound/drag.mp3')
    elif sound == 'drift':
        playsound('/home/luis/catkin_ws/src/PSR_Trabalho3/robutler_bringup_tp3/lib/sound/drift.mp3')
    elif sound == 'thunder':
        playsound('/home/luis/catkin_ws/src/PSR_Trabalho3/robutler_bringup_tp3/lib/sound/thunder.mp3')
    elif sound == 'aceleracao':
        playsound('/home/luis/catkin_ws/src/PSR_Trabalho3/robutler_bringup_tp3/lib/sound/burnout.mp3')
    elif sound == 'drag_curto':
        playsound('/home/luis/catkin_ws/src/PSR_Trabalho3/robutler_bringup_tp3/lib/sound/som1.mp3')
    elif sound == 'drift_curto':
        playsound('/home/luis/catkin_ws/src/PSR_Trabalho3/robutler_bringup_tp3/lib/sound/som2.mp3')

    else:
        print('ERRO A REPRODUZIR FICHEIRO DE AUDIO')
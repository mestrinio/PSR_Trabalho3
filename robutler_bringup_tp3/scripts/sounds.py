from playsound import playsound

def play(sound):
    if sound == 'foto':
        playsound('/home/mestre/catkin_ws/src/TP3/PSR_Trabalho3/robutler_bringup_tp3/lib/sound/foto.mp3')
    elif sound == 'drag':
        playsound('/home/mestre/catkin_ws/src/TP3/PSR_Trabalho3/robutler_bringup_tp3/lib/sound/drag.mp3')
    elif sound == 'drift':
        playsound('/home/mestre/catkin_ws/src/TP3/PSR_Trabalho3/robutler_bringup_tp3/lib/sound/drift.mp3')
    elif sound == 'thunder':
        playsound('/home/mestre/catkin_ws/src/TP3/PSR_Trabalho3/robutler_bringup_tp3/lib/sound/thunder.mp3')
    elif sound == 'aceleracao':
        playsound('/home/mestre/catkin_ws/src/TP3/PSR_Trabalho3/robutler_bringup_tp3/lib/sound/thunder.mp3')
    else:
        print('ERRO A REPRODUZIR FICHEIRO DE AUDIO')
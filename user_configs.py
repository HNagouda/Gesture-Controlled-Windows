# Currently binded gestures and features
# NOTE: DNC = Do NOT Change

class gesture_binds:
    actions = {
        # General Functionality
        'open_palm': 'cursor', # DNC
        'fist': 'mouse_click', # DNC
        'open_thumb': 'copy',
        'open_index': 'paste',
        'open_ring': 'screenshot',

        # Media Controls (YouTube)
        'fold_thumb': 'play_pause_vid',
        'fold_index': 'rewind_vid',
        'fold_middle': 'forward_vid',
        'fold_ring': 'activate_subtitles',
        'fold_pinky': 'full_screen',


        # Open-Program Controls
        'fold_thumb_and_index': 'open_vscode',
        'fold_index_and_middle': 'open_discord',
        'fold_middle_and_ring': 'open_spotify',
        'fold_ring_and_pinky': 'open_powershell',
        'open_pinky': 'open_browser',
        }

class paths:
    program_paths = {
            'desktop': 'C:/users/harsh/Desktop',
            'vscode': "C:/Users/harsh/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Visual Studio Code/Visual Studio Code.lnk",
            'discord': "C:/Users/harsh/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Discord Inc/Discord.lnk",
            'browser': "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Edge.lnk",
            'cmd': "C:/Users/harsh/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/System Tools/Command Prompt.lnk",
            'explorer': "C:/Users/harsh/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/System Tools/File Explorer.lnk",
            'powershell': "C:/Users/harsh/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Windows PowerShell/Windows PowerShell.lnk",
            'spotify': "C:/Users/harsh/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Spotify.lnk"

    }

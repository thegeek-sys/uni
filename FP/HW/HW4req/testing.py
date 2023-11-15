def traduci_spartito(tarahumara_song):
    umkansanian_song = ""
    duration = 0

    for symbol in tarahumara_song:
        if symbol.isdigit():
            duration = int(symbol) + duration * 10
        elif symbol == '-':
            umkansanian_song += 'b'
        elif symbol == '+':
            umkansanian_song += '#'
        elif symbol == ' ':
            umkansanian_song += 'P' + str(duration) + ' '
            duration = 0
        else:
            note_mapping = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'P'}
            umkansanian_song += note_mapping[symbol] + str(duration) + ' '
            duration = 0

    return umkansanian_song

# Esempio di utilizzo
spartito_input = "3+ 0-453 5+5- 0+ 1-64+ 56- 1- 1-3- 2+35- 130 66- 3+ 0+46-5- 5-66+ 52- 1+5 1 6 3+ 40+ 4-5+3+ 5+1"
spartito_output = traduci_spartito(spartito_input)
output_atteso = "D#1P1Ab1E1F1D1P1F#1Fb1P1A#1P1Bb1G1E#1P1F1Gb1P1Bb1P1Bb1Db1P1C#1D1Fb1P1B1D1A1P1G1Gb1P1D#1P1A#1E1Gb1Fb1P1Fb1G1G#1P1F1Cb1P1B#1F1P1B1P1G1P1D#1P1E1A#1P1Eb1F#1D#1P1F#1B1P1"

print(spartito_output == output_atteso)
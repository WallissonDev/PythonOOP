class AudioFile: # Superclasse

    def __init__(self, filename):

        if not filename.endswith(self.ext): # Segundo o vídeo, ele vai p    egar o ext das subclasses ( tenho dúvidas sobre isso )
            raise Exception('Formato Inválido') # Caso não seja a extensão de nenhuma subclasse, aparece formato inválido.

        self.filename = filename

class MP3File(AudioFile): # Subclasse

    ext = 'mp3'

    def play(self):
        print('Tocando arquivo MP3')

class WavFile(AudioFile): # Subclasse

    ext = 'wav'

    def play(self):
        print('Tocando arquivo Wav')

class OggFile(AudioFile):

    ext = 'ogg'

    def play(self):
        print('Tocando arquivo ogg.')

musica = MP3File('Rihanna.mp3')
musica.play()
wav = WavFile('Rihanna.wav')
wav.play()
mp3_falso = MP3File('musica.ogg') # Como o formato de musica.ogg é diferente do EXT da subclasse MP3 -> Traceback error
mp3_falso.play()
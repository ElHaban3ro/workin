from pynput import keyboard

class KeysHandler:
    def __init__(self):
        pass

    def on_press(self, key):
        try:
            print(f'Presionó {key}')


        except Exception as e:
            print(e)


    def start_handler(self):
        with keyboard.Listener(

            on_press = self.on_press

        ) as listerner:
            listerner.join()

from kivy.app import App
from kivy.uix.label import Label

class IPOneLite(App):
    def build(self):
        return Label(text="IP ONE LITE\nStatus: 300MB/Day ACTIVE\nWallet: Linked to Mr. Swartz\nHigh Earning: ENABLED")

if __name__ == "__main__":
    IPOneLite().run()

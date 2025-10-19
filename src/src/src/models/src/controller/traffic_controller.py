class TrafficController:
    def __init__(self):
        self.signals = {}
        print("[CTRL] TrafficController ready")

    def set_signal(self, junction, state):
        self.signals[junction] = state
        print(f"[CTRL] Signal at {junction} set to {state}")

    def get_signal(self, junction):
        return self.signals.get(junction, "RED")

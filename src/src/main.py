from src.controller.traffic_controller import TrafficController
from src.models.traffic_flow_predictor import TrafficFlowPredictor

def main():
    print("🚦 Starting AI Traffic Simulation...")
    controller = TrafficController()
    predictor = TrafficFlowPredictor()
    traffic_state = predictor.predict({})
    controller.set_signal("Junction-1", "GREEN")
    print("Predicted Traffic:", traffic_state)

if __name__ == "__main__":
    main()

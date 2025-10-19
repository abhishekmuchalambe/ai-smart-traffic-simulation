# src/main.py

from src.api.server import app
from src.controller.traffic_controller import TrafficController
from src.models.traffic_flow_predictor import TrafficFlowPredictor

def main():
    print("Starting AI Smart Traffic Simulation...")

    # Initialize modules
    controller = TrafficController()
    predictor = TrafficFlowPredictor()

    # Example usage
    traffic_state = predictor.predict(None)
    controller.set_signal("Intersection-1", "GREEN")
    print("Traffic state:", traffic_state)

if __name__ == "__main__":
    main()


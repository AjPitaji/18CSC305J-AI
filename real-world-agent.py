class AirQualityAgent:
    def __init__(self, threshold):
        self.threshold = threshold

    def read_air_quality(self):
        import random
        return random.randint(0, 500)

    def act(self, aqi):
        if aqi < self.threshold:
            return "Air quality is good. No action needed."
        else:
            return "Air quality is poor. Activating air purifiers."

    def run(self):
        while True:
            aqi = self.read_air_quality()
            action = self.act(aqi)
            print(f"AQI: {aqi}, Action: {action}")
            import time
            time.sleep(5)

if __name__ == "__main__":
    agent = AirQualityAgent(threshold=100)
    agent.run()

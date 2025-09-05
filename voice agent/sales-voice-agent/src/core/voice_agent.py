class SalesVoiceAgent:
    def __init__(self):
        print("Voice Agent initialized")
    
    def start_call(self):
        return "Hello! Thank you for calling. How can I help you today?"

# Simple test
if __name__ == "__main__":
    agent = SalesVoiceAgent()
    print(agent.start_call())

import os

def create_sales_voice_agent_project():
    # Create main project directory
    os.makedirs("sales-voice-agent/src/core", exist_ok=True)
    os.makedirs("sales-voice-agent/src/llm", exist_ok=True)
    os.makedirs("sales-voice-agent/src/voice", exist_ok=True)
    os.makedirs("sales-voice-agent/src/sales", exist_ok=True)
    os.makedirs("sales-voice-agent/src/utils", exist_ok=True)

    # Create main files
    files_to_create = {
        "sales-voice-agent/main.py": '''#!/usr/bin/env python3
"""
Sales Voice Agent - Main Entry Point
"""

def main():
    print("Sales Voice Agent - Ready to deploy!")
    print("Upload this folder to GitHub and run from there!")

if __name__ == "__main__":
    main()
''',

        "sales-voice-agent/requirements.txt": '''openai>=1.0.0
anthropic>=0.5.0
websockets>=11.0
pyyaml>=6.0
''',

        "sales-voice-agent/README.md": '''# Sales Voice Agent

An AI-powered voice agent for sales calls.

## Quick Start
1. Upload this folder to GitHub
2. Set up your API keys in repository secrets
3. Run `main.py`

## Features
- Real-time voice processing
- AI-powered conversation
- Lead qualification
- Multi-LLM support
''',

        "sales-voice-agent/.gitignore": '''# Python
__pycache__/
*.py[cod]
*.pyo
*~
.pytest_cache/
.coverage
.env
config.yaml

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
.DS_Store
''',

        "sales-voice-agent/src/core/voice_agent.py": '''class SalesVoiceAgent:
    def __init__(self):
        print("Voice Agent initialized")
    
    def start_call(self):
        return "Hello! Thank you for calling. How can I help you today?"

# Simple test
if __name__ == "__main__":
    agent = SalesVoiceAgent()
    print(agent.start_call())
''',

        "sales-voice-agent/src/llm/llm_interface.py": '''class LLMInterface:
    def __init__(self):
        self.model = "gpt-4-turbo"  # Placeholder
    
    def generate_response(self, prompt):
        # In real implementation, this would call actual LLM APIs
        return f"AI Response to: {prompt}"

# Simple test
if __name__ == "__main__":
    llm = LLMInterface()
    print(llm.generate_response("Hello there!"))
'''
    }

    # Create all files
    for filepath, content in files_to_create.items():
        with open(filepath, 'w') as f:
            f.write(content)
    
    print("✅ Project created successfully!")
    print("📁 Folder 'sales-voice-agent' is ready to upload to GitHub")

if __name__ == "__main__":
    create_sales_voice_agent_project()
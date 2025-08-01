#!/usr/bin/env python
import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

from flows.morpheus_chat_flow import MorpheusChatFlow

def run():
    """
    Run the Morpheus chat flow.
    """
    flow = MorpheusChatFlow()
    flow.state.message = "Hello, what can you help me with today?"
    response = flow.kickoff()
    
    print("Morpheus flow execution completed!")
    print(response)
    return response

if __name__ == "__main__":
    run()
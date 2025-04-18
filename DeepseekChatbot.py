from deepseek import DeepSeekAPI

# Initialize the DeepSeek API with your API key
api_key = "your_api_key_here"
deepseek = DeepSeekAPI(api_key)

# Define a function to handle the chat
def chat_with_deepseek():
    print("Welcome to DeepSeek Chat! Type 'quit' to exit.")
    
    # Initialize conversation history.
    # @TODO: persist the chat history in disk.
    conversation_history = []
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Add user message to history
        conversation_history.append({"role": "user", "content": user_input}) 
        
        try:
            # Send the entire conversation history
            response = deepseek.chat(
                messages=conversation_history,
                max_tokens=4000,  # Increase max tokens to prevent truncation
                stream=False  # Set to True if you want streaming responses
            )
            
            # Add assistant response to history
            assistant_response = response.choices[0].message.content
            conversation_history.append({"role": "assistant", "content": assistant_response})
            
            print(f"DeepSeek: {assistant_response}")
            
        except Exception as e:
            print(f"Error: {e}")
            # Optionally remove the last user message if there was an error
            conversation_history.pop()

# Start the chat
chat_with_deepseek()

# A simple chatbot build with Python, UV and Chainlit.
# 1- Chat Session: It represent one conversation between a user and the applicant.
# 2- EVENTS:When certain thing happens like sending a message.
# 3- HOOKS: Hooks are special functions that "hook into"these events.
# 4- DECOTATORS: These are special markers @ that enhance functions.
# 5- It is stateless because user data does not store.


import chainlit as cl

@cl.on_message # This is a Decorator
# Here is a specific fuction by using Decorator, where we pass a "message" parameter.
async def main(message: cl.Message):
    response = f"You said: {message.content}"
    await cl.Message(content=response).send()

#chainlit run main.py -w



# import chainlit as cl

# @cl.on_message
# async def main(message: cl.Message):
#     # Retrieve the user's session data, or initialize it if it doesn't exist
#     user_data = cl.user_session.get("user_data", {})

#     # Example: Store the number of messages sent by the user
#     user_data["message_count"] = user_data.get("message_count", 0) + 1

#     # Store some user-specific data
#     user_data["last_message"] = message.content

#     # Save the updated user data back to the session
#     cl.user_session.set("user_data", user_data)

#     # Prepare the response
#     response = f"You said: {message.content}\n"
#     response += f"You have sent {user_data['message_count']} messages so far.\n"
#     response += f"Your last message was: {user_data['last_message']}"

#     # Send the response
#     await cl.Message(content=response).send()
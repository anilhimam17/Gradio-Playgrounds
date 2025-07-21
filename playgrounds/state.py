import gradio as gr


# The Wrap Function
def message_logger(current_msg: str, message_history: list[str]):
    """Orchestrates the State driven interface to log messages."""
    output = {
        "Current Message": current_msg,
        "Message History": message_history[::-1]  # Reversed list of strings of messages
    }

    # Updating the state of messages in the chat to log.
    message_history.append(current_msg)
    return output, message_history

# The Main Function
def main():
    demo = gr.Interface(
        fn=message_logger, 
        inputs=[gr.Textbox(label="Input Message"), gr.State(value=[])],
        outputs=[gr.JSON(label="Message History"), gr.State()]
    )

    demo.launch()


# Driver Code
if __name__ == "__main__":
    main()
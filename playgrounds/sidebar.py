import gradio as gr
from gradio_pdf import PDF


# The main function that builds the interface
def main():
    with gr.Blocks(fill_width=True, fill_height=True) as demo:
        with gr.Sidebar(position="left"):
            account_name = gr.Markdown(value="## Account Name")
        with gr.Row(equal_height=True):
            pdf_uploader = PDF(label="Upload your PDF file")
            chatbot = gr.Chatbot()
        
    demo.launch(share=True)


# Driver code
if __name__ == "__main__":
    main()

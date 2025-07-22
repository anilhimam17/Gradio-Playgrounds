import gradio as gr
import numpy as np


# The Main Function
def main():
    with gr.Blocks() as demo:
        input_number = gr.Number(label="Input Number (in Degrees)")
        output_number = gr.Number(label="Output Trigo Value")
        sin_button = gr.Button(value="Sine")
        cos_button = gr.Button(value="Cosine")
        random_button = gr.Button(value="Random Numbers")
        clear_button = gr.Button(value="Clear")

        sin_button.click(lambda x: np.sin(x * (np.pi / 180)), inputs=input_number, outputs=output_number)
        cos_button.click(lambda x: np.cos(x * (np.pi / 180)), inputs=input_number, outputs=output_number)
        random_button.click(lambda: np.random.randint(1, 100), outputs=input_number)
        clear_button.click(lambda: None, outputs=input_number)

    demo.launch()


# Driver Code
if __name__ == "__main__":
    main()
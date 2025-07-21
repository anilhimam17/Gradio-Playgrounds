import gradio as gr
import numpy as np


# Wrap Function
def flip_stream(img: np.ndarray):
    return np.flipud(img)

# Main Function
def main():
    demo = gr.Interface(
        fn=flip_stream,
        inputs=gr.Image(streaming=True, sources=["webcam"]),
        outputs=gr.Image(streaming=True),
        live=True
    )

    demo.launch()

# Driver Code
if __name__ == "__main__":
    main()

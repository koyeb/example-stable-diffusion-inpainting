import torch
from diffusers import AutoPipelineForInpainting
import gradio as gr

# Load the inpainting pipeline
pipeline = AutoPipelineForInpainting.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16
).to("cuda")

pipeline.enable_model_cpu_offload()

# Function to perform inpainting
def image_inpaint(image_input, mask_input, prompt_input):
    image = pipeline(prompt=prompt_input, image=image_input, mask_image=mask_input).images[0]
    return image

def gradio_interface():
    with gr.Blocks() as demo:
        gr.Markdown("## Image Inpainting Service")

        with gr.Row():
            with gr.Column():
                image_input = gr.Image(type="pil", label="Upload Image")
                mask_input = gr.Image(type="pil", label="Upload Mask")
                prompt_input = gr.Textbox(label="Enter Prompt", placeholder="Describe what you want to inpaint")
                submit_btn = gr.Button("Inpaint")

            with gr.Column():
                result_output = gr.Image(type="pil", label="Inpainted Image")

        # Connect the button click event with the image inpainting
        submit_btn.click(image_inpaint, inputs=[image_input, mask_input, prompt_input], outputs=result_output)

    demo.launch()

# Run the Gradio interface
if __name__ == "__main__":
    gradio_interface()
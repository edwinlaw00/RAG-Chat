import gradio as gr
from chatbot import ChatBot
import config

with gr.Blocks() as demo:
    with gr.Tabs():
        with gr.TabItem("RAG Chat"):
            # First row:
            with gr.Row() as chatbot_output:
                chatbot = gr.Chatbot(
                    [],
                    elem_id="chatbot",
                    bubble_full_width=False,
                    height=500
                )

            # Second row:
            with gr.Row():
                input_txt = gr.Textbox(
                    lines=4,
                    scale=8,
                    placeholder="Enter text and press 'Submit'",
                    container=False,
                )

            # Third row:
            with gr.Row() as row_two:
                llm_dropdown = gr.Dropdown(label="LLM", choices=config.LLM_LIST, value=config.DEFAULT_LLM)
                text_submit_btn = gr.Button(value="Submit")
                clear_button = gr.ClearButton([input_txt, chatbot])
                temperature_bar = gr.Slider(minimum=0, maximum=1, value=0, step=0.1,
                                            label="Temperature", info="Choose between 0 and 1")

        with gr.TabItem("References"):
            ref_output = gr.Markdown()

        with gr.TabItem("Chat History"):
            history_output = gr.Markdown()

        # Process:
        txt_msg = text_submit_btn.click(fn=ChatBot.respond,
                                        inputs=[chatbot, input_txt, llm_dropdown, temperature_bar],
                                        outputs=[input_txt, chatbot, ref_output, history_output],
                                        queue=False).then(lambda: gr.Textbox(interactive=True),
                                                          None, [input_txt], queue=False)

if __name__ == "__main__":
    demo.launch()
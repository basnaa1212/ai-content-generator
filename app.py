import streamlit as st
import ollama

st.set_page_config(
    page_title="AI Content Generator",
    page_icon="✨"
)

st.title("✨ AI Content Generator")
st.write(
    "Generate blogs, social media captions,"
    "product descriptions, and summaries."
)

content_type=st.selectbox(
    "Choose Content Type",
    ["Blog",
     "Social Media Caption",
     "Product Description",
     "Summary"
     ]
)

topic=st.text_area(
    "Enter your topic or question",
    placeholder="eg: What are the benefits of AI?"
)

writing_style=st.selectbox(
    "Choose Writing Style",
    ["Simple","Professional","Creative"]
)

if content_type=="Summary":
    source_text=st.text_area(
        "Text to Summarize",
        placeholder="Paste the text you want to summarize."
    )
else:
    source_text=""

if st.button("Generate Content"):
    if content_type=="Summary":
        if not source_text.strip():
            st.warning("Please enter the text to summarize.")
            st.stop()
        prompt_topic=source_text
    else:
        if not topic.strip():
            st.warning("Please enter a topic or question.")
            st.stop()
        prompt_topic=topic

    if content_type=="Blog":
        task_instruction="Write only a blog with a title and 2-3 short paragraphs."
    elif content_type=="Social Media Caption":
        task_instruction="Write only one short social media caption with suitable hashtags."
    elif content_type=="Product Description":
        task_instruction="Write only one concise product description."
    else:
        task_instruction="Summarize the provided text using only the main points."

    prompt= f"""
    You are an AI content generator.
    Your only task is: {task_instruction}

    Topic or text:{prompt_topic}
    Writing style:{writing_style}
    
    Do not generate any other type of content.
    Keep the content clear, relevant, and concise.
    Follow the selected writing style.
    Return only the requested content.
    """
    with st.spinner("Generating content with Llama 3..."):
        try:
            response=ollama.chat(
                model="llama3",
                messages=[
                    {"role":"user","content":prompt}
                ],
                options={"num_predict":500}
            ) 
            generated_content=response["message"]["content"]
            st.session_state["generated_content"]=generated_content
            st.session_state["edited_content"]=generated_content
        except Exception as e:
            st.error(
                "Could not connect to Ollama. "
                "Make sure Ollama is running and try again."
            )
            st.caption(str(e))

if "generated_content" in st.session_state:
    st.text_area(
        "Edit your generated content",
        key="edited_content",
        height=300 
    )
    st.download_button(
        "Download Content",
        data=st.session_state["edited_content"],
        file_name="generated_content.txt",
        mime="text/plain"
    )
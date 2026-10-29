# AI Content Generator

## Description

The AI Content Generator is a simple application built using Python and Streamlit. It uses Llama 3 through Ollama to generate content based on user input.

## Features

- Generate blogs
- Generate social media captions
- Generate product descriptions
- Summarize text
- Choose a writing style
- Edit generated content
- Download generated content

## Technologies Used

- Python
- Streamlit
- Ollama
- Llama 3

## Project Structure

- `app.py` – Source code
- `README.md` – Project documentation
- `requirements.txt` – Required Python libraries
- `sample_input_output.md` – Sample input and output

## How to Run

1. Install Python and Ollama.

2. Download the Llama 3 model:

   ```
   ollama pull llama3
   ```

3. Install the required libraries:

   ```
   py -m pip install -r requirements.txt
   ```

4. Run the application:

   ```
   py -m streamlit run app.py
   ```

5. Open the local URL displayed in the terminal.

## Conclusion

This project helps users generate, edit, and download different types of content using AI.
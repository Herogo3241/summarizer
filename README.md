# Streamlit Wikipedia Summarizer

This is a simple Streamlit web application that allows users to search for a topic on Wikipedia and generate a summary using the `distilbart-cnn-12-6` model from the Hugging Face Transformers library.

## Features

- Search any topic on Wikipedia.
- Summarize the content of the Wikipedia page using a pre-trained summarization model.
- Handles disambiguation and empty content cases gracefully.

## Youtube Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/mi7nVDxkrwc" frameborder="0" allowfullscreen></iframe>

## Requirements

- Python 3.x
- [Streamlit](https://streamlit.io/)
- [Transformers](https://huggingface.co/transformers/)
- [Wikipedia-API](https://pypi.org/project/Wikipedia-API/)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. Navigate to the project directory:

   ```bash
   cd summerizer
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

2. Enter the search term in the input box provided.
3. The application will retrieve the Wikipedia page for the given search term, summarize it, and display the summary.





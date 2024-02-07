import wikipedia
import streamlit as st
from transformers import pipeline

st.markdown("<h1 style='text-align: center;'>Wikipedia Summarizer</h1>", unsafe_allow_html=True)


title = st.text_input('Enter a topic to search on Wikipedia', key='search-input', autocomplete='on')


summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e")


def trim_text(text, max_length):
    if len(text) <= max_length:
        return text
    else:
        return text[:max_length]


if title.strip() == "":
    st.warning("Please enter a search term.")
else:
    try:
        wikisearch = wikipedia.page(title)
        wikicontent = wikisearch.content

        wikicontent = trim_text(wikicontent, 1024)

        if not wikicontent.strip():
            st.warning("The Wikipedia page content is empty for the given search term.")
        else:
            st.title(wikisearch.title)
            text = summarizer(wikicontent, max_length=200, min_length=100, do_sample=False)
            st.write(text[0]["summary_text"])

    except wikipedia.DisambiguationError as e:
        st.warning(f"Ambiguous search term. Please select one option:")
        chosen_option = st.selectbox("Select an option", e.options)
        wikisearch = wikipedia.page(chosen_option)
        wikicontent = wikisearch.content
        wikicontent = trim_text(wikicontent, 1024)


        st.title(e.options[0].tilte())
        text = summarizer(wikicontent, max_length=200, min_length=100, do_sample=False)
        st.write(text[0]["summary_text"])

    except wikipedia.PageError:
        st.error("No matching page found. Please try again with a different search term.")

    except wikipedia.exceptions.WikipediaException as e:
        st.error(f"An error occurred while fetching Wikipedia content: {str(e)}")

    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")

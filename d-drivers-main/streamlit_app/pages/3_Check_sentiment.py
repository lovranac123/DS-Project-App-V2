import warnings
import os

# from transformers import pipeline
import streamlit as st
import streamlit_shadcn_ui as ui

from functions import get_sentiment

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Sentiment analysis",
    page_icon="🎭",
    # layout="wide"
)

# Page title and image
file_path = os.path.abspath("DATA-DRIVEN SEARCH FOR TRAFFIC DRIVERS.png")

# Check if the file exists
if os.path.exists(file_path):
    try:
        # Attempt to load the image
        st.image(file_path, use_column_width=True)
    except Exception as e:
        logging.exception("An error occurred while loading the image.")
        st.error(f"An error occurred: {str(e)}")
else:
    logging.error(f"Image file not found at path: {file_path}")
    st.error(f"Image file not found at path: {file_path}")

# Use Streamlit's file uploader for testing
uploaded_file = st.file_uploader("Choose an image file")
if uploaded_file is not None:
    try:
        st.image(uploaded_file, use_column_width=True)
    except Exception as e:
        logging.exception("An error occurred while loading the uploaded image.")
        st.error(f"An error occurred with the uploaded file: {str(e)}")

st.title("Sentiment checker")

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # supressing warnings
warnings.filterwarnings("ignore")

# model_name = "./sentiment/"# initialize sentiment analysis pipeline
# nlp = pipeline("sentiment-analysis", model=model_name)

cols_top = st.columns([0.5, 0.5])
with cols_top[0]:
    st.markdown(
        """How would your text feel to the readers? 
                
Check the sentiment here."""
    )
with cols_top[1]:
    st.info(
        icon="💡",
        body="""Model: \n
[German Sentiment BERT by Oliver Guhr](https://huggingface.co/oliverguhr/german-sentiment-bert)""",
    )
# def get_sentiment(text):
#     text = str(text)
#     if text and text != 'nan': # in case the text is empty
#         result = nlp(text)
#         label = result[0]['label']
#         score = result[0]['score']
#         return label.capitalize(), round(score*100, 2)
#     else:
#         return 'Neutral', None

text = ui.textarea(
    default_value="Ich fahre mein E-Bike sehr gerne!",
    placeholder="Enter your text",
    key="textarea1",
)

### text = st.text_input('Paste your text here', 'Ich fahre mein E-Bike sehr gerne!')
text = text.lower()
label, score = get_sentiment(text)

with ui.card(key="card1"):
    # ui.element("span", children=["Result"], className="text-gray-400 text-sm font-medium m-1", key="label1")
    if label == "Positive":
        ui.element(
            "span",
            children=[f"{label}"],
            className="text-green-400 text-lg font-bold m-1",
            key="label2",
        )
        ui.element(
            "span",
            children=[f"Confidence score {score} %"],
            className="text-gray-400 text-lg font-bold m-1",
            key="label3",
        )
        # st.markdown(f"**:green[{label}]**")
    elif label == "Negative":
        ui.element(
            "span",
            children=[label],
            className="text-red-400 text-lg font-bold m-1",
            key="label2",
        )
        ui.element(
            "span",
            children=[f"Confidence score {score} %"],
            className="text-gray-400 text-lg font-bold m-1",
            key="label3",
        )
        # st.markdown(f"**:red[{label}]**")
    else:
        if text:
            ui.element(
                "span",
                children=[label],
                className="text-blue-400 text-lg font-bold m-1",
                key="label2",
            )
            ui.element(
                "span",
                children=[f"Confidence score {score} %"],
                className="text-gray-400 text-lg font-bold m-1",
                key="label3",
            )

        # st.markdown(f"**:blue[{label}]**")
    # ui.element("span")
    # ui.element()
    # ui.element("span", children=[f"Confidence score {round(score*100, 2)} %"], className="text-gray-400 text-sm font-medium m-1", key="label3")
    # st.caption(f"""Confidence: {round(score*100, 2)} %""")


# with col[1]:
# st.markdown(label)
# st.caption(f"""Confidence: {round(score*100, 2)} %""")

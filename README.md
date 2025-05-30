# TEXT-SUMMARIZATION-TOOL

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: LAASYA SRUJANA I S

*INTERN ID*: CT04DL156

*DOMAIN*: ARTIFICIAL INTELLIGENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH KUMAR

*DESCRIPTION OF TEXT SUMMARIZATION TOOL*:

This project is a Text Summarization Tool that provides concise summaries of long text inputs using Extractive Summarization techniques. The goal is to help users quickly understand the main points of lengthy articles, reports, or documents.

*What I Worked On*:
I developed an end-to-end NLP-based summarization system that uses Natural Language Processing (NLP) techniques to identify and extract the most important sentences from a given text. The tool ranks sentences based on the frequency of meaningful words, and then selects the top-scoring ones to generate a summary. I implemented the full backend logic for summarization and built a user-friendly web interface to make the tool accessible.

*Technologies & Tools Used*:
*Programming Language*: Python

*Libraries Used*:

nltk (Natural Language Toolkit): For tokenization, stopword removal, and text processing.

heapq: To efficiently rank and select top sentences.

gradio: To build a web-based UI for interactive summarization.

Environment: Google Colab & Local Python (can run on both)

Model Type: Rule-based extractive summarization (no machine learning model used)

*Key Features*:
Tokenization: Breaks down text into words and sentences using NLTK.

Stopword Removal: Filters out common words (e.g., "the", "is", "and") that don’t add much meaning.

Frequency-Based Scoring: Calculates how often important words appear.

Sentence Scoring: Scores each sentence based on word frequency.

Top Sentence Selection: Uses heapq to select the top 3 highest-scoring sentences as the summary.

Gradio Interface: Allows users to paste text into a web form and receive a summary instantly.

*Output*:
The tool returns a concise summary (typically 2–3 sentences) that captures the key ideas of the input text.

It’s designed to work best on paragraphs between 100–500 words.

*How to Use*:
Paste or type text into the input box.

Click “Summarize”.

The summarized text will be displayed instantly.

Resources Required
nltk for NLP operations (punkt, stopwords)

gradio for UI interaction

Internet connection (to download NLTK data once)

*Outcome*:
This project demonstrates how simple NLP techniques can be used to build practical tools. It emphasizes clarity, usability, and efficient processing of natural language, making it useful for students, professionals, and researchers alike.

*OUTPUT*:

![Image](https://github.com/user-attachments/assets/c268688f-e311-4ae9-ba71-43cf7978965b)

![Image](https://github.com/user-attachments/assets/582c20a6-6ccc-4e97-9ced-e919984150dd)


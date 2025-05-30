import nltk
import heapq
import gradio as gr
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text):
    # Tokenize words and filter out stopwords and punctuation
    words = word_tokenize(text)
    stopwords = nltk.corpus.stopwords.words('english')

    word_frequencies = {}
    for word in words:
        word = word.lower()
        if word not in stopwords and word.isalpha():
            word_frequencies[word] = word_frequencies.get(word, 0) + 1

    # Tokenize sentences
    sentences = sent_tokenize(text)
    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_frequencies:
                if len(sent.split(' ')) < 30:
                    sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word]

    # Get top 3 scored sentences
    summary_sentences = heapq.nlargest(3, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)

    return summary

# Gradio Interface
demo = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=10, placeholder="Enter your text here..."),
    outputs="text",
    title="📝 Text Summarization Tool",
    description="Extractive summarization using NLTK and basic frequency scoring."
)

# Launch the app
demo.launch()

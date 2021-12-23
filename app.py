# Core Pkgs
import streamlit as st
import os
from gensim.summarization.summarizer import summarize
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline



def main():
    """ NLP Based App with Streamlit """

    # Title

    st.title("Summing")
    st.subheader("About App")
    st.markdown("""
    	#### Description
    	+ This app sums up any big fat text to it's shortest explaination, 
    	It even summarises the youtube video explaining the summary of whole content
    	""")

    options = st.selectbox("Choose the text source", ['Youtube Video Link', 'Random Text'])

    if options=='Random Text':
        message = st.text_area("Enter Text")
        algo = st.selectbox("Choose the Algo", ['Gensim', 'Sumy', 'Hugging Transformer'])
        if options=='Random Text':
            if algo=="Gensim":
                if st.button("Summarize"):

                    st.text("Using Gensim Summarizer ..")
                    summary_result = summarize(message)
                    st.success(summary_result)
            elif algo=="Sumy":
                pass
            elif algo=="Hugging Transformer":
                if st.button("Summarize"):
                    summarizer = pipeline('summarization')
                    num_iters = int(len(message) / 1000)
                    summarized_text = []
                    for i in range(0, num_iters + 1):
                        start = 0
                        start = i * 1000
                        end = (i + 1) * 1000
                        print("input text \n" + message[start:end])
                        out = summarizer(message[start:end])
                        out = out[0]
                        out = out['summary_text']
                        summarized_text.append(out)
                    st.success(summarized_text)




    else:
        Videolink = st.text_area("Paste your link here")
        video_id = Videolink.split("=")[1]
        YouTubeTranscriptApi.get_transcript(video_id)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        result = ""
        for i in transcript:
            result += ' ' + i['text']
        # print(result)
        print(len(result))
        st.text("Using Gensim Summarizer ..")
        summary_result = summarize(result)
        st.success(summary_result)

    st.sidebar.subheader("About App")
    st.sidebar.text("Summing")
    st.sidebar.info("this is a streamlit based application which performs summarisation")

    st.sidebar.subheader("By")
    st.sidebar.text("Siddhivinayak Dubey")
    st.sidebar.text("Amishi Tyagi")


if __name__ == '__main__':
    main()
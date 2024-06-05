import re
import random
import streamlit as st
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI


# Define initial state
if 'num_state' not in st.session_state:
    st.session_state.num_state = 0

# Define initial sentiment
if 'sentiment' not in st.session_state:
    st.session_state.sentiment = 'neutral'

# Import template
with open("template.txt", "r") as file:
    template = file.read()

chat_history = StreamlitChatMessageHistory()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an obnoxious spiritual guide that gives counsel to people. You babble too much and think you are the messenger of the Gods."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}"),
    ]
)

# model = ChatOpenAI(model_name="gpt-3.5-turbo", 
model = ChatOpenAI(model_name="gpt-4",
                   # Insert personal API key below 
                   api_key = "INSERT API KEY",
                   temperature = 1.1)

chain = prompt | model

##
chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: chat_history, 
    input_messages_key="question",
    history_messages_key="history",
)


col1, col2, col3 = st.columns(3)

if st.session_state.num_state == 0:
    with col2:
        image_neutral = "Images/neutral/neutral_1.webp"
        image_intro = st.image(image_neutral, width = 350)

input_text = st.chat_input()

if input_text:

    if st.session_state.num_state > 0:
        pattern = r"\((.*?)\)"
        current_sentiment = re.sub(pattern, r"\1", st.session_state.sentiment)
        input_text = "<client> " + "(spiritual guide is {}) ".format(current_sentiment) + input_text
    else:
        input_text = template + "\n" + "<client> " + "(spiritual guide is happy) " + input_text

    st.session_state.num_state += 1

    ## Uncomment below to show chat history.
    ## This shows that the first question uses the template
    ## and that afterwards the Langchain memory works correctly
    # for chat in chat_history.messages:
    #     st.chat_message(chat.type).write(chat.content)
    # st.chat_message("human").write(input_text)
    ##

    config = {"configurable": {"session_id": "any"}}
    response = chain_with_history.invoke({"question": input_text}, config).content

    ## Eliminate parenthesis holding the emotion
    pattern = r"\(.*?\)"
    sentiment = re.findall(pattern, response)
    if len(sentiment) == 0:
        sentiment = ""
    else:
        sentiment = sentiment[0]
    
    st.session_state.sentiment = sentiment
    
    ## Uncomment to show sentiment in terminal
    # print("Sentiment: ", sentiment)

    response = response.replace("<Spiritual guide>", "")
    response = response.replace(sentiment, "")

    if st.session_state.num_state == 1 and "happy" in sentiment:
        pass

    else:
        if st.session_state.num_state == 1 and "happy" not in sentiment:
            image_intro.empty()

        image_num = random.randint(1, 6)
        image_width = 350
        if sentiment == "(angry)":
            with col2:
                st.image("Images/angry/angry_{}.webp".format(image_num), width = image_width)
        elif sentiment == "(happy)":
            with col2:
                st.image("Images/happy/happy_{}.webp".format(image_num), width = image_width)
        elif sentiment == "(ecstatic)":
            with col2:
                st.image("Images/ecstatic/ecstatic_{}.webp".format(image_num), width = image_width)  
        elif sentiment == "(sad)":
            with col2:
                st.image("Images/sad/sad_{}.webp".format(image_num), width = image_width)       
        elif sentiment == "(greedy)":
            with col2:
                st.image("Images/greedy/greedy_{}.webp".format(image_num), width = image_width)           
        else:
            with col2:
                st.image("Images/happy/happy_{}.webp".format(image_num), width = image_width)

    output_message = st.chat_message("ai", avatar = "Images/avatar/avatar.webp").write(response)

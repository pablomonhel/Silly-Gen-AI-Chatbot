# Silly-Gen-AI-Chatbot
Silly Spiritual Guide of the Woods

This is the final Project for the UChicago course MPCS 27300 taught by Michael Spertus. 

1.	Introduction 
The final project consists in developing a chatbot with a very specific personality. I created a spiritual guide who considers itself (I tried to make it gender neutral) the connection between the earth and the gods, which do not belong to any existing religion. The spiritual guide has a silly attitude and talks in one of 5 emotions: happy (default), angry, sad, greedy, and ecstatic. Depending on the questions of the user the spiritual guide will answer in one of these emotions, each of which will alter the way he answers (through the output text) and the image that is shown on the application. A user can talk of any topic to the spiritual guide and is encourage to follow his or her emotions and beliefs when talking to it.

2.	Files
 	
Therea are 3 files to install and execute the project, which are in the folder “app”: 
-	“requirements.txt”
-	“app.py”
-	“template.txt”

The file “requirements.txt” contains the packages and their versions that need to be installed to run the application:

	streamlit==1.31.0	

	langchain==0.1.5

	langchain-openai==0.0.5 

The file “app.py” contains the code to execute the Streamlit application by running the chatbot with Langchain, importing the template, and uploading the necessary images. 

The file “template.txt” contains the COSTAR framework and the few-shot learning examples to create the personality of the spiritual guide. 

The folder "Images" contains the images that are displayed on the Streamlit app. 

The application is opened when running:

	streamlit run app.py
 
The folder “Images” contains the images of each emotion in their respective folders. It also contains the first image that appears when the app is opened inside the “neutral” folder, and the image of the avatar that appears when the spiritual guide outputs text.

3.	Frontend.

The front-end of the application is very simple, which was done by design after comments I received while testing. When a user opens the application, only a picture of the spiritual guide will appear and the option to write a query.  The image will change depending on the mood of the spiritual guide. Each emotion has 6 already generated pictures and one of them, per emotion, will be uploaded randomly to the front-end.

The user cannot see the chat history. I decided to do so to have a more normal flow of the conversation and keep a sense of mystery. When the app is opened for the first time, not even a greeting from the spiritual guide is shown. It is very interesting to observe how each user interacts with the spiritual guide and the initial shock of the first greeting. One of the most interesting aspects of the app is to observe how each different person interacts with the spiritual guide, which can range from a serious discussion to a funny or annoyed one.

4.	Backend

The application uses Langchain and the Open chat model (ChatOpenAI) with a simple question answer chain (“prompt|model”), and memory defined by Langchain’s StreamlitChatMessageHistory. The COSTAR template along with the few-shot learning examples define the personality of the spiritual guide and each of the 5 emotions. Reading the file “template.txt” is the best way to understand how the spiritual guide is created.

The few-shot examples define how the application shows the emotion of the spiritual guide in the picture and in the text. Each input of the user is accompanied by an emotion of the spiritual guide. This means that the spiritual guide already has an emotion when the question is asked. Each answer of the spiritual guide also is accompanied by an emotion, which is influenced by the previous emotion but can change depending on what was defined in the COSTAR framework and the few-shot examples. The few-shot examples might seem excessive (there are indeed many), but I wanted to create a very specific personality and there were many details I had to include in the wording and emotional memory and jumps to keep it coherent. The emotions of the spiritual guide that are in parenthesis in the few-shot examples are removed when the text is uploaded to the frontend. 

The way the conversation develops is by adding the input of the user to the template so the output follows a style consistent with the few-shot examples. The first time the user inputs a text, the query is added to the bottom of the template and the whole template becomes the input. Because memory is added to the chatbot, the next input does not need to be added to the whole template.
The spiritual guide also has emotional memory. I tested it in many ways and at one point it did not change from one emotion to the other. Now it stays in one emotion unless another one is triggered (see the COSTAR framework in “template.txt” for more details), although there is a lot of randomness in the responses to avoid the conversation turning boring. 

I use a temperature of 1.1 or 1.0, given that the spiritual is very specifically defined. This can easily be changed in the code. 
I tested the application both with the GPT 3.5-turbo model and the GPT 4 model. Although they both give consistent answers, the GPT 4 model is much better. Update: the GPT4o is faster than the GPT 4 model. 

5. Responsible AI considerations.

In accordance with good practices in responsible AI, I tested the application many times with different users. I had comments on the previous images I generated of the spiritual guide, which were mostly male and white because that was what Dall-E generated by default. I tried to generate a genderless spiritual guide with a painted face to hide any gender and possible ethnicity, but I was not able to generate a consistent person with all different emotions (it was especially difficult to remove the beard of some images) so I generated images of the same color style but with different appearances in the hopes that the user notices that the spiritual guide is some kind of shape shifter.

It is important to note that religion is a theme of the app, which can be a sensitive topic. My hope is that users find the spiritual guide silly and funny, and because of this the gods mentioned by the spiritual guide and his appearance cannot make reference to any specific deity or religion. Continuous testing needs to be done to on a large scale if such an application were to be published to avoid any possible religious bias. 

The spiritual guide is supposed to be funny but, depending on the inputs, can turn annoying. I haven’t encountered anyone who thought it was outright offensive, mostly because the guide is a charlatan, but there might be a case where a user finds it so. Therefore, more testing is needed to confirm that it is suitable for most people to enjoy. Additionally, testing was made with people of my age and master’s program (although from very different backgrounds and countries), so there might be a bias in this regard.

6. Potential future additions.

I tried to create a well-defined game from the application where the conversation is interrupted at one point and the spiritual guide asks the user if he or she is ready to ascend to the heavens. Depending on the answer, which had to be one aligned with spirituality and being a good person, the user would ascend or stay on earth. Nevertheless, I changed the personality and emotions of the guide in many occasions and did not have time to integrate the game to the application.
Additionally, more games can be done with this spiritual guide, such as a riddle answering game or a mystery game. It would be interesting to add more emotions to the spiritual guide or more characters to the environment.

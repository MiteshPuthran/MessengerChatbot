# MessengerChatbot

### - This is a personal project under progress.
### - Creating a chatbot using Whatsapp data on Tensorflow to be run on a facebook page. 

#### The idea behind creating the chatbot is to build a self sustainable program that can be used to interact and take decisions on its own without the human interference. This application will try minimize the waiting time and emotional interference while dealing with certain situations. 

## The problem I am trying to solve:
#### There are times when we need responses as soon as possible without any hassle. Suppose someone has met with a car accident where the person has to claim the insurance he has by notifying the company. There are times like today where you are not instantly connected with the respresntative as needed, usually there is a waiting time as the representative is busy with someone else.
#### This is not the right condition where you have met with a accident and waiting in the middle of the road trying to get a hold of the insurance company represntative. This is also a situation where you are emotionally challenged andwhen you get hold of the representative, there is not guarantee that everything will go well without any hassel. There can also be a fued between the two people.
#### Instead why not come up with a online chatbot thats trained well enough to deal with such situations. As most of the things in today's world are connected to internet. The person in distress no longer has to wait for any represntative on the phone, instead they could directly interact with the chatbot that is trained well to deal with different situations that the person in front has experienced. 
#### The chatbot will be capable of asking the right questions and guiding the person through its claiming process without the human interactions. This process will always result in a uniform outcome rather than ambigious ones when humas are involved.

## The process of building the chatbot I undertook is as follows:

## Data Collection and Processing

### Fetching the data
* Using data from my whatsapp conversations to train the model. Data was obatined from Whatsapp where you get the option to email the conversations in the form of text file.

### Data Pre-processing
* Creating functions to clean the data from punctutations, symbols, extra spaces etc. and function to split the sent messages and their responses in a dictionary. I have also included the python notebook of the work I have complted till now.

### Future path of progress:
* Creating word vectors embeddings either by using the text data or using a pre-trianed word vector. 
* Building a Seq2Seq model with Tensorflow
* Training the model
* Setting up messenger chatbot in Facebook.
* Deploying the trained model
* Testing it out.

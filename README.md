# ComprehensibleChinese
Streamlit + ChatGPT app for Chinese learners to consume more comprehensible input by converting native text to learner's level.

## Motivation
I'm currently learning Chinese, and one of the biggest language learning theories is Comprehensible Input (CI).

CI is an instructional technique that relies on learners consuming large amounts of natural input,
and slowly building an understanding of the language.

I didn't want to have to pay for apps that produce Chinese content at my level (B1),
so I made this app to help myself and fellow learners produce their own learning materials.

## Future work
- [ ] "Circling" chatbot to help you learn new words using the Circling method
- [ ] Upload known vocabulary list to get more personalized modifications
- [ ] Generate comprehension questions for the text, interact with a Chatbot to learn more

## Installation
Clone the workspace.

Create virtual environment
```shell
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
Launch the app locally
```shell
streamlit run app.py
```
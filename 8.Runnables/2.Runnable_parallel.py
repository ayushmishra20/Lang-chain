from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from  langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model= 'gemini-2.5-flash',
    api_version='v1beta'
)

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

parellel_cahin = RunnableParallel({
    'tweet':RunnableSequence(prompt1, model, parser),
    'linkdin':RunnableSequence(prompt2, model, parser)
})

result = parellel_cahin.invoke({'topic':'AI'})
print(result['tweet'])
print(result['linkdin'])
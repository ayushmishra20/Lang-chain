from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_version="v1beta"
)

# detailed Way
template2 = PromptTemplate(
    template='Greet this person in 5 languages except hindi. The name of the person is {name}',
    input_variables=['name']
)

# fill the values of the placeholders
prompt = template2.invoke({'name':'Mr Ayush Mishra'})

result = model.invoke(prompt)

print(result.content)
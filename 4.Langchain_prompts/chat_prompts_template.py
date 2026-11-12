from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('System','You are a helpful {domain} expert'),
    ('human', 'Explain in simple tearms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket', 'topic':'Dusra'})

print(prompt)
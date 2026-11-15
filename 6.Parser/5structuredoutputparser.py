from dotenv import load_dotenv
from langchain_classic.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Model (fixed 'api_version' typo, or you can omit it entirely)
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

schema = [
    ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="Fact 3 about the topic"),
]

# Fixed class name to StructuredOutputParser and method name to from_response_schemas
parser = StructuredOutputParser.from_response_schemas(schema)

prompt = PromptTemplate(
    template="Give 3 facts about {topic}\n{format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

chain = prompt | model | parser

result = chain.invoke({"topic": "black hole"})
print(result)

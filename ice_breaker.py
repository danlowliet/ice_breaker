from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate 
from langchain.chat_models import ChatOpenAI

information = """
Elon Reeve Musk is a businessman and investor. He is the founder, chairman, CEO, and CTO of SpaceX;
angel investor, CEO, product architect and former chairman of Tesla, Inc.; owner, chairman and CTO of X Corp.;
founder of the Boring Company and xAI; co-founder of Neuralink and OpenAI; and president of the Musk Foundation.
He is the wealthiest person in the world, with an estimated net worth of US$232 billion as of December 2023,
according to the Bloomberg Billionaires Index, and $254 billion according to Forbes, primarily from his ownership stakes in Tesla
and Spacex
A member of the wealthy South African Musk family, Elon was born in Pretoria and briefly attended the University
of Pretoria before immigrating to Canada at age 18, acquiring citizenship through his Canadian-born mother.
Two years later, he matriculated at Queen's University at Kingston in Canada. 
Musk later transferred to the University of Pennsylvania, and received bachelor's degrees in economics and physics. 
"""

if __name__ == '__main__':
    print("hello friend")
    
    summary_template = """
    given the information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
    """
    
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    
    print(chain.run(information=information))

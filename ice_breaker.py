from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from third_parties.linkedin import scrap_linkedin_profile



if __name__ == "__main__":
    print("hello friend")

    summary_template = """
    given the LinkedIn information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    
    linkedin_data = scrap_linkedin_profile(
        linkedin_profile_url="https://linkedin.com/in/thomas-hepburn-01721719/"
    )

    print(chain.run(information=linkedin_data))



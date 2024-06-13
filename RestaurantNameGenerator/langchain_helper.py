from secret_key import groq_api_key
import os
groq_api_key = os.getenv('GROQ_API_KEY')
import langchain_groq
from langchain_groq import ChatGroq

chat = ChatGroq(
    api_key = groq_api_key,
    model_name = "llama3-8b-8192"
)

def getNameAndItems(cuisine):
    from langchain_core.prompts import PromptTemplate

    prompt = PromptTemplate(
            input_variables=['cuisine'],
            template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this.Please provide only the name and only one name. No need quotations",
    )
    from langchain.chains import LLMChain
    name_chain=LLMChain(llm=chat,prompt=prompt,output_key="restaurant_name")
    prompt_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}. Return it as comma separated list. No need extra sentences",
    )
    items_chain=LLMChain(llm=chat,prompt=prompt_items,output_key="menu_items")
    from langchain.chains import SequentialChain

    chain = SequentialChain(
        chains=[name_chain, items_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"]
    )
    response=chain({"cuisine":cuisine})
    return response

if __name__=="__main__":
    print(getNameAndItems("Italian"))

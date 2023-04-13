from langchain.prompts import PromptTemplate
from typing import List

def format(template: PromptTemplate, product: str) -> str:
    return template.format(product=product)

def create_template(variables: List[str], template: str) -> PromptTemplate:
    return PromptTemplate(
        input_variables=variables,
        template=template,
    )

def main():
    product = "colorful socks"
    prompt_template = create_template(
        variables=["product"],
        template="What is a good name for a company that makes {product}?"
    )
    print(format(prompt_template, product))

if __name__ == '__main__':
    main()

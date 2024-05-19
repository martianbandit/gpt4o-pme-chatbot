import openai
import config

openai.api_key = config.OPENAI_API_KEY

def generate_prompt(question, extracted_info, company_data):
    prompt = f"{extracted_info}\n\nInformations sur l'entreprise :\n{company_data['about']}\n\nProduits : {', '.join(company_data['products'])}\n\nContact : {company_data['contact']}\n\nQuestion: {question}\nRéponse:"
    return prompt

def get_chatbot_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()


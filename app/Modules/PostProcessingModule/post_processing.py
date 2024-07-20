import json
import requests
from decouple import config
from groq import Groq

GROQ_API_KEY = config("GROQ_API_KEY")
GROQ_MODEL = "llama3-70b-8192"

groq_client = Groq(
    api_key=GROQ_API_KEY,
)

def get_system_prompt():
    system_prompt = f"""You're an expert data analyzer and extractor. \
                    You need to assist in cleaning and extracting the perfect textual data from a list of texts.\
                    The text list will contain the OCR-extracted data from the nutritional table usually placed on the products.\
                    \nBasic rules you have to follow:
                    \n1- Please correct any grammar or syntax error
                    \n2- Only pick quantitative data such as calories 190, Protein 5g, etc...
                    \n3- Pick an entity with its first quantitative number and unit if available, for example 
                    \n  a- Calories 190 230 -> Output should be Calories 190
                    \n  b- Total fat 1g %Daily Value% -> Output should be Total fat 1g
                    \n  c- 2% 2% -> Output should be 'None'
                    \n  d- Sodium 210mg 9% 12% -> Output should be Sodium 210mg
                    \n  e- Trans Fat Og -> Trans Fat 0g
                    \n  f- 'Vitamin A 10% 15%' -> Output should be Vitamin A 10%
                    \n  g- Response in JSON format only.
                    \n4- JSON Format should be : 
                    {{
                    data: [list of strings],
                    length: length of list
                    }}
                """

    return system_prompt

def get_user_prompt(input_list):
    user_prompt = f"""A Python list will be provided to you that contains a list of strings,\
    iterate through each string, read it, analyze it, choose what adjustment needs to be made based on the defined rules,\
    and return a modified Python list that contains strings. Please strictly follow the rules, and be consistent with logic.\n

    You can drop non-quantitive or incomplete strings(think twice before doing so, information is critical) such as:
    \n a- 'Nutrition Facts' -> because its not quantitive
    \n b- '1 Cup59g' -> quantity is present, but the quantity of which element it is, is missing so it's incomplete information. 

    \nNote:
    \n i- Don't provide me a Python code or extra text
    \n ii- Provide the modified list ONLY.
    
    \nList:
    {input_list}
    """
    return user_prompt


def Get_llama_respone(input_list):
    try:

        system_prompt = get_system_prompt()
        user_prompt = get_user_prompt(input_list)

        messages = [{"role": "system", "content": system_prompt},{"role": "user", "content": user_prompt}]

        response = groq_client.chat.completions.create(
            messages=messages,
            model=GROQ_MODEL,
            response_format={"type": "json_object"},
            temperature = 0.3)
        ai_response = response.model_dump_json()
        ai_response = json.loads(ai_response)
        result_json = ai_response["choices"][0]["message"]["content"]
        
        print("THIS IS THE RESPONSE",result_json)

        return result_json

    except Exception as e:
        print("THIS IS THE EXCEPTION IN GET LLAMA RESPONSE",e)
        return {}


# input_list = ['bal', 'HIGH IN FIBER', 'Nutrition Facts', '1 Cup59g', 'Servings Per Container About9', 'Ameent Per Serving witt 1h cop', 'Calories 190 230', 'Calories from Fat 10', 'Total Fat 1g %OailyValue**', '2% 2%', 'Saturated Fat Og 0% 0%', 'Trans Fat Og', 'Polyunsaturated Fat Og', 'Monounsaturated Fat Og', 'Cholesterol Omg 0% 0%', 'Sodium 210mg 9% 12%', 'Potassium 390mg 11%17%', 'Total Carbohydrate 46g 15% 17%', 'Dietary Fiber 7g 28%28%', 'Sugars 18g', 'Protein 5g', 'Vitamin A 10% 15%', 'Vitamin C 0% 0%', 'Calcium 2% 25 15%', 'Iron 25%', 'Vitamin D 10%', 'Thiamin 25% 35% 30%', 'Riboflavin 25%', 'Niacin 25% 25%', 'Vitamin Be 25% 25%']

# result_json = Get_llama_respone(input_list)
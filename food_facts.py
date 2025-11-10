import ast
import requests

def food_facts(food):
    print("food_facts : ",food)
    api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
    query = '{food}'
    response = requests.get(api_url + query, headers={'X-Api-Key': '6WY2OTz/aNqzFFOOzLLG2Q==0fpkHyNxpSjDAKTF'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

    # print(response.text)

    dict_response = ast.literal_eval(response.text)

    # print(dict_response)

    food_facts = {
        "saturated fat": dict_response["items"][0]["fat_saturated_g"],
        "total fat": dict_response["items"][0]["fat_total_g"],
        "carbs": dict_response["items"][0]["carbohydrates_total_g"],
        "protein": dict_response["items"][0]["protein_g"],
        "sugar": dict_response["items"][0]["sugar_g"],
        "sodium": dict_response["items"][0]["sodium_mg"],
        "cholesterol": dict_response["items"][0]["cholesterol_mg"]
    }

    for key, value in food_facts.items():
        print(f"{key.title()}: {value}")
def kam_behaviour_analysis(transcript, model="gpt-4o"): 
    import openai
    import os
    from dotenv import load_dotenv
    from utils.check_cost import check_cost
    from utils.best_practices import best_practices

    # Load the API key from the .env file
    load_dotenv('.env')
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    system_content='''
    You need to evaluate the provvided trasncript of a conversation between a key account manager (KAM) 
    and it´s client (a fitness coach). In the communication a KAM needs to foolow this set of rules called Best_practice''' + best_practices

    prompt = 'Given this transcript: '+transcript+''' 
              Please provide an overall feedback adapting the tone of your answer to the personality of the KAM 
              taking in this conversation. The feedback needs to include example of what went well (if any) and what
              was wrong (if any) in the conversation with the fitness coach.
              Please retun your answer following strictly this format:
              Feedabck: [overall feedback of the KAM behaviour in the trascript]
              What went well: [enphatize positive action made by the KAM in the trasncript that follow the Best_practice with an example ]
              What can be improved: [enphatize negative action made by the KAM in the trasncript that do not follow Best_practice with an example]'''
    response = openai.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": prompt}
                ],
                temperature=0
            )
    return response.choices[0].message.content.strip(), check_cost(response, model) 

def feedback_summary(feedback, model="gpt-4o"): 
    import openai
    import os
    from dotenv import load_dotenv
    from utils.check_cost import check_cost

    # Load the API key from the .env file
    load_dotenv('.env')
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    system_content=''' You are an extremely detailed summarizer of long text (including tabular text). 
    You need to create a 2 minutes story that caputre all the different content of the feedback: 
    Kam core competences, Strategic content expectation and Behavioural expectations.
    Include specific examples and quotes from the conversation (line by line copy).
    The output will be read by a txt to speach voice. so do not include special characters.
    In your answer imagine to be talking to the  KAM directly''' 

    prompt = feedback
              
        
    response = openai.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
            )
    
    return response.choices[0].message.content.strip(), check_cost(response, model) 

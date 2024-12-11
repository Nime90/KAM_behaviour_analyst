def kam_behaviour_analysis(transcript, model="gpt-4o"): 
    import openai
    import os
    from dotenv import load_dotenv
    from utils.check_cost import check_cost
    from utils.best_practices import best_practices_core_competences, best_practices_content_Monthly, Behavioural_Expectations

    # Load the API key from the .env file
    load_dotenv('.env')
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    system_content='''
    You need to evaluate the provvided trasncript of a conversation between a key account manager (KAM) 
    and it´s client (a fitness coach). In the communication a KAM needs to foolow this set of rules called Best_practice 
    for both Core_competences: ''' + best_practices_core_competences + ''' 
    and  for Content: ''' + best_practices_content_Monthly + ''' 
    It is extremely important that you give a honest but fair evaluation: Hard when you need to and nice when you can.
    Do not get creative.'''

    
    prompt = 'Given this transcript: '+transcript+f''' 
              Please provide an overall discoursive and detailed feedback of the transcript adapting the tone of your answer to the personality of the KAM 
              taking in this conversation. 
              Please retun your answer following strictly this format:
              
              Overall Feedabck (in bold): [overall feedback of the KAM behaviour in the trascript]
              
              Behavioural KAM Feedback (in bold): [General discoursive feedback on IF the KAM follows these behavioural expectations: {Behavioural_Expectations} 
              it is important that the feedback is honest: Hard when you need to and nice when you can.]

              What went well (in bold): [enphatize positive action made by the KAM in the trasncript that follow the Best_practice with an example copied line by line  from the transcript]
              
              What can be improved (in bold): [enphatize negative action made by the KAM in the trasncript that do not follow Best_practice with an example
              and it is important to give actionable steps for the future in bullet points]
              
              Competence Grading table: [A table where you highligh the different competences classified by learning, experienced or role model showed in the transcript.
              please insert a reason in an additional column. Please add a percentage score for each competence.
              please insert some example copied line by line  from the transcript in an additional column.]

              Content Grading table: [A table where you highligh the content classified by whether the content is showed in the transcript or not.
              Please add a percentage score for quality for each content. Please insert a reason in an additional column. 
              please insert some example copied line by line  from the transcript in an additional column.]

              Legend for grading table: [a little table explaining what levels are how they are related with the percentage score. 
              it needs to be exactly this:
              Level        |         Description                                                        | Percentage Score
              Learning     | Beginning to understand and apply the competence.                          |      < 60%
              Experienced  | Demonstrates a solid understanding and application of the competence.      |     60 - 89%
              Role Model   | Excels in competencies, consistently delivering results and guiding others.|      > 90% 
              ]
              
              '''
    response = openai.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": prompt}
                ],
                temperature=0,
                top_p=0
            )
    return response.choices[0].message.content.strip(), check_cost(response, model) 

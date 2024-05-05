# import openai

# openai.api_key = 'your-api-key'

# def analyze_resume(cv_text, job_description):
#     response = openai.Completion.create(
#       model="gpt-3.5-turo",
#       prompt=f"Rate the following CV against the job description. CV details: {cv_text}. Job Description: {job_description}",
#       temperature=0
#     )
#     return response.choices[0].text.strip()

import os

from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
    
)

def get_prompts(resume_text, jd):
    system_prompt = str()
    with open("prompts/system_prompt.md", "r") as file:
        system_prompt = file.read()

    user_prompt = str()
    with open("prompts/user_prompt.md", "r") as file:
        user_prompt = file.read()
        user_prompt = user_prompt.replace("{resume_text}", resume_text)
        user_prompt = user_prompt.replace("{jd}", jd)

    return system_prompt, user_prompt

def evaluate_resume(resume_text, jd):
    system_prompt, user_prompt = get_prompts(resume_text, jd)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        top_p=0.9
    )

    response = completion.choices[0].message.content
    return str(response)

# def generate_summary(data):
#     summary = """
#     ## Summary of Resume-Job Description Match

#     """

#     if "keyword_frequency" in data:
#         summary += """
#         ### Keyword Frequency
#         """

#         for keyword, frequency in data["keyword_frequency"].items():
#             if int(frequency) <= 0:
#                continue

#             summary += f"""
#             - {keyword}: {frequency} times
#             """

#     if "skill_match" in data:
#         if "total_skills_required" in data["skill_match"]:
#             summary += """
#             ### Skill Match
#             """

#             summary += f"""
#             - Total Skills Required: {data["skill_match"]["total_skills_required"]}
#             """

#         if "skills_matched" in data["skill_match"]:
#             summary += f"""
#             - Skills Matched: {data["skill_match"]["skills_matched"]}
#             """

#         if "percentage_matched" in data["skill_match"]:
#             summary += f"""
#             - Percentage Matched: {data["skill_match"]["percentage_matched"]}
#             """

#     if "experience_relevance" in data:
#         if "total_skills_required" in data["experience_relevance"]:
#             summary += """
#             ### Experience Relevance
#             """

#             summary += f"""
#             - Responsibilities Matched: {data["experience_relevance"]["responsibilities_matched"]}
#             """

#         if "skills_matched" in data["experience_relevance"]:
#             summary += f"""
#             - Achievements Matched: {data["experience_relevance"]["achievements_matched"]}
#             """

#     if "education_match" in data:
#         if "degree_level" in data["experience_relevance"]:
#             summary += f"""
#             ### Education Match
#             """

#             summary += f"""
#             - Degree Level: {data["education_match"]["degree_level"]}
#             """

#         if "major_matched" in data["experience_relevance"]:
#             summary += f"""
#             - Major Match: {"Yes" if data["education_match"]["major_matched"] else "No"}
#             """

#         if "certifications_matched" in data["experience_relevance"]:
#             summary += f"""
#             - Certifications Matched: {", ".join(data["education_match"]["certifications_matched"])}
#             """

#     return summary

    # summary += """
    # Years of Experience:
    # - Total Experience Years: {8}
    # - Required Experience Years: {9}
    # - Experience Match: {10}

    # Soft Skills:""".format(
    #         data["skill_match"]["total_skills_required"],
    #         data["skill_match"]["skills_matched"],
    #         data["skill_match"]["percentage_matched"],
    #         data["experience_relevance"]["responsibilities_matched"],
    #         data["experience_relevance"]["achievements_matched"],

    #         data["years_of_experience"]["total_experience_years"],
    #         data["years_of_experience"]["required_experience_years"],
    #         "Yes" if data["years_of_experience"]["experience_match"] else "No"
    #     )

    # for skill, value in data["soft_skills"].items():
    #     summary += f"\n- {skill.capitalize()}: {'Yes' if value else 'No'}"

    # summary += """

    # Accomplishments Alignment:"""

    # for accomplishment, value in data["accomplishments_alignment"].items():
    #     summary += f"\n- {accomplishment}: {'Yes' if value else 'No'}"

    # summary += """

    # Industry Knowledge:
    # - Terminology Matched: {0}
    # - Industry Experience Match: {1}""".format(
    #         ", ".join(data["industry_knowledge"]["terminology_matched"]),
    #         "Yes" if data["industry_knowledge"]["industry_experience_match"] else "No"
    #     )

    # return summary

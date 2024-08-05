OPENAI_PROMPT = """Analyze the following resume data: 
resume data: {resume} and job listing data: {job}. Give a score from 0 to 10 of how good of a fit it is. 
Keep the analysis very short, 2-3 sentences. This analysis will be displayed to the user whose resume you are analysing.
So keep the tone conversational, analytical and directly aimed at the user. If possible add the technologies by name that are related to your analysis.
Return the score in the format score/10
Please return the result in the following JSON format: {{\"text\": \"<analysis>\", \"score\": <score>}}.

Here are some examples of outputs:
{{"text": "You are a very good fit for this job offer. You might need some improvement in the cloud technologied that are listed, but apart from that it matches your resume very well.",
"score": "8/10"
}}

{{"text": "This job offer might not be very suitable for you based on your resume. There are a lot of differences in the technologies that are required.", 
"score": "2/10"
}}
"""

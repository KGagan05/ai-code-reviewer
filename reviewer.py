from transformers import pipeline

reviewer = pipeline("text2text-generation", model="google/flan-t5-base")


def review_code(code):

    prompt = f"""
You are a senior software engineer.

Review the following code and give:
- Bugs
- Improvements
- Best practices

Code:
{code}

Review:
"""

    result = reviewer(prompt, max_new_tokens=200, do_sample=False)

    return result[0]["generated_text"]
import os
from pdfminer.high_level import extract_text
import google.generativeai as genai

class CVEnhancer:
    def __init__(self, api_key):

        genai.configure(api_key=api_key)
        self.model_name = "gemini-1.5-flash"
        self.prompt_template = """
        Enhance the following CV based on the given job description. Follow these rules strictly:
        1. Highlight and expand on relevant skills, experiences, and qualifications mentioned in the CV that align with the job description.
        2. Do not fabricate any information or include anything not explicitly mentioned in the CV.
        3. Tailor the language and structure of the CV to better match the requirements of the job description.
        4. Ensure the CV remains professional, concise, and well-organized.

        Job Description: {job_description}

        CV: {cv}

        Enhanced CV:
        """

    def enhance(self, cv, job_description):
        model = genai.GenerativeModel(self.model_name)
        prompt = self.prompt_template.format(
            job_description=job_description,
            cv=cv
        )
        enhanced_cv = model.generate_content([prompt],generation_config = genai.GenerationConfig(
                max_output_tokens=1000,
                temperature=0.7,
            ))
        return enhanced_cv.text
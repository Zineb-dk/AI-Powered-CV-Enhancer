import re
from pdfminer.high_level import extract_text
import google.generativeai as genai

class CVParser:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model_name = "gemini-1.5-flash"
        self.prompt = """
        Analyze the following CV and extract all available information. Follow these rules strictly:
        1. Do not omit any details, even if the information is not titled or explicitly organized.
        2. Do not add any information that does not exist in the CV, and is not explicitly mentioned in the CV.
        3. Extract all information present in the CV,and include all of them without leaving any single one.
        4. If an information is not explicitly mentioned in the cv, just write " ".
        5. Include all possible sections like:
            Full Name: 
            Contact Information:
            - Email: 
            - Phone: 
            - Address: 
            Skills: 
            Work Experience:
            - Job Title: 
            - Company: 
            - Dates: 
            - Responsibilities:
            Education: 
            Certifications: 
            Hobbies: 
            Extracurricular Activities: 
            Projects: 
            Other Information: 

        Rules for categorizing sections:
        1. Education refers to formal qualifications from academic institutions (e.g., degrees, certifications, diplomas) and should include the institution name and graduation dates.
        2. Work Experience refers to professional job roles, which include job titles, company names, employment dates, and job responsibilities.
        3. If a piece of information mentions an institution or a course but doesn't specify job-related responsibilities, it belongs under Education.
        4. Projects, extracurricular activities, or freelance work should not be mixed with formal Education or Work Experience unless explicitly labeled.

        For each entry in the CV, answer these questions to decide the category:
        - Does the entry mention a job title, company name, and responsibilities? If yes, classify as Work Experience.
        - Does the entry mention a degree, academic institution, or course of study? If yes, classify as Education.
        - If unclear, mark it as "Uncertain" and include it in Other Information.
        """

# Function to processes the CV file and extract structured information
    def process_cv(self, cv_path):
        try:
            #Extract the cv text using extract_text from pdfminer
            cv_text = extract_text(cv_path)
        except Exception as e:
            raise ValueError(f"Error reading the PDF file: {e}")

        model = genai.GenerativeModel(self.model_name)   
        structured_cv = model.generate_content([self.prompt, cv_text],generation_config = genai.GenerationConfig(
                max_output_tokens=1000,
                temperature=0.7,
            ))
        # The structured CV will be returned in a text format
        return structured_cv.text
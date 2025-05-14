from cvparser import CVParser
from cvenhancer import CVEnhancer

if __name__ == "__main__":

    API_KEY = "YOUR_API_KEY"
    cv_pdf = "resume_path" 
    job_description = """
        We are hiring a Python Software Engineer at any seniority level, who strives for the highest engineering quality, seeks improvements, continuously develops their skills, and applies them at work. This is an exciting opportunity to work with many popular software systems, integrations technologies, and exciting open source solutions.

        The Commercial Systems unit is conceived as five engineering teams that closely collaborate with other engineering and business teams at Canonical. Services designed, developed, and operated by the Commercial Systems unit are at the heart of Canonical business and Python plays an integral role in it. We are looking for Python Software Engineers for the Integrations team.

        The Integrations team is responsible for the automation of SAAS user management and onboarding of new data sources to the data mesh. The team designs, develops, and operates a Python based solution to automate SAAS seat management and track spend across the application portfolio. Furthermore the team integrates internal and external data sources into the data mesh using open-source ETL solutions, enabling more data driven decisions in the organization.

        Location: This role will be based remotely in the EMEA region.

        The role entails

        Develop engineering solutions leveraging Python
        Collaborate with colleagues on technical designs and code reviews
        Deploy and operate services developed by the team
        Depending on your seniority, coach, mentor, and offer career development feedback
        Develop and evangelise great engineering and organisational practices


        What We Are Looking For In You

        Exceptional academic track record from both high school and university
        Undergraduate degree in a technical subject or a compelling narrative about your alternative chosen path
        Track record of going above-and-beyond expectations to achieve outstanding results 
        Experience with software development in Python
        Professional written and spoken English with excellent presentation skills
        Result-oriented, with a personal drive to meet commitments 
        Ability to travel internationally twice a year, for company events up to two weeks long


        Nice-to-have Skills

        Performance engineering and security experience
        Experience with Airbyte, Ranger, Temporal, or Trino
    """

    analyzer = CVParser(api_key=API_KEY)
    structured_cv = analyzer.process_cv(cv_pdf)

    enhancer = CVEnhancer(api_key=API_KEY)
    enhanced_cv= enhancer.enhance(structured_cv, job_description)

    print(f"Enhanced CV : {enhanced_cv}")
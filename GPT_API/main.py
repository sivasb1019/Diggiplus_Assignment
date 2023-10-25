import os
import openai
import  time
openai.api_key = os.getenv("API_KEY")

# Define the GPT-3 model
model = 'text-davinci-002'

# Configuration for prompts and section titles
PROMPTS = {
    "Objectives": "Provide a concise statement of the project objectives.",
    "Approach": "Explain the methodology and approach you will take to accomplish the project objectives.",
    "Schedule": "Outline the proposed project schedule, including major milestones and deliverables.",
    "Resources": "List the required resources, such as personnel, equipment, and technology, needed to execute the project.",
    "Risk Assessment": "Describe any potential risks or obstacles that may impact the project and outline a strategy to mitigate or manage them.",
    "Contingency Plan": "Discuss the plan to address any unforeseen circumstances or project challenges that may arise.",
    "Success Metrics": "Identify and quantify the key performance indicators that will be used to evaluate the project success."
}

# Function to interact with the GPT-3 model
def generate_text(prompt, model, max_tokens=50):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        api_key=API_KEY  # Use the API_KEY variable
    )
    return response.choices[0].text

# Create a project proposal
def create_project_proposal(project_details):
    proposal_sections = []

    for section_title, prompt in PROMPTS.items():
        section_content = generate_text(prompt, model)
        proposal_sections.append((section_title, section_content))

    project_summary = '\n'.join([f'{k}: {v}' for k, v in project_details.items()])
    proposal_sections.insert(0, ("I. Introduction", project_summary))

    return proposal_sections

# Generate and print the project proposal
if __name__ == '__main__':
    # Define project details
    project_details = {
        'Project Title': 'Online Textile Shopping',
        'Project Duration': '5',
        'Project Goals': 'USER FRIENDLY REAL TIME WEBSITE',
        'Project Roles': 'List of project roles and responsibilities',
        'Project Challenges': 'List of potential project challenges',
        'Project Success Metrics': 'User friendly with well-structured website',
    }

    proposal_sections = create_project_proposal(project_details)

    for section_title, section_content in proposal_sections:
        print(f"{section_title}\n{section_content}\n\n")
        time.sleep(2)  # Add a delay between API calls to avoid rate limits


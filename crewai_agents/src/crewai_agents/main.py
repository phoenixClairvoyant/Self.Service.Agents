#!/usr/bin/env python
import sys
import gradio as gr
from crewai_agents.crew import CrewaiAgentsCrew


def run():
    """
    Run the crew.
    """
    inputs = {
        'organization': 'Explore AI', 'task': 'How should we deploy cloud native applications?'
    }
    CrewaiAgentsCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        CrewaiAgentsCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CrewaiAgentsCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        CrewaiAgentsCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def run_crew(organization, query):
    """
    Run the crew with given inputs and return the result.
    """
    inputs = {
        'organization': organization,
        'task': query
    }
    result = CrewaiAgentsCrew().crew().kickoff(inputs=inputs)
    return result

def create_gradio_interface():
    """
    Create and launch the Gradio interface.
    """
    def copy_to_clipboard(response):
        return response

    with gr.Blocks() as ui:
        gr.Markdown("# Self service AI Agents")
        gr.Markdown("Enter the organization name and your query to get a response from the CrewAI Agents.")
        
        with gr.Row():
            org_name = gr.Textbox(label="Organization Name", value="Explore AI")
            query = gr.Textbox(label="Query", value="How should we deploy cloud native applications?")
        
        submit_btn = gr.Button("Submit")
        response = gr.Textbox(label="Response", lines=10)
        copy_btn = gr.Button("Copy Response")

        submit_btn.click(run_crew, inputs=[org_name, query], outputs=response)
        copy_btn.click(copy_to_clipboard, inputs=response, outputs=None, js="(response) => navigator.clipboard.writeText(response)")

        gr.Examples(
            examples=[
                ["Sand Enterprise", "How should we deploy cloud native applications?"],
                ["Explore AI", "What are the best practices for microservices architecture?"]
            ],
            inputs=[org_name, query]
        )

    ui.launch()

if __name__ == "__main__":
    create_gradio_interface()


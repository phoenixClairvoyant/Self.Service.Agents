from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_agents.tools.rag_tool import query_tool

# Uncomment the following line to use an example of a custom tool
# from crewai_agents.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class CrewaiAgentsCrew():
	"""CrewaiAgents crew"""

	@agent
	def software_engineer(self) -> Agent:
		return Agent(
			config=self.agents_config['software_engineer'],
            # Example of custom tool, loaded on the beginning of file
            tools=[query_tool],
            verbose=True
		)

	@agent
	def cloud_engineer(self) -> Agent:
		return Agent(
			config=self.agents_config['cloud_engineer'],
            tools = [query_tool],
            verbose=True
		)
  
	@agent
	def machine_learning_engineer(self) -> Agent:
		return Agent(
            config=self.agents_config['machine_learning_engineer'],
            tools = [query_tool],
            verbose=True
        )
  
	def manager_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['manager'],
            verbose=True,
            allow_delegation=True,
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['consult_knowledge_base'],
		)
  
	@task
	def create_implementation_plan(self):
		return Task(
            config=self.tasks_config['create_implementation_plan']
        )

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['generate_startup_template'],
			output_file='template.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CrewaiAgents crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			manager_agent=self.manager_agent(),		
			process=Process.hierarchical,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
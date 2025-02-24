from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os

@CrewBase
class ResearchCrew:
    """Research Crew"""
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["research_agent"],
            llm=LLM(
                model=os.getenv("MODEL"),
                api_key=os.getenv("ANTHROPIC_API_KEY"),
            ),
        )
    
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
            expected_output=self.tasks_config["research_task"]["expected_output"],
        )   

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""
        return Crew(
            agents=[self.research_agent()],
            tasks=[self.research_task()],
            processes=[Process.sequential],
            verbose=True,
        )

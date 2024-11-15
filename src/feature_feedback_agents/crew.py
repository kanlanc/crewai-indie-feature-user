from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import PDFSearchTool, DirectorySearchTool

@CrewBase
class FeatureFeedbackAgentsCrew():
    """FeatureFeedbackAgents crew"""

    @agent
    def feature_coordinator(self) -> Agent:
        return Agent(
            config=self.agents_config['feature_coordinator'], 
            tools=[PDFSearchTool(pdf="src/feature_feedback_agents/Feature_1.pdf")]
            
        )

    @agent
    def feedback_locator(self) -> Agent:
        return Agent(
            config=self.agents_config['feedback_locator'],
            tools=[PDFSearchTool(pdf="src/feature_feedback_agents/Feature_1.pdf")]
            
        )


    @task
    def search_feedback_in_pdfs(self) -> Task:
        return Task(
            config=self.tasks_config['search_feedback_in_pdfs'],
        )

    @task
    def compile_feedback_report(self) -> Task:
        return Task(
            config=self.tasks_config['compile_feedback_report'],
            
        )


    @crew
    def crew(self) -> Crew:
        """Creates the FeatureFeedbackAgents crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

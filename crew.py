from crewai import Crew, Process
from agents import research_specialist, content_analyst, content_writer
from tasks import research_task, analysis_task, writer_task


def run_research_crew(query: str) -> str:
    """
    Assembles and kicks off the 3-agent research crew.
    Returns the final markdown report as a string.
    """

    # 1. Instantiate agents
    researcher = research_specialist()
    analyst    = content_analyst()
    writer     = content_writer()

    # 2. Create tasks and assign each to its agent
    task_research  = research_task(researcher, query)
    task_analysis  = analysis_task(analyst, query)
    task_write     = writer_task(writer, query)

    # 3. Assemble the Crew — sequential process means tasks run one after another
    crew = Crew(
        agents=[researcher, analyst, writer],
        tasks=[task_research, task_analysis, task_write],
        process=Process.sequential,   # Research → Analysis → Write
        verbose=True,
    )

    # 4. Final Kickoff
    result = crew.kickoff()
    return str(result)
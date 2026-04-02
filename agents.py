from crewai import Agent

senior_researcher = Agent(
    role="Senior YouTube Researcher",
    goal="Explain topics simply",
    verbose=True,  # show everything in terminal
    memory=False,  # true --> remember history, false --> works fresh everytime
    backstory="Expert in simplifying AI topics.",  # adds personality
    tools=[],  # list of external tools such as youtube, search etc
    llm="ollama/llama3.1",
    allow_delegation=False  # FIX
)

script_writer = Agent(
    role="YouTube Script Writer",
    goal="Write short scripts",
    verbose=True,
    memory=False,
    backstory="Expert in writing engaging scripts.",
    tools=[],
    llm="ollama/llama3.1",
    allow_delegation=False  # FIX
)
# CrewAI Research Flow

A Python application that leverages CrewAI to create an automated research workflow. The application identifies trending AI topics and conducts detailed research using AI agents, then saves the findings to a markdown file.

## Features

- Automatic trending topic detection in AI using LiteLLM
- AI-powered research analysis using CrewAI agents
- Sequential process flow management with state handling
- Environment-based configuration
- Automated markdown report generation
- YAML-based task configuration

## Project Structure

```
crew-try/
├── src/
│   └── crew_try/
│       ├── crews/
│       │   └── research_crew/
│       │       ├── config/
│       │       │   └── tasks.yaml
│       │       │   └── agents.yaml
│       │       └── research_crew.py
│       ├── main.py
│       └── __init__.py
├── .env
├── pyproject.toml
├── uv.lock
└── README.md
```

## Prerequisites

- Python 3.11 or higher
- Anthropic API key (for Claude model access)
- UV package manager (for faster and more secure Python package management)

## Installation

1. Install UV (if not already installed):

```bash
pip install uv
```

2. Clone the repository:

```bash
git clone https://github.com/MuhammadRaffey/crew-try.git
cd crew-try
```

3. Create and activate a virtual environment:

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

4. Install dependencies:

```bash
uv sync
```

5. Create a `.env` file in the root directory with the following content:

```env
ANTHROPIC_API_KEY="your_api_key_here"
MODEL="anthropic/claude-3-5-sonnet-latest"
```

## Adding New Dependencies

To add new dependencies to the project:

```bash
uv add package_name
```

## Configuration

The application uses task configuration files:

### Task Configuration (`tasks.yaml`)

Located in `src/crew_try/crews/research_crew/config/tasks.yaml`, it defines:

- Research task description with dynamic topic injection
- Expected output format (markdown)
- Agent assignment

Example:

```yaml
research_task:
  description: >
    Research the topic provided by the user and return the most relevant information. Here is the topic: {topic}
  expected_output: >
    A list of the most relevant information with some explanation in markdown format.
  agent: research_agent
```

## Workflow

The application follows a three-step workflow:

1. **Topic Detection** (`get_topic`):

   - Uses LiteLLM to identify current trending AI topics
   - Stores the topic in the flow state

2. **Research Phase** (`get_news`):

   - Activates when topic is detected
   - Uses CrewAI agent to conduct detailed research
   - Stores research results in flow state

3. **Report Generation** (`write_to_file`):
   - Triggers after research completion
   - Generates a markdown file (`news.md`) with findings
   - Formats results in a readable markdown structure

## Usage

Run the application using:

```bash
uv run try
```

This will:

1. Identify a trending AI topic
2. Initialize the research crew
3. Conduct research on the identified topic
4. Generate a markdown report (`news.md`)

## Flow Visualization

To visualize the application flow:

```bash
uv run plot
```

## Components

### MyFlow Class

The main flow controller that:

- Identifies trending AI topics using LiteLLM
- Manages the research process and state
- Handles state transitions between steps
- Generates markdown reports

### ResearchCrew Class

A CrewAI-based research crew that:

- Configures and manages AI agents
- Defines research tasks based on YAML configuration
- Executes the research process
- Returns formatted research findings

## Development

To extend or modify the application:

1. Modify task definitions in `src/crew_try/crews/research_crew/config/tasks.yaml`
2. Extend the `ResearchCrew` class for additional functionality
3. Add new flow steps in `main.py`
4. Customize the output format in the `write_to_file` method

## Dependencies

- crewai[tools] >= 0.102.0
- python-dotenv >= 1.0.1
- litellm (for AI model interactions)
- Additional dependencies are managed through pyproject.toml and uv.lock

## License

[MIT License](LICENSE)

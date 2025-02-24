from crewai.flow.flow import Flow , start , listen
from litellm import completion
from dotenv import load_dotenv,find_dotenv
import os
from crew_try.crews.research_crew.research_crew import ResearchCrew

_:bool = load_dotenv(find_dotenv())

class MyFlow(Flow):
    @start()
    def get_topic(self):
        response = completion(
            model=os.getenv("MODEL"),
            messages=[{"role": "user", "content": "What are the Trending Topics of the AI world? Just return one very very famous topic no other text is needed."}]
        )
        self.state["topic"]=response["choices"][0]["message"]["content"]
        print(self.state["topic"])
    @listen("get_topic")
    def get_news(self):
        response = (
            ResearchCrew().crew().kickoff(inputs={"topic": self.state["topic"]})
        )
        print(response.raw)
        self.state["news"]=response
    @listen("get_news")
    def write_to_file(self):
        with open("news.md", "w") as f:
            news=self.state["news"]
            f.write(news.raw)


def kickoff():
    flow = MyFlow()
    flow.kickoff()

def plot():
    flow = MyFlow()
    flow.plot()


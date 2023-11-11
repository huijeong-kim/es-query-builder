from openai import OpenAI

class AssistantClient:
    def __init__(self, key):
        self.client = OpenAI(api_key=key)
        self.assistant = self.client.beta.assistants.create(
            name="Elasticsearch Helper",
            instructions="You are helping me with building Elasticsearch queries. Provide a proper query for the fields and requests. Don't explain, just return a query",
            tools=[{"type":"retrieval"}],
            model="gpt-4-1106-preview"
        )
        self.thread = self.client.beta.threads.create()
        
    
    def get(self, layout, query):
        message = self.client.beta.threads.messages.create(
            thread_id = self.thread.id,
            role="user",
            content=f"with doc fields {layout}, {query}"    
        )
        
        run = self.client.beta.threads.runs.create(
            thread_id = self.thread.id,
            assistant_id = self.assistant.id,
            instructions=""
        )
        
        run = self.client.beta.threads.runs.retrieve(
            thread_id = self.thread.id,
            run_id = run.id
        )
        
        messages = self.client.beta.threads.messages.list(
            thread_id=self.thread.id
        )
        
        ### how can I parse this....??
        return messages
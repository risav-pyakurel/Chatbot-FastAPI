from pydantic import BaseModel
from typing import List





class RequestState(BaseModel):
    modelName: str
    modelProvider: str
    system_prompt : str
    messages: List[str]
    allow_search: bool

from fastapi import FastAPI
from aiAgent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES = ["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4o-mini"]

app = FastAPI(title= "LangGraph AI Agent")

@app.post("/chat")
def chat_endpoint(request:RequestState):
    """
    this is the API endpoint to interact with the chatbot using LangGraph and search tools.
    It dynamically selects the model specified the model specified in the request
    """
    if request.modelName not in ALLOWED_MODEL_NAMES:
        return {"Error": "Invalid model name. Please Select a valid AI model"}
    llm_id= request.model_name
    query = request.messages
    allow_search= request.allow_search
    system_prompt = request.system_prompt
    provider = request.modelProvider
    
    
    response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port =9999)
    
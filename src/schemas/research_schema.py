from pydantic import BaseModel
from typing import Dict, Any

class TopicRequest(BaseModel):
     topic: str

class TopicResponse(BaseModel):
     search_results: str
     scraped_content: str
     report: str
     feedback: Any  
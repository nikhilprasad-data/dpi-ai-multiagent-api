# Switch

from fastapi import APIRouter, HTTPException, status

from src.services import run_research_pipeline

# schema

from src.schemas import TopicRequest, TopicResponse

research_router = APIRouter()

@research_router.post('/research',response_model= TopicResponse, status_code= status.HTTP_200_OK)
async def research_endpoint(request: TopicRequest):
     try:
          user_topic = request.topic

          pipeline_result = run_research_pipeline(topic= user_topic)

          return TopicResponse(
                    search_results=pipeline_result.get("search_results", "No search results"),
                    scraped_content=pipeline_result.get("scraped_content", "No content scraped"),
                    report=pipeline_result.get("report", "No report generated"),
                    feedback=str(pipeline_result.get("feedback", "No feedback available"))
               )

     except Exception as e:
          print(f"Pipeline error: {e}")
          raise HTTPException(
               status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
               detail=f"Research pipeline failed: {str(e)}"
          )
          
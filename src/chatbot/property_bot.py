from typing import Dict, List, Optional
import logging
from langchain_community.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
import numpy as np
import asyncio
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env'))

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PropertyBot:
    def __init__(self):
        """Initialize the PropertyBot with HuggingFace LLM."""
        try:
            # Get API token from environment
            huggingface_token = os.getenv("HUGGINGFACE_API_TOKEN")
            if not huggingface_token:
                raise ValueError("HUGGINGFACE_API_TOKEN not found in environment variables")

            # Initialize HuggingFace LLM
            self.llm = HuggingFaceHub(
                repo_id="google/flan-t5-large",  # Free and good for text generation
                model_kwargs={"temperature": 0.7, "max_length": 512},
                huggingfacehub_api_token=huggingface_token
            )
            self.setup_chains()
            logger.info("PropertyBot initialized successfully")
        except Exception as e:
            error_message = str(e)
            if "token" in error_message.lower():
                logger.error("""
                HuggingFace API token not found in .env file. Please ensure:
                1. You have a .env file in the project root
                2. The file contains: HUGGINGFACE_API_TOKEN=your_token
                3. The token is valid
                Error: %s
                """, error_message)
            else:
                logger.error("Failed to initialize PropertyBot: %s", error_message)
            raise RuntimeError(
                "Failed to initialize PropertyBot. Please check your .env file and HuggingFace API token."
            )

    def setup_chains(self):
        """Set up LangChain chains for different property analysis tasks."""
        self.property_analysis_prompt = PromptTemplate(
            input_variables=["property_details", "user_preferences"],
            template="""
            Task: Analyze a property based on user preferences and provide a detailed recommendation.
            
            Property Details: {property_details}
            User Preferences: {user_preferences}
            
            Please provide a comprehensive analysis covering:
            1. Location & accessibility
            2. Market dynamics
            3. Property features
            4. Amenities & facilities
            5. Environmental factors
            6. Financial aspects
            7. Developer reputation
            8. Technology features
            9. Risk factors
            10. Economic indicators
            
            End with a clear recommendation and an overall score out of 100.
            Keep the response concise but informative.
            """
        )
        
        # Create a runnable sequence
        self.property_analysis_chain = RunnableSequence(
            self.property_analysis_prompt | self.llm
        )

    def calculate_property_score(self, property_data: Dict) -> float:
        """Calculate weighted score for a property."""
        try:
            # Define default weights for different categories
            weights = {
                "location": 0.2,
                "market": 0.15,
                "features": 0.15,
                "amenities": 0.1,
                "environmental": 0.1,
                "financial": 0.1,
                "developer": 0.05,
                "tech": 0.05,
                "risk": 0.05,
                "economic": 0.05
            }
            
            scores = {
                "location": min(
                    (property_data.get("location", {}).get("walkability_score", 0) +
                     property_data.get("location", {}).get("transit_score", 0)) / 2,
                    100
                ),
                "market": min(
                    100 - property_data.get("market_metrics", {}).get("vacancy_rate", 0) * 10,
                    100
                ),
                "features": property_data.get("features", {}).get("construction_quality", 0),
                "amenities": 100 if property_data.get("amenities", {}).get("available_facilities") else 0,
                "environmental": float(property_data.get("environmental", {}).get("air_quality_index", 0)),
                "financial": min(property_data.get("financial", {}).get("estimated_roi", 0) * 10, 100),
                "developer": property_data.get("developer", {}).get("success_rate", 0),
                "tech": property_data.get("tech_features", {}).get("tech_readiness_score", 0),
                "risk": 100 - property_data.get("risk_assessment", {}).get("market_risk", 0),
                "economic": property_data.get("economic_indicators", {}).get("political_stability_index", 0)
            }
            
            total_score = sum(weights[k] * scores[k] for k in weights)
            return round(total_score, 2)
            
        except Exception as e:
            logger.error(f"Error calculating property score: {str(e)}")
            return 0.0

    async def get_property_recommendation(
        self,
        property_details: Dict,
        user_preferences: Dict
    ) -> Dict:
        """Get property recommendations based on user preferences."""
        try:
            # Calculate property score
            score = self.calculate_property_score(property_details)
            
            # Get AI analysis
            analysis = await self.property_analysis_chain.ainvoke({
                "property_details": str(property_details),
                "user_preferences": str(user_preferences)
            })
            
            return {
                "score": score,
                "analysis": analysis,
                "recommendation": "Highly Recommended" if score >= 80 else
                               "Recommended" if score >= 60 else
                               "Consider with Caution" if score >= 40 else
                               "Not Recommended",
                "details": {
                    "property_id": property_details.get("id"),
                    "location": property_details.get("location", {}),
                    "features": property_details.get("features", {})
                }
            }
        except Exception as e:
            logger.error(f"Error in property recommendation: {str(e)}")
            return {
                "score": 0,
                "analysis": f"Error analyzing property: {str(e)}",
                "recommendation": "Error",
                "details": {"error": str(e)}
            }

    async def compare_properties(
        self,
        properties: List[Dict],
        user_preferences: Dict
    ) -> Dict:
        """Compare multiple properties based on user preferences."""
        try:
            results = []
            for prop in properties:
                analysis = await self.get_property_recommendation(prop, user_preferences)
                results.append({
                    "property_id": prop.get("id"),
                    "neighborhood": prop.get("location", {}).get("neighborhood"),
                    "score": analysis["score"],
                    "analysis": analysis["analysis"],
                    "recommendation": analysis["recommendation"]
                })
            
            # Sort results by score
            results.sort(key=lambda x: x["score"], reverse=True)
            
            return {
                "comparisons": results,
                "best_match": results[0] if results else None,
                "summary": f"Analyzed {len(results)} properties based on your preferences.",
                "score_difference": round(results[0]["score"] - results[-1]["score"], 2) if len(results) > 1 else 0
            }
        except Exception as e:
            logger.error(f"Error in property comparison: {str(e)}")
            return {
                "error": str(e),
                "comparisons": [],
                "best_match": None,
                "summary": f"Error comparing properties: {str(e)}"
            }

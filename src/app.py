import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import asyncio
import sys
import os
from dotenv import load_dotenv

# Add the src directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load environment variables from root .env file
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env'))

from src.chatbot.property_bot import PropertyBot
from src.models.property import Property, Location, MarketMetrics, PropertyFeatures, Amenities, Environmental, Financial, DeveloperInfo, TechFeatures, RiskAssessment, EconomicIndicators
from src.visualization.property_viz import PropertyVisualizer

# Page configuration
st.set_page_config(
    page_title="RightHome.ai Property Assistant",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'property_bot' not in st.session_state:
    try:
        with st.spinner('Initializing Property Assistant...'):
            # Check for HuggingFace API token
            huggingface_token = os.getenv("HUGGINGFACE_API_TOKEN")
            if not huggingface_token:
                st.error("""
                HuggingFace API token not found in .env file!
                
                Please ensure:
                1. You have a .env file in the project root
                2. The file contains: HUGGINGFACE_API_TOKEN=your_token
                3. The token is valid
                """)
                st.session_state.bot_initialized = False
                st.session_state.property_bot = None
            else:
                st.session_state.property_bot = PropertyBot()
                st.session_state.bot_initialized = True
                st.success('Property Assistant initialized successfully! You can now start chatting.')
    except Exception as e:
        error_msg = str(e)
        st.error(f"""
        Error initializing Property Assistant:
        
        {error_msg}
        
        Please check your .env file and ensure the HuggingFace API token is valid.
        """)
        st.session_state.bot_initialized = False
        st.session_state.property_bot = None

if 'property_viz' not in st.session_state:
    st.session_state.property_viz = PropertyVisualizer()

def save_chat_history(user_input, bot_response):
    """Save chat interaction to history."""
    st.session_state.chat_history.append({
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'user_input': user_input,
        'bot_response': bot_response
    })

def create_sample_property(property_id="prop123", neighborhood="Mission District"):
    """Create a sample property for demonstration."""
    try:
        return Property(
            id=property_id,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            location=Location(
                city="San Francisco",
                neighborhood=neighborhood,
                coordinates={"lat": 37.7749, "lng": -122.4194},
                walkability_score=85.0,
                transit_score=90.0,
                parking_available=True
            ),
            market_metrics=MarketMetrics(
                vacancy_rate=5.2,
                rental_yield=4.8,
                price_trend=12.5,
                competition_level="Medium"
            ),
            features=PropertyFeatures(
                property_type="Apartment",
                size_sqft=1200.0,
                num_bedrooms=2,
                num_bathrooms=2.0,
                year_built=2015,
                construction_quality=85.0,
                space_efficiency=90.0
            ),
            amenities=Amenities(
                green_certification=True,
                onsite_management=True,
                security_features=["24/7 Security", "CCTV", "Access Control"],
                available_facilities=["Gym", "Pool", "Parking"]
            ),
            environmental=Environmental(
                air_quality_index=75.0,
                noise_level_db=45.0,
                green_space_proximity=0.5,
                energy_efficiency_rating="A"
            ),
            financial=Financial(
                purchase_price=850000.0,
                monthly_operating_costs=2500.0,
                tax_rate=1.2,
                estimated_roi=6.5,
                available_financing=["Conventional", "FHA", "VA"]
            ),
            developer=DeveloperInfo(
                name="Quality Builders Inc.",
                years_active=25,
                completed_projects=50,
                success_rate=95.0,
                financial_stability_rating="A+"
            ),
            tech_features=TechFeatures(
                smart_home_features=["Smart Thermostat", "Smart Locks", "Smart Lighting"],
                internet_speed=1000.0,
                automation_systems=["HVAC", "Security", "Lighting"],
                tech_readiness_score=90.0
            ),
            risk_assessment=RiskAssessment(
                market_risk=25.0,
                financial_risk=20.0,
                regulatory_risk=15.0,
                environmental_risk=10.0
            ),
            economic_indicators=EconomicIndicators(
                gdp_growth=3.5,
                employment_rate=95.0,
                population_growth=2.1,
                political_stability_index=85.0
            )
        )
    except Exception as e:
        st.error(f"Error creating sample property: {str(e)}")
        return None

def handle_chat_input(user_input: str):
    """Handle chat input and generate response."""
    if not st.session_state.bot_initialized:
        return "Please make sure Ollama is running and the model is downloaded."
    
    try:
        # Create sample property
        property_data = create_sample_property()
        if property_data is None:
            return "Error creating property data for analysis."
        
        # Convert property to dictionary format
        property_dict = property_data.to_dict()
        
        # Process user input and get response
        response = asyncio.run(st.session_state.property_bot.get_property_recommendation(
            property_details=property_dict,
            user_preferences={"input": user_input}
        ))
        
        if "error" in response:
            return f"Error: {response['error']}"
        
        # Format response
        analysis = response.get("analysis", "No analysis available")
        score = response.get("score", 0)
        recommendation = response.get("recommendation", "No recommendation available")
        
        return f"""
        Analysis: {analysis}
        
        Property Score: {score}/100
        Recommendation: {recommendation}
        """
    except Exception as e:
        st.error(f"Error processing request: {str(e)}")
        return "I encountered an error while processing your request. Please try again."

# Sidebar
with st.sidebar:
    st.title("💬 Chat History")
    
    # Add filters for history
    st.subheader("Filters")
    date_filter = st.date_input("Filter by date")
    
    # Display chat history
    st.subheader("Recent Conversations")
    for chat in reversed(st.session_state.chat_history[-10:]):  # Show last 10 conversations
        with st.expander(f"🕒 {chat['timestamp']}", expanded=False):
            st.write("**You:** " + chat['user_input'])
            st.write("**Assistant:** " + str(chat['bot_response']))

# Main content
st.title("🏠 RightHome.ai Property Assistant")

# Add tabs
tab1, tab2, tab3 = st.tabs(["Chat", "Property Analysis", "Comparisons"])

with tab1:
    st.header("Chat with Property Assistant")
    
    user_input = st.text_input("Ask me about properties:", key="chat_input")
    
    if st.button("Send", key="send_button"):
        if user_input:
            response = handle_chat_input(user_input)
            st.write("**Assistant:**", response)
            save_chat_history(user_input, response)

with tab2:
    st.header("Property Analysis")
    
    with st.form("property_analysis_form"):
        st.subheader("Enter Property Details")
        
        col1, col2 = st.columns(2)
        
        with col1:
            property_type = st.selectbox("Property Type", ["Apartment", "House", "Condo", "Townhouse"])
            price = st.number_input("Price ($)", min_value=0, value=500000)
            size = st.number_input("Size (sq ft)", min_value=0, value=1000)
        
        with col2:
            city = st.text_input("City", "San Francisco")
            neighborhood = st.text_input("Neighborhood", "Mission District")
        
        if st.form_submit_button("Analyze Property"):
            with st.spinner("Analyzing property..."):
                try:
                    sample_property = create_sample_property()
                    if sample_property and st.session_state.property_bot:
                        analysis = asyncio.run(st.session_state.property_bot.get_property_recommendation(
                            sample_property.dict(),
                            {"location_importance": 0.3, "price_importance": 0.4, "amenities_importance": 0.3}
                        ))
                        
                        st.success("Analysis complete!")
                        st.json(analysis)
                        
                        # Create and display visualization
                        fig = st.session_state.property_viz.create_radar_chart(
                            [sample_property.dict()],
                            ["walkability_score", "transit_score", "construction_quality", "space_efficiency"]
                        )
                        st.plotly_chart(fig)
                except Exception as e:
                    st.error(f"Error in analysis: {str(e)}")

with tab3:
    st.header("Property Comparisons")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Property 1")
        property1_neighborhood = st.text_input("Neighborhood 1", "Mission District")
    
    with col2:
        st.subheader("Property 2")
        property2_neighborhood = st.text_input("Neighborhood 2", "Pacific Heights")
    
    if st.button("Compare Properties"):
        with st.spinner("Comparing properties..."):
            try:
                property1 = create_sample_property("prop123", property1_neighborhood)
                property2 = create_sample_property("prop456", property2_neighborhood)
                
                if property1 and property2 and st.session_state.property_bot:
                    comparison = asyncio.run(st.session_state.property_bot.compare_properties(
                        [property1.dict(), property2.dict()],
                        {"location_importance": 0.3, "price_importance": 0.4, "amenities_importance": 0.3}
                    ))
                    
                    st.success("Comparison complete!")
                    st.json(comparison)
                    
                    # Create and display comparison visualization
                    fig = st.session_state.property_viz.create_radar_chart(
                        [property1.dict(), property2.dict()],
                        ["walkability_score", "transit_score", "construction_quality", "space_efficiency"]
                    )
                    st.plotly_chart(fig)
            except Exception as e:
                st.error(f"Error in comparison: {str(e)}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by RightHome.ai Team")

# API Documentation

This document details the core APIs and components of RightHome.ai.

## Core Components

### PropertyBot

The main AI-powered analysis engine.

#### Initialization
```python
from src.chatbot.property_bot import PropertyBot

bot = PropertyBot()
```

#### Methods

##### get_property_recommendation
```python
async def get_property_recommendation(
    self,
    property_details: Dict,
    user_preferences: Dict
) -> Dict:
```
Analyzes a property and provides recommendations.

**Parameters:**
- `property_details`: Property information dictionary
- `user_preferences`: User preference settings

**Returns:**
```python
{
    "score": float,  # 0-100
    "analysis": str,  # Detailed analysis
    "recommendation": str,  # Recommendation category
    "details": {
        "property_id": str,
        "location": Dict,
        "features": Dict
    }
}
```

##### compare_properties
```python
async def compare_properties(
    self,
    properties: List[Dict],
    user_preferences: Dict
) -> Dict:
```
Compares multiple properties.

**Parameters:**
- `properties`: List of property dictionaries
- `user_preferences`: User preference settings

**Returns:**
```python
{
    "comparisons": List[Dict],  # Individual analyses
    "best_match": Dict,  # Best property match
    "summary": str,  # Comparison summary
    "score_difference": float  # Score spread
}
```

### PropertyVisualizer

Handles all visualization components.

#### Initialization
```python
from src.visualization.property_viz import PropertyVisualizer

visualizer = PropertyVisualizer()
```

#### Methods

##### create_radar_chart
```python
def create_radar_chart(
    self,
    properties: List[Dict],
    metrics: List[str]
) -> go.Figure:
```
Creates a radar chart comparison.

**Parameters:**
- `properties`: List of property dictionaries
- `metrics`: List of metrics to compare

**Returns:**
- Plotly Figure object

##### create_heatmap
```python
def create_heatmap(
    self,
    property_data: Dict
) -> go.Figure:
```
Creates a score heatmap.

**Parameters:**
- `property_data`: Property scores dictionary

**Returns:**
- Plotly Figure object

##### create_bar_comparison
```python
def create_bar_comparison(
    self,
    properties: List[Dict],
    metric: str,
    title: str = None
) -> go.Figure:
```
Creates a bar chart comparison.

**Parameters:**
- `properties`: List of property dictionaries
- `metric`: Metric to compare
- `title`: Optional custom title

**Returns:**
- Plotly Figure object

## Data Models

### Property
```python
class Property(BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    location: Location
    market_metrics: MarketMetrics
    features: PropertyFeatures
    amenities: Amenities
    environmental: Environmental
    financial: Financial
    developer: DeveloperInfo
    tech_features: TechFeatures
    risk_assessment: RiskAssessment
    economic_indicators: EconomicIndicators
```

### Location
```python
class Location(BaseModel):
    city: str
    neighborhood: str
    coordinates: Dict[str, float]
    walkability_score: float
    transit_score: float
    parking_available: bool
```

### MarketMetrics
```python
class MarketMetrics(BaseModel):
    vacancy_rate: float
    rental_yield: float
    price_trend: float
    competition_level: str
```

## Integration

### Model Integration
```python
from src.models.custom_model import CustomModel

model = CustomModel(
    model_kwargs={"temperature": 0.7}
)
```

### Streamlit Integration
```python
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="RightHome.ai Property Assistant",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)
```

## Error Handling

### Common Errors

1. **Model Error**
```python
if not model_initialized:
    raise ValueError("Model not initialized correctly")
```

2. **Property Validation**
```python
try:
    property_data = Property(**data)
except ValidationError as e:
    logger.error(f"Invalid property data: {e}")
```

3. **API Errors**
```python
try:
    analysis = await self.property_analysis_chain.ainvoke(params)
except Exception as e:
    logger.error(f"Analysis failed: {e}")
    return {"error": str(e)}
```

## Best Practices

1. **Async Operations**
   - Use async/await for API calls
   - Handle timeouts appropriately
   - Implement proper error handling

2. **Data Validation**
   - Use Pydantic models
   - Validate all inputs
   - Handle missing data gracefully

3. **Visualization**
   - Implement responsive designs
   - Handle large datasets efficiently
   - Provide interactive features

4. **Security**
   - Use environment variables
   - Validate user inputs
   - Implement rate limiting

## Examples

### Property Analysis
```python
# Create property bot
bot = PropertyBot()

# Analyze property
result = await bot.get_property_recommendation(
    property_details=property_data,
    user_preferences={"location_importance": 0.3}
)

# Visualize results
viz = PropertyVisualizer()
fig = viz.create_radar_chart(
    [property_data],
    ["walkability_score", "transit_score"]
)
```

### Property Comparison
```python
# Compare properties
comparison = await bot.compare_properties(
    properties=[property1, property2],
    user_preferences={"price_importance": 0.4}
)

# Visualize comparison
fig = viz.create_bar_comparison(
    [property1, property2],
    "features.construction_quality"
)

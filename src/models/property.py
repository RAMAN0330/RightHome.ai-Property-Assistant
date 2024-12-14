from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class Location(BaseModel):
    city: str
    neighborhood: str
    coordinates: Dict[str, float]
    walkability_score: float = Field(ge=0, le=100)
    transit_score: float = Field(ge=0, le=100)
    parking_available: bool

class MarketMetrics(BaseModel):
    vacancy_rate: float = Field(ge=0, le=100)
    rental_yield: float = Field(ge=0)
    price_trend: float
    competition_level: str

class PropertyFeatures(BaseModel):
    property_type: str
    size_sqft: float
    num_bedrooms: int
    num_bathrooms: float
    year_built: int
    construction_quality: float = Field(ge=0, le=100)
    space_efficiency: float = Field(ge=0, le=100)

class Amenities(BaseModel):
    green_certification: bool
    onsite_management: bool
    security_features: List[str]
    available_facilities: List[str]

class Environmental(BaseModel):
    air_quality_index: float = Field(ge=0, le=100)
    noise_level_db: float = Field(ge=0, le=120)
    green_space_proximity: float = Field(ge=0, le=1)
    energy_efficiency_rating: str

class Financial(BaseModel):
    purchase_price: float = Field(ge=0)
    monthly_operating_costs: float = Field(ge=0)
    tax_rate: float = Field(ge=0)
    estimated_roi: float
    available_financing: List[str]

class DeveloperInfo(BaseModel):
    name: str
    years_active: int = Field(ge=0)
    completed_projects: int = Field(ge=0)
    success_rate: float = Field(ge=0, le=100)
    financial_stability_rating: str

class TechFeatures(BaseModel):
    smart_home_features: List[str]
    internet_speed: float = Field(ge=0)
    automation_systems: List[str]
    tech_readiness_score: float = Field(ge=0, le=100)

class RiskAssessment(BaseModel):
    market_risk: float = Field(ge=0, le=100)
    financial_risk: float = Field(ge=0, le=100)
    regulatory_risk: float = Field(ge=0, le=100)
    environmental_risk: float = Field(ge=0, le=100)

class EconomicIndicators(BaseModel):
    gdp_growth: float
    employment_rate: float = Field(ge=0, le=100)
    population_growth: float
    political_stability_index: float = Field(ge=0, le=100)

class Property(BaseModel):
    id: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
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
    
    class Config:
        arbitrary_types_allowed = True
        
    def to_dict(self) -> Dict:
        """Convert property model to dictionary format."""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "location": self.location.dict(),
            "market_metrics": self.market_metrics.dict(),
            "features": self.features.dict(),
            "amenities": self.amenities.dict(),
            "environmental": self.environmental.dict(),
            "financial": self.financial.dict(),
            "developer": self.developer.dict(),
            "tech_features": self.tech_features.dict(),
            "risk_assessment": self.risk_assessment.dict(),
            "economic_indicators": self.economic_indicators.dict()
        }

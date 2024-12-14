import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import List, Dict

class PropertyVisualizer:
    def __init__(self):
        """Initialize the PropertyVisualizer."""
        self.color_scheme = px.colors.qualitative.Set3

    def create_radar_chart(self, properties: List[Dict], metrics: List[str]) -> go.Figure:
        """
        Create a radar chart comparing multiple properties across different metrics.
        
        Args:
            properties: List of property dictionaries
            metrics: List of metrics to compare
            
        Returns:
            go.Figure: Plotly radar chart
        """
        fig = go.Figure()
        
        for i, prop in enumerate(properties):
            # Extract nested values based on metric path
            values = []
            for metric in metrics:
                # Handle nested paths (e.g., "location.walkability_score")
                parts = metric.split('.')
                value = prop
                for part in parts:
                    value = value.get(part, {}) if isinstance(value, dict) else 0
                values.append(float(value) if isinstance(value, (int, float)) else 0)
            
            # Create trace for property
            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=metrics,
                name=f"Property {prop.get('id', i+1)}",
                line=dict(color=self.color_scheme[i % len(self.color_scheme)]),
                fill='toself'
            ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    showticklabels=True,
                    ticksuffix="%"
                )
            ),
            showlegend=True,
            title="Property Comparison Radar Chart",
            height=600
        )
        
        return fig

    def create_heatmap(self, property_data: Dict) -> go.Figure:
        """
        Create a heatmap showing property scores across different categories.
        
        Args:
            property_data: Dictionary containing property scores
            
        Returns:
            go.Figure: Plotly heatmap
        """
        # Extract relevant scores
        categories = [
            'Location', 'Market', 'Features', 'Amenities',
            'Environmental', 'Financial', 'Developer', 'Tech'
        ]
        
        scores = [
            (property_data.get('location', {}).get('walkability_score', 0) +
             property_data.get('location', {}).get('transit_score', 0)) / 2,
            100 - property_data.get('market_metrics', {}).get('vacancy_rate', 0) * 10,
            property_data.get('features', {}).get('construction_quality', 0),
            100 if property_data.get('amenities', {}).get('available_facilities') else 0,
            float(property_data.get('environmental', {}).get('air_quality_index', 0)),
            min(property_data.get('financial', {}).get('estimated_roi', 0) * 10, 100),
            property_data.get('developer', {}).get('success_rate', 0),
            property_data.get('tech_features', {}).get('tech_readiness_score', 0)
        ]
        
        fig = go.Figure(data=go.Heatmap(
            z=[scores],
            x=categories,
            y=['Scores'],
            colorscale='RdYlGn',
            showscale=True,
            text=[[f"{score:.1f}%" for score in scores]],
            texttemplate="%{text}",
            textfont={"size": 12},
            textcolor="black"
        ))
        
        fig.update_layout(
            title="Property Score Heatmap",
            xaxis_title="Categories",
            yaxis_title="Property",
            height=300
        )
        
        return fig

    def create_bar_comparison(self, properties: List[Dict], metric: str, title: str = None) -> go.Figure:
        """
        Create a bar chart comparing a specific metric across properties.
        
        Args:
            properties: List of property dictionaries
            metric: Metric to compare (e.g., 'financial.estimated_roi')
            title: Custom title for the chart
            
        Returns:
            go.Figure: Plotly bar chart
        """
        property_ids = [p.get('id', f'Property {i+1}') for i, p in enumerate(properties)]
        
        # Extract nested values
        values = []
        for prop in properties:
            parts = metric.split('.')
            value = prop
            for part in parts:
                value = value.get(part, {}) if isinstance(value, dict) else 0
            values.append(float(value) if isinstance(value, (int, float)) else 0)
        
        fig = go.Figure(data=go.Bar(
            x=property_ids,
            y=values,
            marker_color=self.color_scheme[:len(properties)],
            text=[f"{v:.1f}" for v in values],
            textposition='auto'
        ))
        
        metric_label = metric.replace('_', ' ').title()
        fig.update_layout(
            title=title or f"{metric_label} Comparison",
            xaxis_title="Properties",
            yaxis_title=metric_label,
            height=400,
            showlegend=False
        )
        
        return fig

    def create_scatter_matrix(self, properties: List[Dict], metrics: List[str]) -> go.Figure:
        """
        Create a scatter matrix comparing multiple metrics across properties.
        
        Args:
            properties: List of property dictionaries
            metrics: List of metrics to compare
            
        Returns:
            go.Figure: Plotly scatter matrix
        """
        # Extract data for each metric
        data = {metric: [] for metric in metrics}
        for prop in properties:
            for metric in metrics:
                parts = metric.split('.')
                value = prop
                for part in parts:
                    value = value.get(part, {}) if isinstance(value, dict) else 0
                data[metric].append(float(value) if isinstance(value, (int, float)) else 0)
        
        df = pd.DataFrame(data)
        fig = px.scatter_matrix(
            df,
            dimensions=metrics,
            title="Property Metrics Scatter Matrix",
            labels={col: col.replace('_', ' ').title() for col in metrics}
        )
        
        fig.update_traces(diagonal_visible=False)
        fig.update_layout(height=800)
        return fig

    def create_timeline(self, property_data: Dict) -> go.Figure:
        """
        Create a timeline visualization of property history and projections.
        
        Args:
            property_data: Dictionary containing property timeline data
            
        Returns:
            go.Figure: Plotly timeline
        """
        events = property_data.get('timeline', [])
        if not events:  # Create sample timeline if none exists
            events = [
                {'date': property_data.get('created_at', ''), 'description': 'Property Listed'},
                {'date': property_data.get('updated_at', ''), 'description': 'Last Updated'}
            ]
        
        dates = [event['date'] for event in events]
        descriptions = [event['description'] for event in events]
        
        fig = go.Figure(data=go.Scatter(
            x=dates,
            y=[1] * len(dates),
            mode='markers+text',
            text=descriptions,
            textposition='top center',
            marker=dict(size=12, symbol='diamond')
        ))
        
        fig.update_layout(
            title="Property Timeline",
            showlegend=False,
            yaxis={'visible': False},
            height=200,
            margin=dict(t=50, b=20)
        )
        
        return fig

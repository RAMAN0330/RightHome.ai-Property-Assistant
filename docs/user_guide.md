# User Guide

This guide explains how to use RightHome.ai's features effectively.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Property Analysis](#property-analysis)
3. [Property Comparison](#property-comparison)
4. [Visualization Guide](#visualization-guide)
5. [Best Practices](#best-practices)

## Getting Started

### Launching the Application
1. Open your terminal
2. Navigate to the project directory
3. Run: `python -m streamlit run src/app.py`
4. The application will open in your default browser

### Interface Overview
- **Chat Tab**: Direct interaction with the AI assistant
- **Property Analysis Tab**: Analyze individual properties
- **Comparisons Tab**: Compare multiple properties
- **Sidebar**: Access chat history and filters

## Property Analysis

### Single Property Analysis
1. Navigate to the "Property Analysis" tab
2. Fill in property details:
   - Property Type
   - Price
   - Size
   - Location details
3. Click "Analyze Property"

### Analysis Results
You'll see three tabs:

1. **Overview**
   - Radar chart showing key metrics
   - Interactive legend
   - Hover for detailed values

2. **Detailed Scores**
   - Heatmap of all scores
   - Color-coded performance indicators
   - Comprehensive analysis text
   - Overall score and recommendation

3. **Timeline**
   - Property history visualization
   - Key events and dates
   - Interactive timeline

## Property Comparison

### Comparing Properties
1. Go to "Property Comparisons" tab
2. Enter details for both properties:
   - Neighborhood
   - Property type
   - Price range
3. Click "Compare Properties"

### Comparison Views

1. **Overview**
   - Side-by-side radar chart
   - Key metrics comparison
   - Interactive legend

2. **Detailed Comparison**
   - Bar charts for key metrics
   - Direct metric comparisons
   - Value labels

3. **Metrics**
   - Scatter matrix
   - Correlation analysis
   - Interactive tooltips

## Visualization Guide

### Radar Charts
- **Purpose**: Compare multiple metrics simultaneously
- **Usage**: 
  - Hover over points for values
  - Click legend to show/hide properties
  - Double-click to reset view

### Heatmaps
- **Purpose**: Show performance across categories
- **Features**:
  - Color intensity shows performance
  - Hover for exact values
  - Click to zoom

### Bar Charts
- **Purpose**: Direct metric comparisons
- **Features**:
  - Value labels
  - Interactive tooltips
  - Custom color schemes

### Scatter Matrix
- **Purpose**: Analyze metric relationships
- **Usage**:
  - Click and drag to zoom
  - Double-click to reset
  - Hover for details

## Best Practices

### Property Analysis
1. **Complete Information**
   - Provide as much detail as possible
   - Use accurate measurements
   - Include recent updates

2. **Context Matters**
   - Consider neighborhood trends
   - Include market conditions
   - Note special features

### Comparison Tips
1. **Similar Properties**
   - Compare properties in similar price ranges
   - Consider location differences
   - Note age and condition variations

2. **Multiple Metrics**
   - Don't focus on single metrics
   - Consider all aspects
   - Weight factors based on importance

### Data Interpretation
1. **Score Context**
   - Scores are relative
   - Consider local market
   - Factor in property type

2. **Recommendations**
   - Read full analysis
   - Consider all factors
   - Use as guidance, not absolute truth

## Tips and Tricks

1. **Efficient Analysis**
   - Save common property types
   - Use filters effectively
   - Export results when needed

2. **Better Comparisons**
   - Compare similar properties
   - Use consistent criteria
   - Note significant differences

3. **Visualization Usage**
   - Customize views as needed
   - Export charts for presentations
   - Use interactive features

## Support

For additional help:
1. Check the [FAQ](faq.md)
2. Visit the GitHub repository
3. Contact support team

## Updates and Feedback

- Check for regular updates
- Submit feature requests
- Report issues on GitHub
- Provide feedback for improvements

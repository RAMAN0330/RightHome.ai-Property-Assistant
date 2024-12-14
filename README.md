# RightHome.ai Property Recommendation Assistant

An AI-powered property recommendation system for intelligent property analysis and comparison.

## 🌟 Features

- **Smart Property Analysis**: Advanced analysis of properties based on 10+ key parameters
- **Interactive Visualizations**: 
  - Radar charts for property comparisons
  - Heatmaps for score visualization
  - Bar charts for metric comparisons
  - Scatter matrices for detailed analysis
  - Timeline views for property history
- **AI-Powered Recommendations**: Intelligent property insights and recommendations
- **Real-time Analysis**: Instant property scoring and comparison
- **User-friendly Interface**: Built with Streamlit for a seamless experience

## 📊 Parameters Analyzed

1. **Location & Accessibility**
   - Walkability score
   - Transit score
   - Parking availability
   - Neighborhood quality

2. **Market Dynamics**
   - Vacancy rates
   - Rental yield
   - Price trends
   - Competition level

3. **Property Features**
   - Size and layout
   - Construction quality
   - Age and condition
   - Space efficiency

4. **Amenities & Facilities**
   - Available facilities
   - Green certification
   - Security features
   - Management services

5. **Environmental Factors**
   - Air quality
   - Noise levels
   - Green space proximity
   - Energy efficiency

6. **Financial Aspects**
   - Purchase price
   - Operating costs
   - Tax considerations
   - ROI estimates

7. **Developer Information**
   - Track record
   - Years active
   - Success rate
   - Financial stability

8. **Technology Features**
   - Smart home capabilities
   - Internet connectivity
   - Automation systems
   - Tech readiness

9. **Risk Assessment**
   - Market risks
   - Financial risks
   - Regulatory compliance
   - Environmental risks

10. **Economic Indicators**
    - GDP growth impact
    - Employment rates
    - Population growth
    - Political stability

## 🚀 Quick Start

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/RightHome.git
cd RightHome
```

2. **Set up environment:**
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the application:**
```bash
python -m streamlit run src/app.py
```

## 📁 Project Structure

```
RightHome/
├── src/
│   ├── chatbot/
│   │   └── property_bot.py    # Core AI functionality
│   ├── models/
│   │   └── property.py        # Data models
│   ├── visualization/
│   │   └── property_viz.py    # Visualization components
│   └── app.py                 # Streamlit application
├── requirements.txt           # Project dependencies
└── README.md                 # Documentation
```

## 💻 Usage

### Property Analysis
1. Navigate to the "Property Analysis" tab
2. Enter property details
3. Click "Analyze Property"
4. View the analysis across three tabs:
   - Overview (Radar Chart)
   - Detailed Scores (Heatmap)
   - Timeline

### Property Comparison
1. Go to the "Property Comparisons" tab
2. Enter details for two properties
3. Click "Compare Properties"
4. Explore the comparison across:
   - Overview (Radar Chart)
   - Detailed Comparison (Bar Charts)
   - Metrics (Scatter Matrix)

## 🔧 Configuration

### Model Configuration
The system uses a custom model for property analysis, which can be configured in `property_bot.py`:
```python
self.model = CustomModel()
```

## 📈 Visualization Components

### Radar Chart
- Compares multiple properties across different metrics
- Interactive legend
- Percentage-based scaling
- Filled areas for better visualization

### Heatmap
- Shows property scores across categories
- Color-coded for easy interpretation
- Includes actual values as labels
- Responsive design

### Bar Charts
- Compares specific metrics between properties
- Includes value labels
- Custom color schemes
- Adjustable titles and axes

### Scatter Matrix
- Advanced metric correlation analysis
- Interactive tooltips
- Customizable dimensions
- Auto-scaling

### Timeline
- Property history visualization
- Key events marking
- Custom styling
- Automatic date formatting

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Streamlit for the amazing web framework
- Plotly for interactive visualizations
- The open-source community for inspiration and tools
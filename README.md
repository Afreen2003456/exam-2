# Airline Data Analytics Dashboard

A comprehensive web application for analyzing airline booking data, flight trends, and market insights. Built with Flask, Python, and modern web technologies.

![Airline Analytics Dashboard](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🚀 Features

- **Real-time Data Scraping**: Fetches airline data from public APIs and web sources
- **Interactive Dashboard**: Modern, responsive web interface with charts and visualizations
- **Data Processing**: Automated data cleaning and insight generation
- **Popular Routes Analysis**: Identifies trending flight routes and destinations
- **Airline Performance Metrics**: Analyzes airline distribution and market share
- **Peak Time Analysis**: Determines high-demand periods and optimal booking times
- **Airport Activity Monitoring**: Tracks busiest airports and hub performance
- **Filtering & Search**: Advanced filtering options for customized data views

## 📋 Requirements

- Python 3.8 or higher
- Flask 2.3.3+
- Internet connection for API calls
- Modern web browser (Chrome, Firefox, Safari, Edge)

## 🛠️ Installation

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd airline-analytics-dashboard
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (Optional)
   ```bash
   # Create a .env file in the project root
   echo "AVIATIONSTACK_API_KEY=your_api_key_here" > .env
   echo "OPENAI_API_KEY=your_openai_key_here" >> .env
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

### API Keys Setup (Optional)

The application works with mock data by default, but you can enhance it with real APIs:

#### Aviationstack API (Free Tier Available)
1. Visit [Aviationstack](https://aviationstack.com/)
2. Sign up for a free account
3. Get your API key
4. Add it to your `.env` file: `AVIATIONSTACK_API_KEY=your_key_here`

#### OpenAI API (Optional for Advanced Insights)
1. Visit [OpenAI](https://platform.openai.com/)
2. Create an account and get an API key
3. Add it to your `.env` file: `OPENAI_API_KEY=your_key_here`

## 🖥️ Usage

### Dashboard Overview
The main dashboard provides:
- **Statistics Cards**: Total flights, routes, airlines, and airports
- **Interactive Charts**: Visual representations of data trends
- **Filter Options**: Customize data by airport codes and limits
- **Data Table**: Detailed flight information

### Filtering Data
1. **From Airport**: Enter 3-letter IATA code (e.g., JFK, LAX)
2. **To Airport**: Enter destination IATA code
3. **Data Limit**: Choose number of flights to analyze (10-100)
4. Click "Load Data" to refresh the dashboard

### Understanding the Charts
- **Popular Routes**: Bar chart showing most frequented flight paths
- **Airline Distribution**: Pie chart of airline market share
- **Peak Times**: Line chart of flight frequency by hour
- **Airport Activity**: Bar chart of busiest airports

## 🏗️ Project Structure

```
airline-analytics-dashboard/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── templates/
│   └── index.html       # Main HTML template
├── static/
│   ├── css/            # Custom stylesheets
│   ├── js/             # JavaScript files
│   └── images/         # Static images
└── data/               # Data storage directory
```

## 🔧 Configuration

### Environment Variables
- `AVIATIONSTACK_API_KEY`: API key for Aviationstack service
- `OPENAI_API_KEY`: OpenAI API key for advanced insights
- `FLASK_ENV`: Flask environment (development/production)
- `SECRET_KEY`: Flask secret key for sessions

### Config Options
Modify `config.py` to adjust:
- API endpoints and timeouts
- Data processing parameters
- Cache settings
- Default values

## 🎯 API Endpoints

The application provides RESTful API endpoints:

- `GET /`: Main dashboard page
- `GET /api/data`: Fetch flight data with filters
- `GET /api/insights`: Get processed insights
- `GET /api/charts`: Retrieve chart data

### Example API Usage
```bash
# Get data for JFK to LAX flights
curl "http://localhost:5000/api/data?from=JFK&to=LAX&limit=25"

# Get insights
curl "http://localhost:5000/api/insights"
```

## 🧪 Testing

Run the application in development mode:
```bash
export FLASK_ENV=development
python app.py
```

The application includes:
- Mock data for testing without API keys
- Error handling for API failures
- Responsive design for mobile testing

## 📊 Data Sources

### Primary Sources
- **Aviationstack API**: Real-time flight data
- **Mock Data Generator**: Fallback data for testing
- **Web Scraping**: Additional public data sources

### Data Processing Pipeline
1. **Data Extraction**: Fetch from APIs or generate mock data
2. **Data Cleaning**: Remove duplicates, handle missing values
3. **Data Analysis**: Generate insights and statistics
4. **Data Visualization**: Create charts and graphs

## 🔍 Insights Generated

The application automatically generates:
- **Popular Routes**: Most frequently traveled paths
- **Airline Performance**: Market share and distribution
- **Peak Periods**: High-demand times and seasons
- **Airport Rankings**: Busiest hubs and terminals
- **Price Trends**: Cost variations over time (with API data)
- **Demand Patterns**: Seasonal and weekly trends

## 🚀 Deployment

### Local Development
```bash
python app.py
# Access at http://localhost:5000
```

### Production Deployment
```bash
# Using Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Using Docker (create Dockerfile)
docker build -t airline-analytics .
docker run -p 5000:5000 airline-analytics
```

### Cloud Deployment
The application is ready for deployment on:
- **Heroku**: Include `Procfile` with `web: gunicorn app:app`
- **AWS**: Use Elastic Beanstalk or EC2
- **Google Cloud**: Deploy to App Engine
- **Azure**: Use App Service

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🛡️ Security

- API keys are stored in environment variables
- Input validation on all user inputs
- CSRF protection enabled
- Secure headers implemented

## 🔧 Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Install missing dependencies
   ```bash
   pip install -r requirements.txt
   ```

2. **API Key Errors**: Check your `.env` file and API key validity

3. **Port Already in Use**: Change the port in `app.py`
   ```python
   app.run(debug=True, port=5001)
   ```

4. **Empty Charts**: Ensure data is loading properly - check browser console

### Getting Help
- Check the [Issues](https://github.com/your-repo/issues) section
- Review the application logs
- Test with mock data first

## 📈 Future Enhancements

- [ ] Real-time data updates
- [ ] Advanced machine learning insights
- [ ] Email notifications for price changes
- [ ] Mobile app version
- [ ] Multi-language support
- [ ] Export functionality (PDF, Excel)
- [ ] User authentication and profiles
- [ ] Historical data analysis

## 🏆 Acknowledgments

- [Aviationstack](https://aviationstack.com/) for flight data API
- [Bootstrap](https://getbootstrap.com/) for responsive design
- [Plotly](https://plotly.com/) for interactive charts
- [Flask](https://flask.palletsprojects.com/) for web framework

---

**Built with ❤️ for airline industry analytics** 
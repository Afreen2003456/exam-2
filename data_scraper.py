"""
Advanced Data Scraper Module for Airline Analytics Dashboard
Includes web scraping capabilities and multiple data sources
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time
import random
from datetime import datetime, timedelta
from config import Config
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AdvancedAirlineScraper:
    """Advanced scraper with multiple data sources and web scraping capabilities"""
    
    def __init__(self):
        self.config = Config()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
    def get_flight_data_with_scraping(self, source='aviationstack', **kwargs):
        """
        Get flight data from multiple sources including web scraping
        
        Args:
            source: Data source ('aviationstack', 'mock', 'scrape')
            **kwargs: Additional parameters for filtering
        """
        try:
            if source == 'aviationstack':
                return self._get_aviationstack_data(**kwargs)
            elif source == 'scrape':
                return self._scrape_public_data(**kwargs)
            else:
                return self._generate_enhanced_mock_data(**kwargs)
        except Exception as e:
            logger.error(f"Error fetching data from {source}: {str(e)}")
            return self._generate_enhanced_mock_data(**kwargs)
    
    def _get_aviationstack_data(self, route_from=None, route_to=None, limit=50):
        """Fetch data from Aviationstack API"""
        url = f"{self.config.AVIATIONSTACK_BASE_URL}/flights"
        params = {
            'access_key': self.config.AVIATIONSTACK_API_KEY,
            'limit': min(limit, self.config.MAX_FLIGHT_LIMIT)
        }
        
        if route_from:
            params['dep_iata'] = route_from.upper()
        if route_to:
            params['arr_iata'] = route_to.upper()
        
        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.warning(f"API request failed: {str(e)}")
            return self._generate_enhanced_mock_data(route_from, route_to, limit)
    
    def _scrape_public_data(self, **kwargs):
        """Scrape publicly available flight data (educational purposes)"""
        # This is a placeholder for educational purposes
        # In real implementation, you would scrape from public flight tracking sites
        # Always respect robots.txt and terms of service
        
        logger.info("Web scraping functionality - returning mock data for demo")
        return self._generate_enhanced_mock_data(**kwargs)
    
    def _generate_enhanced_mock_data(self, route_from=None, route_to=None, limit=50):
        """Generate enhanced mock data with realistic patterns"""
        flights = []
        
        # Define realistic flight patterns
        popular_routes = [
            ('JFK', 'LAX'), ('LAX', 'JFK'),
            ('ORD', 'DFW'), ('DFW', 'ORD'),
            ('ATL', 'MIA'), ('MIA', 'ATL'),
            ('SFO', 'SEA'), ('SEA', 'SFO'),
            ('LAS', 'DEN'), ('DEN', 'LAS'),
            ('BOS', 'WAS'), ('WAS', 'BOS')
        ]
        
        airlines = [
            {'name': 'American Airlines', 'iata': 'AA', 'icao': 'AAL'},
            {'name': 'United Airlines', 'iata': 'UA', 'icao': 'UAL'},
            {'name': 'Delta Air Lines', 'iata': 'DL', 'icao': 'DAL'},
            {'name': 'Southwest Airlines', 'iata': 'WN', 'icao': 'SWA'},
            {'name': 'JetBlue Airways', 'iata': 'B6', 'icao': 'JBU'},
            {'name': 'Alaska Airlines', 'iata': 'AS', 'icao': 'ASA'},
            {'name': 'Spirit Airlines', 'iata': 'NK', 'icao': 'NKS'},
            {'name': 'Frontier Airlines', 'iata': 'F9', 'icao': 'FFT'}
        ]
        
        flight_statuses = ['scheduled', 'active', 'landed', 'cancelled', 'incident', 'diverted']
        
        # Generate flights
        for i in range(min(limit, 100)):
            # Select route
            if route_from and route_to:
                dep_iata, arr_iata = route_from.upper(), route_to.upper()
            elif route_from:
                dep_iata = route_from.upper()
                arr_iata = random.choice([code for code in self.config.POPULAR_AIRPORTS.keys() if code != dep_iata])
            elif route_to:
                arr_iata = route_to.upper()
                dep_iata = random.choice([code for code in self.config.POPULAR_AIRPORTS.keys() if code != arr_iata])
            else:
                dep_iata, arr_iata = random.choice(popular_routes)
            
            # Select airline
            airline = random.choice(airlines)
            
            # Generate flight number
            flight_number = f"{random.randint(1000, 9999)}"
            
            # Generate times (realistic scheduling)
            base_date = datetime.now() + timedelta(days=random.randint(0, 7))
            dep_hour = random.choices([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 
                                     weights=[5, 8, 12, 15, 12, 10, 8, 6, 8, 10, 12, 15, 12, 10, 8, 6])[0]
            dep_time = base_date.replace(hour=dep_hour, minute=random.randint(0, 59))
            
            # Calculate arrival time (realistic flight duration)
            flight_duration = random.randint(60, 360)  # 1-6 hours
            arr_time = dep_time + timedelta(minutes=flight_duration)
            
            # Generate terminals and gates
            dep_terminal = random.choice(['1', '2', '3', '4', '5', 'A', 'B', 'C', 'D', 'E'])
            arr_terminal = random.choice(['1', '2', '3', '4', '5', 'A', 'B', 'C', 'D', 'E'])
            dep_gate = f"{random.choice(['A', 'B', 'C', 'D', 'E'])}{random.randint(1, 30)}"
            arr_gate = f"{random.choice(['A', 'B', 'C', 'D', 'E'])}{random.randint(1, 30)}"
            
            flight = {
                "flight_date": dep_time.strftime("%Y-%m-%d"),
                "flight_status": random.choices(flight_statuses, weights=[70, 15, 10, 3, 1, 1])[0],
                "departure": {
                    "airport": self.config.POPULAR_AIRPORTS.get(dep_iata, f"{dep_iata} Airport"),
                    "timezone": "America/New_York",
                    "iata": dep_iata,
                    "icao": f"K{dep_iata}",
                    "terminal": dep_terminal,
                    "gate": dep_gate,
                    "scheduled": dep_time.isoformat() + "+00:00",
                    "estimated": (dep_time + timedelta(minutes=random.randint(-15, 30))).isoformat() + "+00:00"
                },
                "arrival": {
                    "airport": self.config.POPULAR_AIRPORTS.get(arr_iata, f"{arr_iata} Airport"),
                    "timezone": "America/Los_Angeles",
                    "iata": arr_iata,
                    "icao": f"K{arr_iata}",
                    "terminal": arr_terminal,
                    "gate": arr_gate,
                    "scheduled": arr_time.isoformat() + "+00:00",
                    "estimated": (arr_time + timedelta(minutes=random.randint(-15, 30))).isoformat() + "+00:00"
                },
                "airline": airline,
                "flight": {
                    "number": flight_number,
                    "iata": f"{airline['iata']}{flight_number}",
                    "icao": f"{airline['icao']}{flight_number}"
                },
                "aircraft": {
                    "registration": f"N{random.randint(100, 999)}{random.choice(['AA', 'UA', 'DL', 'WN'])}",
                    "iata": random.choice(['B738', 'A320', 'B777', 'A330', 'E190']),
                    "icao": random.choice(['B738', 'A320', 'B777', 'A330', 'E190'])
                },
                "live": {
                    "updated": datetime.now().isoformat() + "+00:00",
                    "latitude": round(random.uniform(25.0, 50.0), 6),
                    "longitude": round(random.uniform(-125.0, -65.0), 6),
                    "altitude": random.randint(30000, 42000),
                    "direction": random.randint(0, 360),
                    "speed_horizontal": random.randint(400, 600),
                    "speed_vertical": random.randint(-50, 50),
                    "is_ground": random.choice([True, False])
                }
            }
            
            flights.append(flight)
        
        return {
            "pagination": {
                "limit": limit,
                "offset": 0,
                "count": len(flights),
                "total": len(flights)
            },
            "data": flights
        }
    
    def get_market_insights(self, data):
        """Generate advanced market insights from flight data"""
        if not data or 'data' not in data:
            return {}
        
        flights = data['data']
        df = pd.DataFrame(flights)
        
        insights = {
            'market_analysis': self._analyze_market_trends(flights),
            'route_performance': self._analyze_route_performance(flights),
            'airline_metrics': self._analyze_airline_metrics(flights),
            'operational_insights': self._analyze_operational_data(flights),
            'temporal_patterns': self._analyze_temporal_patterns(flights),
            'recommendations': self._generate_recommendations(flights)
        }
        
        return insights
    
    def _analyze_market_trends(self, flights):
        """Analyze market trends and demand patterns"""
        try:
            # Route popularity
            routes = [f"{f['departure']['iata']}-{f['arrival']['iata']}" for f in flights 
                     if f.get('departure') and f.get('arrival')]
            route_counts = pd.Series(routes).value_counts()
            
            # Airline market share
            airlines = [f['airline']['name'] for f in flights if f.get('airline')]
            airline_counts = pd.Series(airlines).value_counts()
            
            return {
                'top_routes': route_counts.head(10).to_dict(),
                'market_leaders': airline_counts.head(5).to_dict(),
                'market_concentration': len(airline_counts),
                'route_diversity': len(route_counts)
            }
        except Exception as e:
            logger.error(f"Error analyzing market trends: {str(e)}")
            return {}
    
    def _analyze_route_performance(self, flights):
        """Analyze individual route performance"""
        try:
            route_data = {}
            for flight in flights:
                if not (flight.get('departure') and flight.get('arrival')):
                    continue
                    
                route = f"{flight['departure']['iata']}-{flight['arrival']['iata']}"
                if route not in route_data:
                    route_data[route] = {
                        'flights': 0,
                        'airlines': set(),
                        'on_time_rate': 0,
                        'avg_delay': 0
                    }
                
                route_data[route]['flights'] += 1
                route_data[route]['airlines'].add(flight['airline']['name'])
                
                # Calculate on-time performance (mock calculation)
                if flight['flight_status'] in ['scheduled', 'active', 'landed']:
                    route_data[route]['on_time_rate'] += 1
            
            # Process route data
            for route in route_data:
                route_data[route]['airlines'] = len(route_data[route]['airlines'])
                route_data[route]['on_time_rate'] = round(
                    route_data[route]['on_time_rate'] / route_data[route]['flights'] * 100, 2
                )
            
            return dict(sorted(route_data.items(), 
                              key=lambda x: x[1]['flights'], reverse=True)[:10])
        except Exception as e:
            logger.error(f"Error analyzing route performance: {str(e)}")
            return {}
    
    def _analyze_airline_metrics(self, flights):
        """Analyze airline-specific metrics"""
        try:
            airline_metrics = {}
            for flight in flights:
                if not flight.get('airline'):
                    continue
                    
                airline = flight['airline']['name']
                if airline not in airline_metrics:
                    airline_metrics[airline] = {
                        'total_flights': 0,
                        'routes_served': set(),
                        'aircraft_types': set(),
                        'on_time_performance': 0
                    }
                
                airline_metrics[airline]['total_flights'] += 1
                
                if flight.get('departure') and flight.get('arrival'):
                    route = f"{flight['departure']['iata']}-{flight['arrival']['iata']}"
                    airline_metrics[airline]['routes_served'].add(route)
                
                if flight.get('aircraft'):
                    airline_metrics[airline]['aircraft_types'].add(flight['aircraft']['iata'])
                
                # Mock on-time performance
                if flight['flight_status'] in ['scheduled', 'active', 'landed']:
                    airline_metrics[airline]['on_time_performance'] += 1
            
            # Process metrics
            for airline in airline_metrics:
                metrics = airline_metrics[airline]
                metrics['routes_served'] = len(metrics['routes_served'])
                metrics['aircraft_types'] = len(metrics['aircraft_types'])
                metrics['on_time_performance'] = round(
                    metrics['on_time_performance'] / metrics['total_flights'] * 100, 2
                )
            
            return dict(sorted(airline_metrics.items(), 
                              key=lambda x: x[1]['total_flights'], reverse=True)[:5])
        except Exception as e:
            logger.error(f"Error analyzing airline metrics: {str(e)}")
            return {}
    
    def _analyze_operational_data(self, flights):
        """Analyze operational insights"""
        try:
            # Airport utilization
            airports = []
            for flight in flights:
                if flight.get('departure'):
                    airports.append(flight['departure']['iata'])
                if flight.get('arrival'):
                    airports.append(flight['arrival']['iata'])
            
            airport_counts = pd.Series(airports).value_counts()
            
            # Flight status distribution
            statuses = [f['flight_status'] for f in flights if f.get('flight_status')]
            status_counts = pd.Series(statuses).value_counts()
            
            return {
                'busiest_airports': airport_counts.head(10).to_dict(),
                'flight_status_distribution': status_counts.to_dict(),
                'operational_efficiency': round(
                    (status_counts.get('scheduled', 0) + status_counts.get('active', 0) + 
                     status_counts.get('landed', 0)) / len(statuses) * 100, 2
                ) if statuses else 0
            }
        except Exception as e:
            logger.error(f"Error analyzing operational data: {str(e)}")
            return {}
    
    def _analyze_temporal_patterns(self, flights):
        """Analyze temporal patterns in flight data"""
        try:
            # Extract hours from departure times
            departure_hours = []
            for flight in flights:
                if flight.get('departure') and flight['departure'].get('scheduled'):
                    try:
                        dt = datetime.fromisoformat(flight['departure']['scheduled'].replace('Z', '+00:00'))
                        departure_hours.append(dt.hour)
                    except:
                        continue
            
            if not departure_hours:
                return {}
            
            hour_counts = pd.Series(departure_hours).value_counts().sort_index()
            
            # Identify peak hours
            peak_hours = hour_counts.nlargest(3).index.tolist()
            
            return {
                'hourly_distribution': hour_counts.to_dict(),
                'peak_hours': peak_hours,
                'busiest_hour': hour_counts.idxmax() if not hour_counts.empty else None,
                'quietest_hour': hour_counts.idxmin() if not hour_counts.empty else None
            }
        except Exception as e:
            logger.error(f"Error analyzing temporal patterns: {str(e)}")
            return {}
    
    def _generate_recommendations(self, flights):
        """Generate actionable recommendations based on data analysis"""
        try:
            recommendations = []
            
            # Route recommendations
            routes = [f"{f['departure']['iata']}-{f['arrival']['iata']}" for f in flights 
                     if f.get('departure') and f.get('arrival')]
            route_counts = pd.Series(routes).value_counts()
            
            if not route_counts.empty:
                top_route = route_counts.index[0]
                recommendations.append({
                    'type': 'route_opportunity',
                    'title': f'High Demand Route: {top_route}',
                    'description': f'This route shows {route_counts.iloc[0]} flights, indicating high demand.',
                    'action': 'Consider increasing frequency or capacity on this route.'
                })
            
            # Airline recommendations
            airlines = [f['airline']['name'] for f in flights if f.get('airline')]
            airline_counts = pd.Series(airlines).value_counts()
            
            if not airline_counts.empty:
                recommendations.append({
                    'type': 'market_insight',
                    'title': f'Market Leader: {airline_counts.index[0]}',
                    'description': f'Dominates with {airline_counts.iloc[0]} flights in the dataset.',
                    'action': 'Monitor competitive strategies and market positioning.'
                })
            
            # Operational recommendations
            statuses = [f['flight_status'] for f in flights if f.get('flight_status')]
            cancelled_rate = len([s for s in statuses if s == 'cancelled']) / len(statuses) * 100 if statuses else 0
            
            if cancelled_rate > 5:
                recommendations.append({
                    'type': 'operational_alert',
                    'title': 'High Cancellation Rate',
                    'description': f'Cancellation rate at {cancelled_rate:.1f}% - above industry average.',
                    'action': 'Review operational procedures and weather contingencies.'
                })
            
            return recommendations
        except Exception as e:
            logger.error(f"Error generating recommendations: {str(e)}")
            return []

# Usage example
if __name__ == "__main__":
    scraper = AdvancedAirlineScraper()
    
    # Test data fetching
    print("Testing data fetching...")
    data = scraper.get_flight_data_with_scraping(source='mock', limit=10)
    print(f"Fetched {len(data.get('data', []))} flights")
    
    # Test insights generation
    print("\nTesting insights generation...")
    insights = scraper.get_market_insights(data)
    print(f"Generated {len(insights)} insight categories")
    
    # Print sample insights
    if insights.get('recommendations'):
        print("\nSample recommendations:")
        for rec in insights['recommendations'][:2]:
            print(f"- {rec['title']}: {rec['description']}") 
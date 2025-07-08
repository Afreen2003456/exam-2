"""
Configuration file for Airline Data Analytics Dashboard
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Base configuration class"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    AVIATIONSTACK_API_KEY = os.environ.get('AVIATIONSTACK_API_KEY') or 'demo_key'
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY') or ''
    
    # API Configuration
    AVIATIONSTACK_BASE_URL = 'http://api.aviationstack.com/v1'
    
    # Data Configuration
    DEFAULT_FLIGHT_LIMIT = 50
    MAX_FLIGHT_LIMIT = 100
    
    # Cache Configuration
    CACHE_TIMEOUT = 300  # 5 minutes
    
    # Popular airports for demo purposes
    POPULAR_AIRPORTS = {
        'JFK': 'John F Kennedy International Airport',
        'LAX': 'Los Angeles International Airport', 
        'ORD': 'Chicago O\'Hare International Airport',
        'ATL': 'Hartsfield-Jackson Atlanta International Airport',
        'DFW': 'Dallas/Fort Worth International Airport',
        'DEN': 'Denver International Airport',
        'SFO': 'San Francisco International Airport',
        'LAS': 'McCarran International Airport',
        'SEA': 'Seattle-Tacoma International Airport',
        'MIA': 'Miami International Airport'
    }
    
    # Popular airlines for demo purposes
    POPULAR_AIRLINES = {
        'AA': 'American Airlines',
        'UA': 'United Airlines',
        'DL': 'Delta Air Lines',
        'WN': 'Southwest Airlines',
        'B6': 'JetBlue Airways',
        'AS': 'Alaska Airlines',
        'NK': 'Spirit Airlines',
        'F9': 'Frontier Airlines'
    }

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True

# Configuration mapping
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
} 
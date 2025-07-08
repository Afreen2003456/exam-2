from flask import Flask, render_template, request, jsonify
import requests
import pandas as pd
import json
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import plotly.graph_objs as go
import plotly.utils

# Load environment variables
load_dotenv()

app = Flask(__name__)

class AirlineDataScraper:
    def __init__(self):
        self.aviationstack_key = os.getenv('AVIATIONSTACK_API_KEY', 'free_key')
        self.openai_key = os.getenv('OPENAI_API_KEY', '')
        
    def get_flight_data(self, route_from=None, route_to=None, limit=50):
        """Get flight data from Aviationstack API (free tier)"""
        try:
            # Using free tier of Aviationstack API
            url = "http://api.aviationstack.com/v1/flights"
            params = {
                'access_key': self.aviationstack_key,
                'limit': limit
            }
            
            if route_from:
                params['dep_iata'] = route_from
            if route_to:
                params['arr_iata'] = route_to
                
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                return self.get_mock_data()
        except:
            return self.get_mock_data()
    
    def get_mock_data(self):
        """Generate enhanced mock airline data with more comprehensive dataset"""
        import random
        from datetime import datetime, timedelta
        
        # Define comprehensive worldwide data for realistic simulation
        airports = {
            # North America
            'JFK': 'John F Kennedy International Airport',
            'LAX': 'Los Angeles International Airport',
            'ORD': 'Chicago O\'Hare International Airport',
            'ATL': 'Hartsfield-Jackson Atlanta International Airport',
            'DFW': 'Dallas/Fort Worth International Airport',
            'DEN': 'Denver International Airport',
            'SFO': 'San Francisco International Airport',
            'LAS': 'McCarran International Airport',
            'SEA': 'Seattle-Tacoma International Airport',
            'MIA': 'Miami International Airport',
            'YYZ': 'Toronto Pearson International Airport',
            'YVR': 'Vancouver International Airport',
            'MEX': 'Mexico City International Airport',
            
            # Europe
            'LHR': 'London Heathrow Airport',
            'CDG': 'Charles de Gaulle Airport',
            'FRA': 'Frankfurt Airport',
            'AMS': 'Amsterdam Airport Schiphol',
            'MAD': 'Madrid-Barajas Airport',
            'FCO': 'Leonardo da Vinci International Airport',
            'MUC': 'Munich Airport',
            'ZUR': 'Zurich Airport',
            'VIE': 'Vienna International Airport',
            'ARN': 'Stockholm Arlanda Airport',
            'CPH': 'Copenhagen Airport',
            'HEL': 'Helsinki Airport',
            'IST': 'Istanbul Airport',
            'SVO': 'Sheremetyevo International Airport',
            
            # Asia-Pacific
            'NRT': 'Narita International Airport',
            'HND': 'Haneda Airport',
            'ICN': 'Incheon International Airport',
            'PEK': 'Beijing Capital International Airport',
            'PVG': 'Shanghai Pudong International Airport',
            'HKG': 'Hong Kong International Airport',
            'SIN': 'Singapore Changi Airport',
            'BKK': 'Suvarnabhumi Airport',
            'KUL': 'Kuala Lumpur International Airport',
            'CGK': 'Soekarno-Hatta International Airport',
            'SYD': 'Sydney Kingsford Smith Airport',
            'MEL': 'Melbourne Airport',
            'BNE': 'Brisbane Airport',
            'AKL': 'Auckland Airport',
            'DEL': 'Indira Gandhi International Airport',
            'BOM': 'Chhatrapati Shivaji International Airport',
            'BLR': 'Kempegowda International Airport',
            'MAA': 'Chennai International Airport',
            'HYD': 'Rajiv Gandhi International Airport',
            
            # Middle East & Africa
            'DXB': 'Dubai International Airport',
            'DOH': 'Hamad International Airport',
            'AUH': 'Abu Dhabi International Airport',
            'KWI': 'Kuwait International Airport',
            'CAI': 'Cairo International Airport',
            'JNB': 'O.R. Tambo International Airport',
            'CPT': 'Cape Town International Airport',
            'NBO': 'Jomo Kenyatta International Airport',
            'ADD': 'Addis Ababa Bole International Airport',
            
            # South America
            'GRU': 'São Paulo-Guarulhos International Airport',
            'GIG': 'Rio de Janeiro-Galeão International Airport',
            'EZE': 'Ezeiza International Airport',
            'SCL': 'Santiago International Airport',
            'LIM': 'Jorge Chávez International Airport',
            'BOG': 'El Dorado International Airport'
        }
        
        airlines = [
            # North American Airlines
            {'name': 'American Airlines', 'iata': 'AA', 'icao': 'AAL'},
            {'name': 'United Airlines', 'iata': 'UA', 'icao': 'UAL'},
            {'name': 'Delta Air Lines', 'iata': 'DL', 'icao': 'DAL'},
            {'name': 'Southwest Airlines', 'iata': 'WN', 'icao': 'SWA'},
            {'name': 'JetBlue Airways', 'iata': 'B6', 'icao': 'JBU'},
            {'name': 'Air Canada', 'iata': 'AC', 'icao': 'ACA'},
            {'name': 'Alaska Airlines', 'iata': 'AS', 'icao': 'ASA'},
            
            # European Airlines
            {'name': 'British Airways', 'iata': 'BA', 'icao': 'BAW'},
            {'name': 'Lufthansa', 'iata': 'LH', 'icao': 'DLH'},
            {'name': 'Air France', 'iata': 'AF', 'icao': 'AFR'},
            {'name': 'KLM', 'iata': 'KL', 'icao': 'KLM'},
            {'name': 'Turkish Airlines', 'iata': 'TK', 'icao': 'THY'},
            {'name': 'Swiss International Air Lines', 'iata': 'LX', 'icao': 'SWR'},
            {'name': 'Austrian Airlines', 'iata': 'OS', 'icao': 'AUA'},
            {'name': 'Finnair', 'iata': 'AY', 'icao': 'FIN'},
            {'name': 'SAS', 'iata': 'SK', 'icao': 'SAS'},
            {'name': 'Ryanair', 'iata': 'FR', 'icao': 'RYR'},
            {'name': 'easyJet', 'iata': 'U2', 'icao': 'EZY'},
            
            # Asian Airlines
            {'name': 'Singapore Airlines', 'iata': 'SQ', 'icao': 'SIA'},
            {'name': 'Cathay Pacific', 'iata': 'CX', 'icao': 'CPA'},
            {'name': 'Japan Airlines', 'iata': 'JL', 'icao': 'JAL'},
            {'name': 'All Nippon Airways', 'iata': 'NH', 'icao': 'ANA'},
            {'name': 'Korean Air', 'iata': 'KE', 'icao': 'KAL'},
            {'name': 'China Southern Airlines', 'iata': 'CZ', 'icao': 'CSN'},
            {'name': 'China Eastern Airlines', 'iata': 'MU', 'icao': 'CES'},
            {'name': 'Air China', 'iata': 'CA', 'icao': 'CCA'},
            {'name': 'Thai Airways', 'iata': 'TG', 'icao': 'THA'},
            {'name': 'Malaysia Airlines', 'iata': 'MH', 'icao': 'MAS'},
            {'name': 'Qantas', 'iata': 'QF', 'icao': 'QFA'},
            {'name': 'Jetstar', 'iata': 'JQ', 'icao': 'JST'},
            {'name': 'IndiGo', 'iata': '6E', 'icao': 'IGO'},
            {'name': 'Air India', 'iata': 'AI', 'icao': 'AIC'},
            {'name': 'SpiceJet', 'iata': 'SG', 'icao': 'SEJ'},
            
            # Middle Eastern Airlines
            {'name': 'Emirates', 'iata': 'EK', 'icao': 'UAE'},
            {'name': 'Qatar Airways', 'iata': 'QR', 'icao': 'QTR'},
            {'name': 'Etihad Airways', 'iata': 'EY', 'icao': 'ETD'},
            {'name': 'Kuwait Airways', 'iata': 'KU', 'icao': 'KAC'},
            
            # African Airlines
            {'name': 'South African Airways', 'iata': 'SA', 'icao': 'SAA'},
            {'name': 'Ethiopian Airlines', 'iata': 'ET', 'icao': 'ETH'},
            {'name': 'Kenya Airways', 'iata': 'KQ', 'icao': 'KQA'},
            {'name': 'EgyptAir', 'iata': 'MS', 'icao': 'MSR'},
            
            # South American Airlines
            {'name': 'LATAM Airlines', 'iata': 'LA', 'icao': 'LAN'},
            {'name': 'Avianca', 'iata': 'AV', 'icao': 'AVA'},
            {'name': 'Azul Brazilian Airlines', 'iata': 'AD', 'icao': 'AZU'},
            {'name': 'Copa Airlines', 'iata': 'CM', 'icao': 'CMP'}
        ]
        
        # Popular worldwide routes with realistic frequency weights
        popular_routes = [
            # North America Domestic
            ('JFK', 'LAX', 15), ('LAX', 'JFK', 15),
            ('ORD', 'DFW', 12), ('DFW', 'ORD', 12),
            ('ATL', 'MIA', 10), ('MIA', 'ATL', 10),
            ('SFO', 'SEA', 8), ('SEA', 'SFO', 8),
            ('JFK', 'SFO', 9), ('SFO', 'JFK', 9),
            ('ORD', 'LAX', 11), ('LAX', 'ORD', 11),
            ('ATL', 'JFK', 13), ('JFK', 'ATL', 13),
            ('DFW', 'LAX', 8), ('LAX', 'DFW', 8),
            ('MIA', 'JFK', 7), ('JFK', 'MIA', 7),
            
            # Trans-Atlantic Routes
            ('JFK', 'LHR', 12), ('LHR', 'JFK', 12),
            ('LAX', 'LHR', 8), ('LHR', 'LAX', 8),
            ('ORD', 'CDG', 7), ('CDG', 'ORD', 7),
            ('JFK', 'CDG', 10), ('CDG', 'JFK', 10),
            ('ATL', 'LHR', 6), ('LHR', 'ATL', 6),
            ('JFK', 'FRA', 8), ('FRA', 'JFK', 8),
            ('DFW', 'LHR', 5), ('LHR', 'DFW', 5),
            ('MIA', 'MAD', 4), ('MAD', 'MIA', 4),
            ('JFK', 'AMS', 6), ('AMS', 'JFK', 6),
            
            # Trans-Pacific Routes
            ('LAX', 'NRT', 10), ('NRT', 'LAX', 10),
            ('SFO', 'HKG', 8), ('HKG', 'SFO', 8),
            ('SEA', 'ICN', 7), ('ICN', 'SEA', 7),
            ('LAX', 'SYD', 6), ('SYD', 'LAX', 6),
            ('SFO', 'SIN', 5), ('SIN', 'SFO', 5),
            ('LAX', 'PEK', 7), ('PEK', 'LAX', 7),
            ('ORD', 'NRT', 5), ('NRT', 'ORD', 5),
            ('DFW', 'ICN', 4), ('ICN', 'DFW', 4),
            
            # European Routes
            ('LHR', 'CDG', 15), ('CDG', 'LHR', 15),
            ('LHR', 'FRA', 12), ('FRA', 'LHR', 12),
            ('CDG', 'AMS', 10), ('AMS', 'CDG', 10),
            ('LHR', 'AMS', 11), ('AMS', 'LHR', 11),
            ('FRA', 'MUC', 8), ('MUC', 'FRA', 8),
            ('LHR', 'MAD', 7), ('MAD', 'LHR', 7),
            ('CDG', 'FCO', 6), ('FCO', 'CDG', 6),
            ('AMS', 'ZUR', 5), ('ZUR', 'AMS', 5),
            ('LHR', 'IST', 6), ('IST', 'LHR', 6),
            
            # Asian Routes
            ('HKG', 'SIN', 12), ('SIN', 'HKG', 12),
            ('NRT', 'ICN', 10), ('ICN', 'NRT', 10),
            ('BKK', 'SIN', 8), ('SIN', 'BKK', 8),
            ('HKG', 'BKK', 7), ('BKK', 'HKG', 7),
            ('PEK', 'PVG', 9), ('PVG', 'PEK', 9),
            ('DEL', 'BOM', 8), ('BOM', 'DEL', 8),
            ('SIN', 'KUL', 6), ('KUL', 'SIN', 6),
            ('HKG', 'SYD', 5), ('SYD', 'HKG', 5),
            ('NRT', 'SIN', 4), ('SIN', 'NRT', 4),
            
            # Middle East Hub Routes
            ('DXB', 'LHR', 10), ('LHR', 'DXB', 10),
            ('DOH', 'LHR', 8), ('LHR', 'DOH', 8),
            ('DXB', 'JFK', 7), ('JFK', 'DXB', 7),
            ('DXB', 'BOM', 6), ('BOM', 'DXB', 6),
            ('DOH', 'SIN', 5), ('SIN', 'DOH', 5),
            ('DXB', 'SIN', 6), ('SIN', 'DXB', 6),
            ('AUH', 'LHR', 4), ('LHR', 'AUH', 4),
            
            # Africa Routes
            ('JNB', 'CPT', 8), ('CPT', 'JNB', 8),
            ('CAI', 'LHR', 5), ('LHR', 'CAI', 5),
            ('ADD', 'DXB', 4), ('DXB', 'ADD', 4),
            ('JNB', 'LHR', 6), ('LHR', 'JNB', 6),
            ('NBO', 'DXB', 3), ('DXB', 'NBO', 3),
            
            # South America Routes
            ('GRU', 'GIG', 6), ('GIG', 'GRU', 6),
            ('GRU', 'EZE', 5), ('EZE', 'GRU', 5),
            ('SCL', 'LIM', 4), ('LIM', 'SCL', 4),
            ('BOG', 'MIA', 5), ('MIA', 'BOG', 5),
            ('GRU', 'LHR', 4), ('LHR', 'GRU', 4),
            ('GIG', 'CDG', 3), ('CDG', 'GIG', 3)
        ]
        
        flight_statuses = [
            ('scheduled', 60), ('active', 20), ('landed', 15), 
            ('delayed', 3), ('cancelled', 1), ('diverted', 1)
        ]
        
        aircraft_types = [
            'B737', 'A320', 'B777', 'A330', 'E190', 'B757', 'A319', 
            'B767', 'A321', 'E175', 'B787', 'A350', 'B747', 'A380'
        ]
        
        flights = []
        base_date = datetime.now()
        
        # Generate 300 flights for comprehensive worldwide data
        for i in range(300):
            # Select route based on popularity
            route_data = random.choices(popular_routes, weights=[r[2] for r in popular_routes])[0]
            dep_iata, arr_iata = route_data[0], route_data[1]
            
            # Select airline with realistic global distribution
            airline = random.choices(airlines, weights=[
                12, 10, 8, 6, 4, 3, 2,  # North American airlines (7)
                8, 6, 5, 4, 3, 2, 2, 2, 2, 2, 2,  # European airlines (11)
                7, 6, 5, 4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2,  # Asian airlines (15)
                5, 4, 3, 2,  # Middle Eastern airlines (4)
                2, 2, 2, 2,  # African airlines (4)
                3, 2, 2, 2   # South American airlines (4)
            ])[0]
            
            # Generate realistic flight times
            flight_day = random.randint(0, 6)  # Next week
            flight_hour = random.choices(
                range(5, 23), 
                weights=[2, 4, 8, 12, 15, 18, 20, 18, 15, 12, 10, 8, 6, 4, 3, 2, 1, 1]
            )[0]
            
            dep_time = (base_date + timedelta(days=flight_day)).replace(
                hour=flight_hour, 
                minute=random.randint(0, 59),
                second=0, 
                microsecond=0
            )
            
            # Calculate realistic flight duration based on distance (in minutes)
            flight_duration_map = {
                # North America Domestic
                ('JFK', 'LAX'): 360, ('LAX', 'JFK'): 330,
                ('ORD', 'DFW'): 150, ('DFW', 'ORD'): 140,
                ('ATL', 'MIA'): 120, ('MIA', 'ATL'): 110,
                ('SFO', 'SEA'): 120, ('SEA', 'SFO'): 110,
                ('JFK', 'SFO'): 370, ('SFO', 'JFK'): 320,
                ('ORD', 'LAX'): 270, ('LAX', 'ORD'): 240,
                ('ATL', 'JFK'): 140, ('JFK', 'ATL'): 130,
                ('DFW', 'LAX'): 180, ('LAX', 'DFW'): 170,
                ('MIA', 'JFK'): 165, ('JFK', 'MIA'): 160,
                
                # Trans-Atlantic Routes
                ('JFK', 'LHR'): 430, ('LHR', 'JFK'): 480,
                ('LAX', 'LHR'): 660, ('LHR', 'LAX'): 720,
                ('ORD', 'CDG'): 480, ('CDG', 'ORD'): 540,
                ('JFK', 'CDG'): 440, ('CDG', 'JFK'): 490,
                ('ATL', 'LHR'): 480, ('LHR', 'ATL'): 540,
                ('JFK', 'FRA'): 460, ('FRA', 'JFK'): 510,
                ('DFW', 'LHR'): 560, ('LHR', 'DFW'): 620,
                ('MIA', 'MAD'): 500, ('MAD', 'MIA'): 560,
                ('JFK', 'AMS'): 440, ('AMS', 'JFK'): 490,
                
                # Trans-Pacific Routes
                ('LAX', 'NRT'): 660, ('NRT', 'LAX'): 630,
                ('SFO', 'HKG'): 900, ('HKG', 'SFO'): 840,
                ('SEA', 'ICN'): 660, ('ICN', 'SEA'): 630,
                ('LAX', 'SYD'): 900, ('SYD', 'LAX'): 840,
                ('SFO', 'SIN'): 1020, ('SIN', 'SFO'): 960,
                ('LAX', 'PEK'): 780, ('PEK', 'LAX'): 720,
                ('ORD', 'NRT'): 780, ('NRT', 'ORD'): 720,
                ('DFW', 'ICN'): 840, ('ICN', 'DFW'): 780,
                
                # European Routes
                ('LHR', 'CDG'): 80, ('CDG', 'LHR'): 80,
                ('LHR', 'FRA'): 90, ('FRA', 'LHR'): 90,
                ('CDG', 'AMS'): 75, ('AMS', 'CDG'): 75,
                ('LHR', 'AMS'): 65, ('AMS', 'LHR'): 65,
                ('FRA', 'MUC'): 60, ('MUC', 'FRA'): 60,
                ('LHR', 'MAD'): 140, ('MAD', 'LHR'): 140,
                ('CDG', 'FCO'): 130, ('FCO', 'CDG'): 130,
                ('AMS', 'ZUR'): 90, ('ZUR', 'AMS'): 90,
                ('LHR', 'IST'): 240, ('IST', 'LHR'): 240,
                
                # Asian Routes
                ('HKG', 'SIN'): 200, ('SIN', 'HKG'): 200,
                ('NRT', 'ICN'): 140, ('ICN', 'NRT'): 140,
                ('BKK', 'SIN'): 140, ('SIN', 'BKK'): 140,
                ('HKG', 'BKK'): 160, ('BKK', 'HKG'): 160,
                ('PEK', 'PVG'): 120, ('PVG', 'PEK'): 120,
                ('DEL', 'BOM'): 120, ('BOM', 'DEL'): 120,
                ('SIN', 'KUL'): 90, ('KUL', 'SIN'): 90,
                ('HKG', 'SYD'): 540, ('SYD', 'HKG'): 540,
                ('NRT', 'SIN'): 420, ('SIN', 'NRT'): 420,
                
                # Middle East Hub Routes
                ('DXB', 'LHR'): 420, ('LHR', 'DXB'): 420,
                ('DOH', 'LHR'): 400, ('LHR', 'DOH'): 400,
                ('DXB', 'JFK'): 840, ('JFK', 'DXB'): 840,
                ('DXB', 'BOM'): 180, ('BOM', 'DXB'): 180,
                ('DOH', 'SIN'): 420, ('SIN', 'DOH'): 420,
                ('DXB', 'SIN'): 420, ('SIN', 'DXB'): 420,
                ('AUH', 'LHR'): 420, ('LHR', 'AUH'): 420,
                
                # Africa Routes
                ('JNB', 'CPT'): 120, ('CPT', 'JNB'): 120,
                ('CAI', 'LHR'): 300, ('LHR', 'CAI'): 300,
                ('ADD', 'DXB'): 240, ('DXB', 'ADD'): 240,
                ('JNB', 'LHR'): 660, ('LHR', 'JNB'): 660,
                ('NBO', 'DXB'): 300, ('DXB', 'NBO'): 300,
                
                # South America Routes
                ('GRU', 'GIG'): 60, ('GIG', 'GRU'): 60,
                ('GRU', 'EZE'): 140, ('EZE', 'GRU'): 140,
                ('SCL', 'LIM'): 120, ('LIM', 'SCL'): 120,
                ('BOG', 'MIA'): 180, ('MIA', 'BOG'): 180,
                ('GRU', 'LHR'): 660, ('LHR', 'GRU'): 660,
                ('GIG', 'CDG'): 660, ('CDG', 'GIG'): 660,
            }
            
            base_duration = flight_duration_map.get((dep_iata, arr_iata), 180)
            duration_variance = random.randint(-30, 30)
            flight_duration = base_duration + duration_variance
            
            arr_time = dep_time + timedelta(minutes=flight_duration)
            
            # Select flight status with realistic distribution
            status_data = random.choices(flight_statuses, weights=[s[1] for s in flight_statuses])[0]
            flight_status = status_data[0]
            
            # Generate realistic delay if delayed
            actual_dep_time = dep_time
            actual_arr_time = arr_time
            if flight_status == 'delayed':
                delay_minutes = random.randint(15, 120)
                actual_dep_time = dep_time + timedelta(minutes=delay_minutes)
                actual_arr_time = arr_time + timedelta(minutes=delay_minutes)
            
            # Generate terminals and gates
            terminals = ['1', '2', '3', '4', '5', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
            gates = [f"{random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'])}{random.randint(1, 50)}" for _ in range(2)]
            
            flight_number = f"{random.randint(1000, 9999)}"
            
            # Assign realistic timezones based on airport location
            timezone_map = {
                # North America
                'JFK': 'America/New_York', 'LAX': 'America/Los_Angeles', 'ORD': 'America/Chicago',
                'ATL': 'America/New_York', 'DFW': 'America/Chicago', 'DEN': 'America/Denver',
                'SFO': 'America/Los_Angeles', 'LAS': 'America/Los_Angeles', 'SEA': 'America/Los_Angeles',
                'MIA': 'America/New_York', 'YYZ': 'America/Toronto', 'YVR': 'America/Vancouver',
                'MEX': 'America/Mexico_City',
                
                # Europe
                'LHR': 'Europe/London', 'CDG': 'Europe/Paris', 'FRA': 'Europe/Berlin',
                'AMS': 'Europe/Amsterdam', 'MAD': 'Europe/Madrid', 'FCO': 'Europe/Rome',
                'MUC': 'Europe/Berlin', 'ZUR': 'Europe/Zurich', 'VIE': 'Europe/Vienna',
                'ARN': 'Europe/Stockholm', 'CPH': 'Europe/Copenhagen', 'HEL': 'Europe/Helsinki',
                'IST': 'Europe/Istanbul', 'SVO': 'Europe/Moscow',
                
                # Asia-Pacific
                'NRT': 'Asia/Tokyo', 'HND': 'Asia/Tokyo', 'ICN': 'Asia/Seoul',
                'PEK': 'Asia/Shanghai', 'PVG': 'Asia/Shanghai', 'HKG': 'Asia/Hong_Kong',
                'SIN': 'Asia/Singapore', 'BKK': 'Asia/Bangkok', 'KUL': 'Asia/Kuala_Lumpur',
                'CGK': 'Asia/Jakarta', 'SYD': 'Australia/Sydney', 'MEL': 'Australia/Melbourne',
                'BNE': 'Australia/Brisbane', 'AKL': 'Pacific/Auckland', 'DEL': 'Asia/Kolkata',
                'BOM': 'Asia/Kolkata', 'BLR': 'Asia/Kolkata', 'MAA': 'Asia/Kolkata',
                'HYD': 'Asia/Kolkata',
                
                # Middle East & Africa
                'DXB': 'Asia/Dubai', 'DOH': 'Asia/Qatar', 'AUH': 'Asia/Dubai',
                'KWI': 'Asia/Kuwait', 'CAI': 'Africa/Cairo', 'JNB': 'Africa/Johannesburg',
                'CPT': 'Africa/Johannesburg', 'NBO': 'Africa/Nairobi', 'ADD': 'Africa/Addis_Ababa',
                
                # South America
                'GRU': 'America/Sao_Paulo', 'GIG': 'America/Sao_Paulo', 'EZE': 'America/Argentina/Buenos_Aires',
                'SCL': 'America/Santiago', 'LIM': 'America/Lima', 'BOG': 'America/Bogota'
            }
            
            dep_timezone = timezone_map.get(dep_iata, 'UTC')
            arr_timezone = timezone_map.get(arr_iata, 'UTC')
            
            flight = {
                "flight_date": dep_time.strftime("%Y-%m-%d"),
                "flight_status": flight_status,
                "departure": {
                    "airport": airports[dep_iata],
                    "timezone": dep_timezone,
                    "iata": dep_iata,
                    "icao": f"K{dep_iata}",
                    "terminal": random.choice(terminals),
                    "gate": gates[0],
                    "scheduled": dep_time.isoformat() + "+00:00",
                    "estimated": actual_dep_time.isoformat() + "+00:00",
                    "actual": actual_dep_time.isoformat() + "+00:00" if flight_status == 'landed' else None,
                    "delay": max(0, int((actual_dep_time - dep_time).total_seconds() / 60)) if flight_status in ['delayed', 'landed'] else None
                },
                "arrival": {
                    "airport": airports[arr_iata],
                    "timezone": arr_timezone,
                    "iata": arr_iata,
                    "icao": f"K{arr_iata}",
                    "terminal": random.choice(terminals),
                    "gate": gates[1],
                    "scheduled": arr_time.isoformat() + "+00:00",
                    "estimated": actual_arr_time.isoformat() + "+00:00",
                    "actual": actual_arr_time.isoformat() + "+00:00" if flight_status == 'landed' else None,
                    "delay": max(0, int((actual_arr_time - arr_time).total_seconds() / 60)) if flight_status in ['delayed', 'landed'] else None
                },
                "airline": airline,
                "flight": {
                    "number": flight_number,
                    "iata": f"{airline['iata']}{flight_number}",
                    "icao": f"{airline['icao']}{flight_number}"
                },
                "aircraft": {
                    "registration": f"N{random.randint(100, 999)}{random.choice(['AA', 'UA', 'DL', 'WN', 'B6'])}",
                    "iata": random.choice(aircraft_types),
                    "icao": random.choice(aircraft_types)
                },
                "live": {
                    "updated": datetime.now().isoformat() + "+00:00",
                    "latitude": round(random.uniform(25.0, 50.0), 6),
                    "longitude": round(random.uniform(-125.0, -65.0), 6),
                    "altitude": random.randint(30000, 42000) if flight_status == 'active' else 0,
                    "direction": random.randint(0, 360),
                    "speed_horizontal": random.randint(400, 600) if flight_status == 'active' else 0,
                    "speed_vertical": random.randint(-10, 10) if flight_status == 'active' else 0,
                    "is_ground": flight_status not in ['active']
                }
            }
            
            flights.append(flight)
        
        return {
            "pagination": {
                "limit": 300,
                "offset": 0,
                "count": len(flights),
                "total": len(flights)
            },
            "data": flights
        }

    def process_data(self, data):
        """Process and analyze flight data"""
        if not data or 'data' not in data:
            return {}
        
        flights = data['data']
        df = pd.DataFrame(flights)
        
        # Extract insights
        insights = {
            'total_flights': len(flights),
            'popular_routes': self.get_popular_routes(flights),
            'airline_distribution': self.get_airline_distribution(flights),
            'peak_times': self.get_peak_times(flights),
            'airport_activity': self.get_airport_activity(flights)
        }
        
        return insights
    
    def get_popular_routes(self, flights):
        """Analyze popular routes"""
        routes = []
        for flight in flights:
            if flight.get('departure') and flight.get('arrival'):
                route = f"{flight['departure']['iata']}-{flight['arrival']['iata']}"
                routes.append(route)
        
        route_counts = pd.Series(routes).value_counts().head(10)
        return route_counts.to_dict()
    
    def get_airline_distribution(self, flights):
        """Analyze airline distribution"""
        airlines = []
        for flight in flights:
            if flight.get('airline'):
                airlines.append(flight['airline']['name'])
        
        airline_counts = pd.Series(airlines).value_counts().head(10)
        return airline_counts.to_dict()
    
    def get_peak_times(self, flights):
        """Analyze peak flight times"""
        times = []
        for flight in flights:
            if flight.get('departure') and flight['departure'].get('scheduled'):
                time_str = flight['departure']['scheduled']
                try:
                    dt = datetime.fromisoformat(time_str.replace('Z', '+00:00'))
                    times.append(dt.hour)
                except:
                    continue
        
        if times:
            time_counts = pd.Series(times).value_counts().head(10)
            return time_counts.to_dict()
        return {}
    
    def get_airport_activity(self, flights):
        """Analyze airport activity"""
        airports = []
        for flight in flights:
            if flight.get('departure'):
                airports.append(flight['departure']['iata'])
            if flight.get('arrival'):
                airports.append(flight['arrival']['iata'])
        
        airport_counts = pd.Series(airports).value_counts().head(10)
        return airport_counts.to_dict()

# Initialize the scraper
scraper = AirlineDataScraper()

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    """API endpoint to get flight data"""
    route_from = request.args.get('from', '')
    route_to = request.args.get('to', '')
    limit = int(request.args.get('limit', 50))
    
    # Get flight data
    data = scraper.get_flight_data(route_from, route_to, limit)
    
    # Process data for insights
    insights = scraper.process_data(data)
    
    return jsonify({
        'raw_data': data,
        'insights': insights,
        'status': 'success'
    })

@app.route('/api/insights')
def get_insights():
    """API endpoint to get processed insights"""
    data = scraper.get_flight_data()
    insights = scraper.process_data(data)
    
    return jsonify(insights)

@app.route('/api/charts')
def get_charts():
    """API endpoint to get chart data"""
    data = scraper.get_flight_data()
    insights = scraper.process_data(data)
    
    # Create charts
    charts = {}
    
    # Popular routes chart
    if insights.get('popular_routes'):
        routes = list(insights['popular_routes'].keys())
        counts = list(insights['popular_routes'].values())
        
        fig = go.Figure(data=[go.Bar(x=routes, y=counts)])
        fig.update_layout(title='Most Popular Routes', xaxis_title='Route', yaxis_title='Number of Flights')
        charts['popular_routes'] = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    # Airline distribution chart
    if insights.get('airline_distribution'):
        airlines = list(insights['airline_distribution'].keys())
        counts = list(insights['airline_distribution'].values())
        
        fig = go.Figure(data=[go.Pie(labels=airlines, values=counts)])
        fig.update_layout(title='Airline Distribution')
        charts['airline_distribution'] = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    # Peak times chart
    if insights.get('peak_times'):
        hours = list(insights['peak_times'].keys())
        counts = list(insights['peak_times'].values())
        
        fig = go.Figure(data=[go.Scatter(x=hours, y=counts, mode='lines+markers')])
        fig.update_layout(title='Peak Flight Times', xaxis_title='Hour of Day', yaxis_title='Number of Flights')
        charts['peak_times'] = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return jsonify(charts)

if __name__ == '__main__':
    # For deployment, use environment variables for host and port
    import os
    host = os.environ.get('HOST', '127.0.0.1')
    port = int(os.environ.get('PORT', 8080))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    app.run(debug=debug, host=host, port=port) 
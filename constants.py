url = 'https://www.indiavotes.com/lok-sabha'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

driver_path = 'C:/Users/vtsab/chromedriver-win64/chromedriver.exe'

lok_sabha_num = {
    1952: 1,
    1957: 2,
    1962: 3,
    1967: 4,
    1971: 5,
    1977: 6,
    1980: 7,
    1984: 8,
    1989: 9,
    1991: 10,
    1996: 11,
    1998: 12,
    1999: 13,
    2004: 14,
    2009: 15,
    2014: 16,
    2019: 17,
    2024: 18
}

state_codes = {
    'Ajmer': 17, # 1952 only
    'Andaman & Nicobar Islands': 34, # 1967 onwards
    'Andhra Pradesh': 27, # 2009 and earlier
    'Andhra Pradesh [2014 Onwards]': 62, # 2014 onwards
    'Arunachal Pradesh': 41, # 1977 onwards
    'Assam': 1, # all years
    'Bhopal': 18, # 1952 only
    'Bihar [1947 - 1999]': 2, # 1999 and earlier
    'Bihar [2000 Onwards]': 58, # 2000 onwards
    'Bilaspur': 19, # 1952 only
    'Bombay': 3, # 1952, 1957 yy
    'Chandigarh': 35, # 1967 onwards
    'Chhattisgarh': 54, # 2004 onwards
    'Coorg': 20, # 1952 only
    'Dadra & Nagar Haveli': 36, # 1967 onwards
    'Daman & Diu': 52, # 1977 onwards
    'Delhi': 21, # 1952-1971 yy
    'Delhi [1977 Onwards]': 57, #1977 onwards
    'Goa': 51, # 1989 onwards
    'Goa, Daman And Diu' : 37, # 1984 and earlier
    'Gujarat': 29, # 1962 onwards
    'Haryana': 31, # 1967 onwards
    'Himachal Pradesh': 22, # 1962 onwards
    'Hyderabad': 10, # 1952 only
    'Jammu & Kashmir': 32, # 1967 onwards
    'Jharkhand': 53, # 2004 onwards
    'Karnataka': 1943, # 1977 onwards
    'Kerala': 28, # 1957 onwards
    'Kutch': 23, # 1952 only
    'Laccadive, Minicoy And Amindivi Islands': 38, # 1967, 1971 yy
    'Ladakh': 63, # 2024 onwards
    'Lakshadweep': 48, # 1977 onwards
    'Madhya Bharat': 11, # 1952 only
    'Madhya Pradesh [1947 - 1999]': 4, # 1999 and earlier
    'Madhya Pradesh [2000 Onwards]': 59, # 2000 onwards
    'Madras': 5, # 1967 and earlier
    'Maharashtra': 30, # 1962 onwards
    'Manipur': 24, # all years
    'Meghalaya': 44, # 1977 onwards
    'Mizoram': 45, # 1977 onwards
    'Mysore': 12, # 1971 and earlier
    'Nagaland': 33, # 1967 onwards
    'Orissa': 6, # all years
    'Patiala And East Punj': 13, # 1952 only
    'Pondicherry': 39, # 1967 onwards
    'Punjab': 7, # all years
    'Rajasthan': 14, # all years
    'Saurashtra': 15, # 1952 only
    'Sikkim': 46, # 1977 onwards
    'Tamil Nadu': 40, # 1971 onwards
    'Telangana': 61, # 2014 onwards
    'Travancore Cochin': 16, # 1952 only
    'Tripura': 25, # all years
    'Uttar Pradesh [1947 - 1999]': 8, # 1999 and earlier
    'Uttar Pradesh [2000 Onwards]': 60, # 2000 onwards
    'Uttarakhand': 56, # 2004 onwards
    'Vindhya Pradesh': 26, # 1952 only
    'West Bengal': 9 # all years
}
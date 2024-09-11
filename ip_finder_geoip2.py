
import geoip2.database

# Setup the reader for the City database
city_reader = geoip2.database.Reader('/Users/macbook/Downloads/CS/Python/GeoLite2-City_20240621/GeoLite2-City.mmdb')

# Setup the reader for the Country database
country_reader = geoip2.database.Reader('/Users/macbook/Downloads/CS/Python/GeoLite2-Country_20240621/GeoLite2-Country.mmdb')

ip_address = '205.251.198.251'  # Example IP address

try:
    # Query the City database
    city_response = city_reader.city(ip_address)
    print("City Details:")
    print("Country:", city_response.country.name)
    print("State:", city_response.subdivisions.most_specific.name)
    print("City:", city_response.city.name)
    print("Postal Code:", city_response.postal.code)
    print("Latitude:", city_response.location.latitude)
    print("Longitude:", city_response.location.longitude)

    # Query the Country database
    country_response = country_reader.country(ip_address)
    print("\nCountry Details:")
    print("Country:", country_response.country.name)

except geoip2.errors.AddressNotFoundError:
    print("The address was not found in the database.")
except Exception as e:
    print("Error:", e)
finally:
    # Ensure both readers are closed properly
    city_reader.close()
    country_reader.close()

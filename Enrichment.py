import requests
import csv
import time
from bs4 import BeautifulSoup

# Define keyword list
keywords = [
    "24 Hour Porta Potty Rentals",
    "ADA-Compliant Portable Toilets",
    "Backyard Event Portable Toilets",
    "Bathroom Trailer Rentals",
    "Budget-Friendly Porta Potty Rentals",
    "Campground Portable Toilets",
    "Commercial Porta Potty Rentals",
    "Concert Portable Restrooms",
    "Construction Site Portable Toilets",
    "Deluxe Flushable Porta Potties",
    "Eco-Friendly Portable Toilets",
    "Emergency Porta Potty Rentals",
    "Event Portable Restrooms",
    "Executive Restroom Trailers",
    "Festival Portable Toilets",
    "Film Production Portable Toilets",
    "Hand Sanitizer Stations",
    "Hand Washing Stations",
    "High-Capacity Porta Potties",
    "Holding Tank Rentals",
    "Industrial Portable Toilets",
    "Indoor/Outdoor Restroom Rentals",
    "Long-Term Porta Potty Rentals",
    "Luxury Porta Potty Rentals",
    "Mobile Bathroom Rentals",
    "Mobile Hand Washing Stations",
    "Outdoor Wedding Restrooms",
    "Park & Recreation Restroom Rentals",
    "Porta John Rentals",
    "Porta Potty Cleaning Services",
    "Porta Potty Delivery & Setup",
    "Porta Potty Disposal Services",
    "Porta Potty Handicapped Units",
    "Porta Potty Maintenance Contracts",
    "Porta Potty Rental for Corporate Events",
    "Porta Potty Rental for Private Parties",
    "Porta Potty Rental for Sports Events",
    "Porta Potty Rental with Sinks",
    "Portable Restroom Trailers",
    "Portable Sanitation Services",
    "Portable Sink Rentals",
    "Private Event Portable Toilets",
    "Residential Porta Potty Rentals",
    "Restroom Trailer Rentals",
    "Roadside Construction Toilets",
    "School Event Portable Toilets",
    "Short-Term Porta Potty Rentals",
    "Special Event Porta Potties",
    "Standard Portable Toilets",
    "Temporary Restroom Solutions",
    "Towable Porta Potties",
    "Trailer-Mounted Restrooms",
    "Ultra-Luxury Portable Restrooms",
    "Urinal Station Rentals",
    "VIP Porta Potty Rentals",
    "VIP Restroom Trailers",
    "Waste Holding Tanks",
    "Weekend Porta Potty Rentals",
    "Wheelchair-Accessible Portable Toilets",
    "24 Hour Septic Cleaning",
    "24 Hour Septic Pumping",
    "24 Hour Septic Tank Cleaning",
    "Advanced Septic Treatment Systems",
    "Aerobic Septic Maintenance",
    "Aerobic Treatment Unit (ATU) System",
    "Affordable Septic Services",
    "Backhoe Service",
    "Bio-Enzyme Septic Treatments",
    "Camera Pipe Scoping",
    "Certified Septic Tank Specialists",
    "Cesspool Drain Field Repair",
    "Cesspool Pumping",
    "Cesspool Repair",
    "Cesspool Replacement",
    "Cesspool Service",
    "Chamber Septic System",
    "Cleaning",
    "Commercial Grease Trap Cleaning",
    "Commercial Septic Services",
    "Commercial Septic Tank Cleaning",
    "Constructed Wetland Septic System",
    "Conventional Septic System",
    "Drain Field Aeration Services",
    "Drain Field Replacement",
    "Drain Fields",
    "Drain Line Cleaning",
    "Drains Inspections",
    "Drip Distribution Septic System",
    "Effluent Filter Cleaning",
    "Emergency Grease Trap Cleaning",
    "Emergency Septic Pumping",
    "Emergency Septic Repair",
    "Evapotranspiration Septic System",
    "Excavation",
    "Family Owned",
    "Field Line Repairs",
    "Food Processing Grease Removal",
    "Free Estimates",
    "Gravity Septic System",
    "Grease Service",
    "Grease Trap Cleaning",
    "Grease Trap Compliance Inspections",
    "Grease Trap Inspection",
    "Grease Trap Pumping & Disposal",
    "Grease Trap Service",
    "Grease Traps",
    "Grease Waste Disposal Services",
    "High-Pressure Grease Line Cleaning",
    "High-Pressure Jet Rodding",
    "Home Inspection Letters",
    "Hydro Jetting",
    "Hydro Jetting for Septic Systems",
    "Indoor Grease Trap Service",
    "Industrial Grease Trap Services",
    "Industrial Septic Services",
    "Inspections",
    "Lift Station Maintenance",
    "Lift Station Repairs",
    "Lift Stations",
    "Locally Owned",
    "Marine Septic System Services",
    "Mound Septic System",
    "Municipal Septic Services",
    "No-Dig Septic Repairs",
    "Overflow Repairs",
    "Portable Restroom Septic Services",
    "Pressure Distribution Septic System",
    "Pump Replacement",
    "Pumping Out Septic Tanks",
    "Quarterly Maintenance",
    "Recirculating Sand Filter System",
    "Repair & Installation",
    "Residential Grease Trap Cleaning",
    "Residential Septic Tank Cleaning",
    "Restaurant Grease Trap Cleaning",
    "Riser Installations",
    "Riser Repair",
    "Root Removal",
    "Routine Septic Maintenance",
    "RV Septic Tank Pumping",
    "Rural Septic Services",
    "Same-Day Service",
    "Same-Day Services",
    "Sand Filter Septic System",
    "Schedule Maintenance",
    "Septic Design",
    "Septic Distribution Box Repair",
    "Septic Drain Field Restoration",
    "Septic Emergency",
    "Septic Field Repair",
    "Septic Holding Tank Services",
    "Septic Inspection",
    "Septic Inspections",
    "Septic Leach Field Pipe",
    "Septic Lid Replacement",
    "Septic Line Snaking Services",
    "Septic Maintenance Contracts",
    "Septic Repair",
    "Septic Riser Installation",
    "Septic Riser Installations",
    "Septic Service",
    "Septic System Backup Solutions",
    "Septic System Camera Inspections",
    "Septic System Cost Estimate",
    "Septic System Engineering & Design",
    "Septic System Installation Consultation",
    "Septic System Installations",
    "Septic System Inspections",
    "Septic System Permitting Assistance",
    "Septic System Repair",
    "Septic System Services",
    "Septic System Troubleshooting",
    "Septic System Upgrades",
    "Septic System Winterization",
    "Septic Tank and Leach Field Installation",
    "Septic Tank Bacteria Additives",
    "Septic Tank Cleaning",
    "Septic Tank Inspection Services",
    "Septic Tank Installation",
    "Septic Tank Leak Detection",
    "Septic Tank Lid Replacement",
    "Septic Tank Location",
    "Septic Tank Maintenance",
    "Septic Tank Odor Control",
    "Septic Tank Pumping",
    "Septic Tank Repair",
    "Septic Tank Replacement",
    "Septic Tank Risers & Lids",
    "Septic Tank Service",
    "Septic Tank System",
    "Sewer & Septic Line Replacement",
    "Sewer Inspection",
    "Sewer Line Cleaning",
    "Sewer Line Flushing",
    "Sewer Line Repair",
    "Sewer Pipe Relining",
    "Sewer Pumps",
    "Sewage Disposal",
    "Site and Soil Evaluation",
    "Sludge Removal Services",
    "Soil Percolation Testing",
    "Tank Repairs",
    "Trenchless Sewer Repair",
    "Video Inspection",
    "Video Pipe Scoping",
    "Wastewater Treatment Systems"
]

# Normalize keywords for comparison
keywords_lower = [kw.lower() for kw in keywords]

# Function to scrape page content and check for keywords
def scrape_and_match(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return []
        
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator=" ").lower()
        matches = [kw for kw in keywords_lower if kw in text]
        return matches
    except requests.RequestException:
        return []

# Main function to process input CSV and generate output CSV
def process_websites(input_csv="input.csv", output_csv="output.csv"):
    results = []

    with open(input_csv, "r", newline="", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        headers = next(reader)  # Read header row
        if "Website" not in headers:
            raise ValueError("Input CSV must contain a 'Website' column.")
        
        website_idx = headers.index("Website")

        for row in reader:
            website = row[website_idx].strip()
            if not website.startswith("http"):
                website = "http://" + website  # Ensure proper URL format

            print(f"Processing: {website}")
            matches = scrape_and_match(website)
            matched_keywords = ", ".join(matches) if matches else "No matches"
            print(f"  Matches found: {matched_keywords}")
            row.append(matched_keywords)
            results.append(row)
            time.sleep(1)  # Pause between requests

    # Write results to output CSV
    with open(output_csv, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        headers.append("Keyword Matches")
        writer.writerow(headers)
        writer.writerows(results)

    print("Processing complete. Results saved to", output_csv)

if __name__ == "__main__":
    process_websites()
#Project: Student Result Management System

#This project uses:

#if

#elif

#else

#nested conditions

#input

#type conversion

#basic calculations

#formatted output

#It will:

#ask student details

#ask marks for 3 subjects

#calculate total

#calculate percentage

#assign grade

#decide pass/fail

#decide distinction / first class / second class

#check voting eligibility

#print final report

print("==========LAND SUITABILITY CHECKER==========")

site_id = input("Enter the site ID: ")
land_cover = input("enter the land cover type (forest, agriculture, urban, baran): ").strip().lower()
soil_type = input("Enter the soil type(sandy, clay, loamy): ")
slope = float(input("Enter the slope of the land in degrees: "))
disatance_water = float(input("Enter the distance to the nearest water source in meters: "))
disatance_road = float(input("Enter the distance to the nearest road in meters: "))
protected_area = input("IS the land within a protected area? (yes/no): ").strip().lower()

# step 1: check protected area

if protected_area == "yes":
    suitability = " not suitable"
    reason = "site falls inside a protected area"
    recommendation = "reject site or perform strict environment review"


# step 2: slope check
else:
    if slope <= 5:
        slope_score = "HIGH"
    elif slope <= 15:
        slope_score = "Medium"
    else:
        slope_score = "Low"

    # step 3: land cover check
    if land_cover == "forest":
        land_cover_score = "Low"
    elif land_cover == "agriculture":
        land_cover_score = "Medium"
    elif land_cover == "urban":
        land_cover_score = "High"
    elif land_cover == " barren":
        land_cover_score = "Low"
    elif land_cover == "Wetland":
        land_cover_score = "Low"
    elif land_cover == "forest":
        land_cover_score = "Low"
    else:
        land_cover_score = "Unknown"    

    #step 4 road accessibility
    # 
    if disatance_road <= 500:
        road_score = "High"
    elif disatance_road <= 2000:
        road_score = "medium"
    else:
        road_score = "low"

    # water accessibility
    if disatance_water <= 1000:
        water_score = "HIGH"
    elif disatance_water <= 3000:
        water_score = "Medium"
    else:
        water_score = "Low"

    #step 6 Final suitability logic
    if land_cover_score == "Unknown":
        suitability = "Not suitable"
        reason = "Unknown land cover type"
        recommendation = "Review input data before ananlysis."

    elif slope_score == "HIGH" and land_cover_score == "High" and road_score == "High" and water_score == "HIGH":
      suitability = "High Suitable"
      reason = "Excellent slop, land cover, road access, and water access."
      recommendation = "Prioritize this site for development."

    elif slope_score == ["HIGH", "Medium"] and land_cover_score in ["High", "Medium"] and road_score == ["high", "Medium"] and water_score == ["high", "Medium"]:
        suitability = "Moderately Suitable"
        reason = "one or more scritical land factors resude suitability."
        recommendation = "Use only if better alternatives are unavailable."

    elif slope_score == "Low" or land_cover_score == "Low":
        suitability = "Low suitability"
        reason = "site conditions are mixed and below preferred criteria."
        recommendation = "further investigation required."

    #Final report

    print("\n====== LAND SUITABILITY REPORT ======")
    print(f"site ID: {site_id}")
    print(f"Land_Cover: {land_cover}")
    print(f"slope: {slope} degrees")
    print(f"Distance to road: {disatance_road}")
    print(f"Distance to water: {disatance_water}")
    print(f"protected Area: {protected_area}")

    if protected_area != "Yes":
        print("\n--- Sutability Factors ---")
        print(f"slope score: {slope_score}")
        print(f"Land cover Score: {land_cover_score}")
        print(f"Road access score: {road_score}")
        print(f"water access score: {water_score}")


    print("\n--- Final decision ---")
    print(f"Sutability: {suitability}")
    print(f"reason: {reason}")
    print(f"Reccommendation: {recommendation}")


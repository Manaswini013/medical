# Medicine Database (Sample - Expand with 40 medicines)
medicines = {
    'paracetamol': {
        'uses': 'Pain reliever and fever reducer',
        'adult_dosage': '500mg every 4-6 hours, not exceeding 4g per day',
        'children_dosage': '10-15mg/kg body weight every 4-6 hours',
        'warnings': 'Do not exceed the recommended dose. Liver damage risk if overdosed.'
    },
    'ibuprofen': {
        'uses': 'Anti-inflammatory, pain reliever, and fever reducer',
        'adult_dosage': '200-400mg every 4-6 hours, not exceeding 1.2g per day',
        'children_dosage': '5-10mg/kg body weight every 6-8 hours',
        'warnings': 'May cause stomach irritation, ulcers, or gastrointestinal bleeding.'
    },
    'aspirin': {
        'uses': 'Pain relief, anti-inflammatory, and fever reduction',
        'adult_dosage': '325-650mg every 4-6 hours, not exceeding 4g per day',
        'children_dosage': 'Not recommended for children due to risk of Reye’s syndrome',
        'warnings': 'May cause stomach bleeding. Do not take with alcohol.'
    },
    'cetirizine': {
        'uses': 'Antihistamine for allergy relief (hay fever, hives)',
        'adult_dosage': '10mg once daily',
        'children_dosage': '1-6 years: 2.5mg once daily, 6-12 years: 5mg once daily',
        'warnings': 'May cause drowsiness. Avoid alcohol while taking.'
    },
    'loperamide': {
        'uses': 'Anti-diarrheal medication',
        'adult_dosage': '2mg after each loose stool, not exceeding 8mg per day',
        'children_dosage': '2-5 years: 1mg after each loose stool, 6-8 years: 2mg',
        'warnings': 'Not recommended for children under 2 years. Overdose may cause serious heart problems.'
    },
    'omeprazole': {
        'uses': 'Proton pump inhibitor for acid reflux, ulcers',
        'adult_dosage': '20mg once daily for 4-8 weeks',
        'children_dosage': 'Not typically recommended for children under 1 year',
        'warnings': 'May increase the risk of bone fractures. Long-term use may lead to low magnesium levels.'
    },
    'diphenhydramine': {
        'uses': 'Antihistamine for allergy symptoms and sleep aid',
        'adult_dosage': '25-50mg every 4-6 hours, not exceeding 300mg per day',
        'children_dosage': '6-12 years: 12.5-25mg every 4-6 hours',
        'warnings': 'May cause drowsiness. Avoid alcohol. Not suitable for young children under 6 years.'
    },
    'gaviscon': {
        'uses': 'Antacid for heartburn and acid indigestion',
        'adult_dosage': '10-20mL after meals and at bedtime',
        'children_dosage': '2-12 years: 5-10mL after meals',
        'warnings': 'Consult a doctor if symptoms persist for more than 2 weeks.'
    },
    'hydrocortisone': {
        'uses': 'Topical steroid for skin conditions (eczema, dermatitis)',
        'adult_dosage': 'Apply a thin layer to affected area 1-2 times daily',
        'children_dosage': 'Not recommended for children under 2 years without a doctor’s advice',
        'warnings': 'Avoid prolonged use to prevent skin thinning.'
    },
    'saline_nasal_spray': {
        'uses': 'Relieves nasal congestion',
        'adult_dosage': 'Spray 1-2 doses in each nostril as needed',
        'children_dosage': 'Not recommended for children under 2 years',
        'warnings': 'Do not use for more than 3 consecutive days to avoid rebound congestion.'
    }
    # Add more medicines (expand with at least 40 medicines)
}

def get_medicine_info(medicine_name):
    """
    Retrieve and display information about a given medicine.
    """
    # Convert input to lowercase for case-insensitive search
    medicine_name = medicine_name.lower()
    
    # Check if the medicine exists in the database
    if medicine_name in medicines:
        med_info = medicines[medicine_name]
        print(f"\nMedicine: {medicine_name.capitalize()}")
        print(f"Uses: {med_info['uses']}")
        print(f"Dosage (Adult): {med_info['adult_dosage']}")
        print(f"Dosage (Children): {med_info['children_dosage']}")
        print(f"Warnings: {med_info['warnings']}\n")
    else:
        print("Medicine not found. Please check the name or try another one.\n")

def main():
    """
    Main function to run the Medicine Recommendation System.
    """
    print("Welcome to the Medicine Recommendation System")
    print("You can search for any basic medicine without a prescription.\n")
    
    # Ask user for the medicine they want information about
    while True:
        medicine_name = input("Enter medicine name (or type 'exit' to quit): ").strip()
        if medicine_name.lower() == 'exit':
            print("Goodbye!")
            break
        else:
            get_medicine_info(medicine_name)

# Run the main function if this script is executed
if __name__ == "__main__":
    main()

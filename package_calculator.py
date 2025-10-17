PACKAGE_DIMENSIONS = {
    "small": "10cm x 15cm x 5cm",
    "medium": "30cm x 40cm x 15cm",
    "large": "60cm x 70cm x 30cm",
}

def get_package_dimensions(item_size):
    
    cleaned_size = item_size.strip().lower()

    error_message = f"Error: '{item_size}' is not a valid size. Please use 'small', 'medium', or 'large'."
    return PACKAGE_DIMENSIONS.get(cleaned_size, error_message)

def main():
    print("--- Package Dimension Calculator ---")
    print("Find the right package for your item.")
    print("Available sizes: small, medium, large\n")

    user_input = input("Please enter the size of your item: ")
    dimensions = get_package_dimensions(user_input)

    print("\n----------------------------------------")
    print(f"> Result: {dimensions}")
    print("----------------------------------------")

if __name__ == "__main__":
    main()
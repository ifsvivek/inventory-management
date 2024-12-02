import cv2
import pytesseract
import json
import os
import re  # Added import statement

# File to store product-rack data
JSON_FILE = "product_racks.json"

# Tesseract-OCR configuration
pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"  # Adjust path as needed


def extract_text_from_image(image_path):
    """Extract text from an image using Tesseract-OCR."""
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Image at '{image_path}' not found.")
        return ""

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to enhance text detection
    _, binary_image = cv2.threshold(
        gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU
    )

    # Extract text using Tesseract
    extracted_text = pytesseract.image_to_string(binary_image, lang="eng")
    return extracted_text


def parse_extracted_text(text):
    """Parse extracted text into product and rack pairs."""
    # Use regex to find product names and rack numbers
    products = re.findall(r"Product\s+(\w+)", text)
    racks = re.findall(r"Pack\s+([A-Z]\d+)", text)

    # Pair products with racks
    product_rack_pairs = []
    for product, rack in zip(products, racks):
        product_rack_pairs.append({"product_name": product, "rack_number": rack})
    return product_rack_pairs


def load_data():
    """Load existing product data from the JSON file."""
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    """Save product data to the JSON file."""
    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {JSON_FILE}.")


def display_data(data):
    """Display all stored products and their racks."""
    print("\nStored Products:")
    if not data:
        print("No data found.")
        return
    for entry in data:
        print(f"Product: {entry['product_name']} -> Rack: {entry['rack_number']}")


def search_product(data, product_name):
    """Search for a product and display where it is stored."""
    found = False
    for entry in data:
        if entry["product_name"].lower() == product_name.lower():
            print(
                f"Product: {entry['product_name']} is stored in Rack: {entry['rack_number']}"
            )
            found = True
            break
    if not found:
        print(f"Product '{product_name}' not found in the inventory.")


# Main logic
if __name__ == "__main__":
    # Load existing data
    product_data = load_data()

    while True:
        print("\nMenu:")
        print("1. Display all stored products")
        print("2. Process an image to extract products and racks")
        print("3. Search for a product to see where it is stored")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_data(product_data)
        elif choice == "2":
            image_path = input("Enter the image path: ")
            print("\nProcessing image to extract products and racks...")
            extracted_text = extract_text_from_image(image_path)
            if extracted_text:
                print("\nExtracted Text:\n", extracted_text)

                # Parse the text and add to data
                new_data = parse_extracted_text(extracted_text)
                if new_data:
                    print("\nNew Data Parsed:")
                    for entry in new_data:
                        print(
                            f"Product: {entry['product_name']} -> Rack: {entry['rack_number']}"
                        )
                    product_data.extend(new_data)
                    save_data(product_data)  # Save updated data to JSON

                    # Display final data
                    print("\nUpdated Product List:")
                    display_data(product_data)
                else:
                    print("No valid product-rack pairs found in the extracted text.")
            else:
                print("No text extracted from the image.")
        elif choice == "3":
            product_name = input("Enter the product name to search for: ")
            search_product(product_data, product_name)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

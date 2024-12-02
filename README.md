# Product Rack Management System

This project is a Python-based **Product Rack Management System** that extracts, processes, and stores information about products and their associated rack numbers. The system includes two key features: extracting product data from images using OCR (Tesseract) and visually creating labeled product representations with rack numbers in an organized grid using Pillow.

---

## Features

1. **Image Text Extraction**:

    - Extract product names and rack numbers from images using **Tesseract-OCR**.
    - Automatically processes images with grayscale conversion and thresholding for better OCR accuracy.

2. **Data Storage in JSON**:

    - Stores product names and rack numbers in a JSON file for persistent storage.
    - Updates the JSON file dynamically whenever new products are added.

3. **Search Functionality**:

    - Search for a product by name and find its corresponding rack number.

4. **Visual Representation**:

    - Generates an image using Pillow, where products and their rack numbers are displayed in labeled boxes.

5. **Interactive CLI Menu**:
    - Easy-to-use CLI interface to:
        - Display stored products.
        - Process an image to extract product data.
        - Search for a specific product.
        - Exit the application.

---

## How It Works

1. **Text Extraction from Images**:

    - Reads an input image using OpenCV and preprocesses it for better text detection.
    - Uses Tesseract-OCR to extract text in the format:  
      `Product: <Product Name>`  
      `Rack: <Rack Number>`.

2. **Parsing Extracted Text**:

    - Extracts and pairs product names and rack numbers using regular expressions.

3. **Data Storage**:

    - Stores all product-rack pairs in a JSON file named `product_racks.json`.
    - Ensures existing data is preserved while new data is added.

4. **Visual Representation**:

    - Draws boxes for each product with its name and rack number.
    - Organizes boxes into rows and columns for a neat and clear layout.

5. **Search Functionality**:
    - Allows users to find a product by its name and displays the corresponding rack.

---

## Requirements

### Libraries

Install the following Python libraries before running the code:

```bash
pip install opencv-python pytesseract pillow
```

### Additional Dependencies

-   **Tesseract-OCR**:
    -   Install Tesseract on Ubuntu:
        ```bash
        sudo apt update
        sudo apt install tesseract-ocr
        ```
    -   Adjust the `pytesseract.pytesseract.tesseract_cmd` path in the script if needed.

---

## Usage Instructions

1. **Clone or Download the Project**:

    - Clone this repository or download the files.

2. **Run the Script**:

    - Execute the Python script:
        ```bash
        python main.py
        ```

3. **Interactive Menu**:

    - The menu provides the following options:
        1. **Display all stored products**: View the current product-rack pairs stored in `product_racks.json`.
        2. **Process an image**: Enter the path to an image file, and the program will extract product data and update the JSON file.
        3. **Search for a product**: Enter a product name to search and locate its rack.
        4. **Exit**: Quit the application.

4. **Generated Visual Representation**:
    - The script creates an image (`product_shelf.png`) with all products displayed in labeled boxes.

---

## Project Files

1. **`main.py`**:

    - Main script for text extraction, JSON management, and visual representation.

2. **`product_racks.json`**:

    - JSON file to store product and rack information.

3. **`product_shelf.png`**:
    - Dynamically generated image showing products and rack numbers in boxes.

---

## Example Workflow

1. **Process an Image**:

    - Example Input Image:

        - Contains text like:
            ```
            Product: Oats
            Rack: A20
            Product: Bread
            Rack: B21
            ```

    - Output:
        - Text extracted and stored as:
            ```json
            [
                { "product_name": "Oats", "rack_number": "A20" },
                { "product_name": "Bread", "rack_number": "B21" }
            ]
            ```

2. **Visual Representation**:

    - Generated image with labeled boxes for `Oats` (Rack A20) and `Bread` (Rack B21).

3. **Search**:
    - Searching for "Oats" will display:
        ```
        Product: Oats is stored in Rack: A20
        ```

---

## Customization

-   **Add New Products**:
    -   Update the `products` list in the visual representation script to include new items.
-   **Adjust Layout**:
    -   Change the grid layout by modifying `columns` or spacing.

---

## Future Improvements

-   Add error handling for invalid or missing images.
-   Enhance OCR accuracy with advanced preprocessing techniques.
-   Allow exporting visual representations as PDFs or other formats.

from PIL import Image, ImageDraw, ImageFont

# Create a blank image
width, height = 1200, 800  # Increased dimensions to fit all products
image = Image.new("RGB", (width, height), "white")  # White background

# Initialize drawing context
draw = ImageDraw.Draw(image)

# Define products and their rack numbers
products = [
    {"name": "Oats", "rack": "A20"},
    {"name": "Bread", "rack": "B21"},
    {"name": "Milk", "rack": "D23"},
    {"name": "Eggs", "rack": "E24"},
    {"name": "Butter", "rack": "F25"},
    {"name": "Cheese", "rack": "G26"},
    {"name": "Yogurt", "rack": "H27"},
    {"name": "Juice", "rack": "I28"},
    {"name": "Water", "rack": "J29"},
    {"name": "Soda", "rack": "K30"},
    {"name": "Chips", "rack": "L31"},
    {"name": "Candy", "rack": "M32"},
    {"name": "Chocolate", "rack": "N33"},
    {"name": "Coffee", "rack": "O34"},
    {"name": "Tea", "rack": "P35"},
]

# Define box dimensions and spacing
box_width, box_height = 200, 100
spacing = 50
x_start = 50
y_start = 50
columns = 4  # Number of columns in the grid

# Draw boxes with product names and rack numbers
for i, product in enumerate(products):
    row = i // columns
    col = i % columns
    x1 = x_start + col * (box_width + spacing)
    y1 = y_start + row * (box_height + spacing)
    x2 = x1 + box_width
    y2 = y1 + box_height

    # Draw rectangle
    draw.rectangle([x1, y1, x2, y2], outline="black", width=3)

    # Add text for product name and rack number
    text_product = f"Product: {product['name']}"
    text_rack = f"Rack: {product['rack']}"
    text_x = x1 + 10
    text_y = y1 + 10

    # Load a default font
    font = ImageFont.load_default()

    # Draw the text
    draw.text((text_x, text_y), text_product, fill="black", font=font)
    draw.text((text_x, text_y + 20), text_rack, fill="black", font=font)

# Save the image
image.save("product_shelf.png")

# Display the image (Optional, depends on the environment)
image.show()
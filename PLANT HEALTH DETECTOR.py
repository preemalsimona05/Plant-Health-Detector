
# Plant Health Detector
from PIL import Image
import matplotlib.pyplot as plt

def plant_health(image_path):
    # 1. Open image safely
    try:
        img = Image.open(image_path).convert("RGB")
    except FileNotFoundError:
        print("Image not found:", image_path)
        return
    except Exception as e:
        print("Cannot open image:", e)
        return

    # 2. Resize image for faster processing
    img = img.resize((200, 200))
    pixels = img.load()

    green_count = 0
    yellow_count = 0

    # 3. Check each pixel
    for x in range(200):
        for y in range(200):
            r, g, b = pixels[x, y]
            if g > r and g > b:  # Green = healthy
                green_count += 1
            elif r > g and g > b:  # Yellow = stressed
                yellow_count += 1

    # 4. Calculate percentages
    total_pixels = 200 * 200
    green_percent = (green_count / total_pixels) * 100
    yellow_percent = (yellow_count / total_pixels) * 100
    other_percent = 100 - (green_percent + yellow_percent)

    print("Green area:", round(green_percent, 2), "%")
    print("Yellow area:", round(yellow_percent, 2), "%")
    print("Other area:", round(other_percent, 2), "%")

    # 5. Create bar chart
    labels = ['Green', 'Yellow', 'Other']
    values = [green_percent, yellow_percent, other_percent]

    plt.figure(figsize=(6,4))
    plt.bar(labels, values, color=['green', 'yellow', 'gray'])
    plt.title("Leaf Color Percentage")
    plt.ylabel("Percentage (%)")
    plt.ylim(0, 100)
    plt.savefig("leaf_bar_chart.png")
    plt.close()
    print("Saved bar chart: leaf_bar_chart.png")

    # 6. Create pie chart
    labels = ['Healthy', 'Diseased']
    values = [green_percent, yellow_percent]
    plt.figure(figsize=(5,5))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=140, colors=['green', 'red'])
    plt.title("Leaf Health Distribution")
    plt.savefig("leaf_pie_chart.png")
    plt.close()
    print("Saved pie chart: leaf_pie_chart.png")

# --- Run the program ---
image_path = input("Enter the path of the leaf image: ")
plant_health(image_path)

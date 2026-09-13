from PIL import Image
from pathlib import Path

folder = Path("static")

for image_path in folder.glob("*.jpg"):
    output_path = image_path.with_suffix(".webp")

    try :
        img = Image.open(image_path)
        img.save(output_path, format="WEBP", quality=85)

        print(f"OK : {image_path.name} -> {output_path.name}")
    except Exception as e:
        print(f"Error : {image_path.name} -> {e}")

print("Done !")
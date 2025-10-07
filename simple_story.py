import ollama
import os

def create_story_from_image(image_path: str):
    """
    Analyzes an image and generates a complete short story based on it.
    Uses only one model call to minimize resource usage.
    """

    if not os.path.exists(image_path):
        print("❌ Image file not found!")
        return

    print("╔════════════════════════════════════════════════════════╗")
    print("║     Image Story Generator - Ollama Edition             ║")
    print("╚════════════════════════════════════════════════════════╝\n")

    print("📸 Analyzing image and creating story...\n")

    # Single prompt that does both analysis and story generation
    prompt = """
    Look at this image and create a complete short story (3-4 paragraphs) based on what you see.

    Your story should:
    1. Describe the scene and setting from the image
    2. Introduce a character or perspective
    3. Create a brief narrative arc with beginning, middle, and end
    4. Be engaging and immersive

    Write the complete story, ready to be read.
    """

    try:
        response = ollama.chat(
            model="llava",
            messages=[{
                'role': 'user',
                'content': prompt,
                'images': [image_path]
            }]
        )

        story = response['message']['content']

        # Display with nice formatting
        print("╔════════════════════════════════════════════════════════╗")
        print("║                    YOUR STORY                          ║")
        print("╚════════════════════════════════════════════════════════╝\n")

        # Word wrap and display
        import textwrap
        wrapped = textwrap.fill(story, width=60)
        print(wrapped)

        # Save to file
        image_name = os.path.splitext(os.path.basename(image_path))[0]
        output_file = f"{image_name}_story.txt"

        with open(output_file, 'w') as f:
            f.write("=" * 60 + "\n")
            f.write("STORY GENERATED FROM: " + os.path.basename(image_path) + "\n")
            f.write("=" * 60 + "\n\n")
            f.write(story)
            f.write("\n\n" + "=" * 60 + "\n")

        print("\n" + "="*60)
        print(f"✨ Story complete! Saved to: {output_file}")

    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nMake sure you have llava installed:")
        print("  ollama pull llava")

def main():
    print("Enter image path (or drag and drop file): ")
    image_path = input().strip().strip("'\"")  # Remove quotes if dragged

    create_story_from_image(image_path)

if __name__ == "__main__":
    main()

# 📖 Ollama Image Story Generator

A Python application that uses AI to analyze images and generate stories based on what it sees. Built with Ollama's vision and language models for an educational multimedia project.

## ✨ Features

- **Single Image Analysis**: Upload any image and get a complete narrative story
- **AI-Powered Storytelling**: Uses Ollama's LLaVA vision model to understand images and create engaging narratives
- **Interactive Mode**: Full-featured interactive storytelling with branching narratives and choices
- **Automatic Story Saving**: Stories are automatically saved to text files for easy sharing
- **Multimedia Suggestions**: Generate audio and visual parameters for enhanced storytelling

## 🛠️ Requirements

- Python 3.7+
- Ollama installed and running
- LLaVA model (required)
- Llama2 model (optional, for interactive mode)

## 📦 Installation

1. **Install Ollama**
   ```bash
   # macOS
   brew install ollama

   # Or download from https://ollama.com/download
   ```

2. **Download the required models**
   ```bash
   # Required for all modes
   ollama pull llava

   # Optional: for interactive storytelling
   ollama pull llama2
   ```

3. **Set up Python environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install ollama
   ```

## 🚀 Usage

### Simple Mode (Recommended for Quick Stories)

Generates a complete story from a single image with minimal resource usage.

```bash
source venv/bin/activate
python simple_story.py
```

**Resource Usage:**
- RAM: ~4-7GB
- Generation time: 5-10 seconds
- Model calls: 1

**Best for:**
- Quick story generation
- Lower-end hardware
- Simple presentations
- One-off story creation

### Interactive Mode (Advanced)

Full-featured interactive storytelling with player choices and branching narratives.

```bash
source venv/bin/activate
python generator.py
```

**Resource Usage:**
- RAM: ~8-12GB
- Generation time: Variable (multiple rounds)
- Model calls: 2-3 per story turn

**Best for:**
- Interactive experiences
- Longer storytelling sessions
- Demonstrations of AI capabilities
- Multiple story paths exploration

## 📝 Example (Simple Mode)

```bash
$ python simple_story.py
Enter image path (or drag and drop file):
theoffice.png

╔════════════════════════════════════════════════════════╗
║     Image Story Generator - Ollama Edition             ║
╚════════════════════════════════════════════════════════╝

📸 Analyzing image and creating story...

[Story generated and displayed]

✨ Story complete! Saved to: theoffice_story.txt
```

## 🎯 How It Works

### Simple Mode
1. Accepts an image file path as input
2. Sends the image to Ollama's LLaVA vision model with a structured prompt
3. The AI analyzes the image and generates a 3-4 paragraph story with:
   - Scene description based on visual elements
   - Character introduction and perspective
   - A narrative arc (beginning, middle, end)
4. The story is displayed with formatting and saved to a text file

### Interactive Mode
1. Analyzes an input image to establish the setting and initial scene
2. Generates a narrative introduction based on the image analysis
3. Creates 3 meaningful choices for the player at each decision point
4. Continues the story based on player choices while maintaining narrative consistency
5. Suggests audio parameters and visual elements for each scene
6. Maintains story context throughout the session

## 💡 Mode Comparison

| Feature | Simple Mode | Interactive Mode |
|---------|-------------|------------------|
| Resource Usage | Low (4-7GB) | High (8-12GB) |
| Generation Speed | Fast (5-10s) | Variable |
| Story Length | Fixed (3-4 paragraphs) | Dynamic |
| User Interaction | None | Full choices |
| Models Required | LLaVA only | LLaVA + Llama2 |
| Multimedia Features | No | Yes (audio/visual) |
| Best For | Presentations | Demonstrations |

## 🔧 Technical Details

**Simple Mode:**
- **Model**: LLaVA (Large Language and Vision Assistant)
- **Model Size**: ~4.7GB
- **Memory Usage**: 4-7GB during generation
- **Average Generation Time**: 5-10 seconds per story
- **Output Format**: Plain text with word wrapping at 60 characters

**Interactive Mode:**
- **Models**: LLaVA + Llama2
- **Combined Size**: ~8.5GB
- **Memory Usage**: 8-12GB during session
- **Generation Time**: 10-15 seconds per turn
- **Features**: Choice generation, context memory, multimedia parameters

## 📚 Project Structure

```
ollama-storyteller/
├── simple_story.py          # Simple single-shot story generator
├── generator.py             # Interactive story system orchestrator
├── story_generator.py       # Interactive story generation engine
├── multimedia_enhancer.py   # Audio/visual parameter generation
├── venv/                    # Python virtual environment
└── README.md                # This file
```

## 🎓 Educational Context

Created for a multimedia project to demonstrate:
- AI multimodal capabilities (text + vision)
- Natural language generation
- Practical use of local LLMs
- Interactive narrative systems
- Resource-conscious AI application design

## 🐛 Troubleshooting

**"Failed to connect to Ollama"**
- Make sure Ollama is running: `ollama serve`
- Check if Ollama is installed: `which ollama`

**"Model not found"**
- Download LLaVA: `ollama pull llava`
- For interactive mode: `ollama pull llama2`
- List installed models: `ollama list`

**"Module not found: ollama"**
- Activate virtual environment: `source venv/bin/activate`
- Install package: `pip install ollama`

**Out of memory errors**
- Use simple mode instead of interactive mode
- Close other applications
- Restart Ollama: `pkill ollama && ollama serve`

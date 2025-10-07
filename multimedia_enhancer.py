import ollama
from typing import Dict, List

class MultimediaEnhancer:
    """
    Classe para adicionar elementos multimídia à experiência.
    Demonstra como o Ollama pode gerar parâmetros para outros sistemas.
    """
    
    def __init__(self):
        self.sound_mappings = {
            "forest": {"ambient": "birds", "volume": 0.3},
            "cave": {"ambient": "dripping", "volume": 0.5},
            "city": {"ambient": "traffic", "volume": 0.4},
            "ocean": {"ambient": "waves", "volume": 0.6}
        }
    
    def generate_scene_audio_params(self, scene_description: str) -> Dict:
        """
        Analisa a descrição da cena e sugere parâmetros de áudio.
        Isso demonstra como o Ollama pode controlar outros aspectos multimídia.
        """
        
        prompt = f"""
        Scene: {scene_description}
        
        Suggest audio parameters for this scene:
        1. Ambient sound type
        2. Music mood (mysterious/cheerful/tense/calm)
        3. Key sound effects needed
        4. Volume levels (0.0 to 1.0)
        
        Format as JSON.
        """
        
        response = ollama.chat(
            model="llama2",
            messages=[{
                'role': 'user',
                'content': prompt
            }]
        )
        
        # Aqui você poderia integrar com pygame.mixer para tocar sons reais
        return response['message']['content']
    
    def generate_visual_elements(self, scene_description: str) -> List[Dict]:
        """
        Gera descrições de elementos visuais que poderiam ser renderizados.
        Útil para criar mapas ou representações visuais simples da narrativa.
        """
        
        prompt = f"""
        Scene: {scene_description}
        
        List visual elements that should be displayed:
        1. Key objects (with suggested positions: left/center/right)
        2. Colors for atmosphere
        3. Simple shapes to represent elements
        
        Format as a list of simple drawing instructions.
        """
        
        response = ollama.chat(
            model="llama2",
            messages=[{
                'role': 'user',
                'content': prompt
            }]
        )
        
        return response['message']['content']

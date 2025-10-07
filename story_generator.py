import ollama
import json
from typing import Dict

class InteractiveStoryGenerator:
    """
    Classe principal que gerencia a criação de histórias interativas
    baseadas em análise de imagens usando Ollama.
    """
    
    def __init__(self, model_vision: str = "llava", model_text: str = "llama2"):
        """
        Inicializa o gerador com os modelos especificados.
        
        model_vision: modelo multimodal para análise de imagens
        model_text: modelo de texto para geração de narrativa
        """
        self.model_vision = model_vision
        self.model_text = model_text
        self.story_context = []  # Mantém o histórico da narrativa
        
    def analyze_image(self, image_path: str) -> Dict[str, any]:
        """
        Analisa uma imagem e extrai elementos narrativos dela.
        Esta é a parte mais importante para demonstrar capacidades multimodais.
        """
        
        # Primeiro, vamos analisar objetivamente a imagem
        objective_prompt = """
        Analyze this image and identify:
        1. Main objects and characters present
        2. Setting/environment description
        3. Mood and atmosphere
        4. Any text or symbols visible
        5. Colors and lighting
        
        Be specific and detailed. Format as JSON.
        """
        
        try:
            # O Ollama aceita diretamente o caminho da imagem
            response = ollama.chat(
                model=self.model_vision,
                messages=[{
                    'role': 'user',
                    'content': objective_prompt,
                    'images': [image_path]
                }]
            )
            
            analysis = response['message']['content']
            
            # Agora, vamos criar uma narrativa baseada na análise
            narrative_prompt = f"""
            Based on this image analysis: {analysis}
            
            Create an engaging story introduction that:
            1. Sets up a mysterious or intriguing scenario
            2. Introduces a protagonist (can be the viewer)
            3. Hints at a larger adventure
            4. Ends with a moment requiring a decision
            
            Make it immersive and about 3-4 paragraphs.
            """
            
            narrative_response = ollama.chat(
                model=self.model_text,
                messages=[{
                    'role': 'user',
                    'content': narrative_prompt
                }]
            )
            
            return {
                'analysis': analysis,
                'narrative': narrative_response['message']['content']
            }
            
        except Exception as e:
            print(f"Erro ao analisar imagem: {e}")
            return None
    
    def generate_choices(self, current_scene: str, num_choices: int = 3) -> Dict[str, str]:
        """
        Gera escolhas interativas baseadas na cena atual.
        Demonstra a capacidade do modelo de manter coerência narrativa.
        """
        
        # Construir o contexto completo da história até agora
        context = "\n".join(self.story_context[-3:])  # Últimas 3 cenas para contexto
        
        prompt = f"""
        Story context: {context}
        Current scene: {current_scene}
        
        Generate {num_choices} distinct choices for the player.
        Each choice should:
        1. Be meaningful and lead to different outcomes
        2. Be consistent with the story tone
        3. Offer different types of actions (explore, interact, observe)
        
        Format as JSON with keys "choice1", "choice2", "choice3" and their descriptions.
        Example format:
        {{
            "choice1": {{"action": "Investigate the glowing crystal", "hint": "might reveal magic"}},
            "choice2": {{"action": "Follow the shadowy figure", "hint": "could be dangerous"}},
            "choice3": {{"action": "Read the ancient book", "hint": "knowledge awaits"}}
        }}
        """
        
        response = ollama.chat(
            model=self.model_text,
            messages=[{
                'role': 'user',
                'content': prompt
            }]
        )
        
        try:
            # Tentar fazer parse do JSON na resposta
            content = response['message']['content']
            # Limpar possível markdown
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0]
            elif "```" in content:
                content = content.split("```")[1].split("```")[0]
                
            choices = json.loads(content)
            return choices
        except:
            # Fallback caso o parsing falhe
            return {
                "choice1": {"action": "Explorar adiante", "hint": "descobrir o desconhecido"},
                "choice2": {"action": "Examinar os arredores", "hint": "procurar pistas"},
                "choice3": {"action": "Voltar", "hint": "buscar outro caminho"}
            }
    
    def continue_story(self, choice: str, previous_scene: str) -> str:
        """
        Continua a narrativa baseada na escolha do jogador.
        Mantém coerência com elementos visuais identificados anteriormente.
        """
        
        prompt = f"""
        Previous scene: {previous_scene}
        Player choice: {choice}
        Story context: {' '.join(self.story_context[-2:])}
        
        Continue the story based on this choice. 
        Write 2-3 paragraphs that:
        1. Show the immediate consequence of the choice
        2. Introduce a new element or revelation
        3. End with another decision point
        
        Keep the tone consistent and reference previous visual elements when relevant.
        """
        
        response = ollama.chat(
            model=self.model_text,
            messages=[{
                'role': 'user',
                'content': prompt
            }]
        )
        
        continuation = response['message']['content']
        self.story_context.append(continuation)
        
        return continuation

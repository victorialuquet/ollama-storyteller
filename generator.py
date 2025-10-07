import os
from typing import Dict, Optional
from dataclasses import dataclass
from multimedia_enhancer import MultimediaEnhancer
from story_generator import InteractiveStoryGenerator

@dataclass
class StoryNode:
    """
    Representa um ponto na narrativa interativa.
    Cada nó contém a descrição da cena atual e as escolhas possíveis.
    """
    description: str
    image_analysis: str
    choices: Dict[str, str]
    image_path: Optional[str] = None


def main():
    """
    Demonstração completa do sistema de história interativa multimodal.
    """
    
    print("=== Gerador de Histórias Interativas com Ollama ===\n")
    
    # Inicializar o gerador
    generator = InteractiveStoryGenerator()
    enhancer = MultimediaEnhancer()
    
    # Solicitar uma imagem ao usuário
    image_path = input("Digite o caminho para uma imagem: ").strip()
    
    if not os.path.exists(image_path):
        print("Arquivo não encontrado!")
        return
    
    print("\n📖 Analisando imagem e criando narrativa inicial...")
    
    # Analisar a imagem e criar a história inicial
    result = generator.analyze_image(image_path)
    
    if result:
        print("\n=== ANÁLISE DA IMAGEM ===")
        print(result['analysis'])
        
        print("\n=== INÍCIO DA HISTÓRIA ===")
        print(result['narrative'])
        
        # Adicionar ao contexto
        generator.story_context.append(result['narrative'])
        
        # Loop interativo principal
        current_scene = result['narrative']
        
        while True:
            print("\n🎮 Gerando escolhas...")
            choices = generator.generate_choices(current_scene)
            
            print("\n=== SUAS OPÇÕES ===")
            for i, (key, value) in enumerate(choices.items(), 1):
                action = value['action'] if isinstance(value, dict) else value
                hint = value.get('hint', '') if isinstance(value, dict) else ''
                print(f"{i}. {action}")
                if hint:
                    print(f"   💡 {hint}")
            
            # Gerar sugestões de áudio para a cena
            print("\n🔊 Parâmetros de áudio sugeridos:")
            audio_params = enhancer.generate_scene_audio_params(current_scene)
            print(audio_params)
            
            # Escolha do usuário
            choice_num = input("\nEscolha (1-3) ou 'q' para sair: ").strip()
            
            if choice_num.lower() == 'q':
                break
            
            try:
                choice_idx = int(choice_num) - 1
                choice_key = list(choices.keys())[choice_idx]
                chosen_action = choices[choice_key]
                
                if isinstance(chosen_action, dict):
                    action_text = chosen_action['action']
                else:
                    action_text = chosen_action
                
                print(f"\n✨ Você escolheu: {action_text}")
                print("\n📖 Continuando a história...")
                
                # Continuar a narrativa
                current_scene = generator.continue_story(action_text, current_scene)
                print(f"\n{current_scene}")
                
            except (ValueError, IndexError):
                print("Escolha inválida!")
    
    print("\n=== FIM DA DEMONSTRAÇÃO ===")

if __name__ == "__main__":
    main()
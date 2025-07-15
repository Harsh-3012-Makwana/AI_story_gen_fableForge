# # from flask import Flask, render_template, request, jsonify
# # import requests
# # import json
# # import os
# # from flask_cors import CORS
# # from openai import OpenAI
# # from dotenv import load_dotenv

# # load_dotenv()

# # app = Flask(__name__)
# # CORS(app)

# # # Hugging Face API configuration
# # # HF_API_URL = "https://api-inference.huggingface.co/models/gpt2"
# # API_URL="https://router.huggingface.co/together/v1"
# # #API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
# # #HF_API_TOKEN = "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"  # Get free token from huggingface.co

# # headers = {
# #     "Authorization": f"Bearer {os.environ.get('HF_API_TOKEN', '')}",
# # }



# # # Alternative free API - OpenAI-compatible endpoint
# # # You can also use other free APIs like:
# # # - Replicate (replicate.com)
# # # - Together AI (together.ai)
# # # - Cohere (cohere.ai)

# # @app.route('/generate_story', methods=['POST'])
# # def generate_story_with_hf(prompt, max_length=500):
# #     """Generate story using Hugging Face API"""
# #     local_hf_token = os.environ.get('HF_API_TOKEN')

# #     if not local_hf_token:
# #         print("API Error: HF_API_TOKEN not found in environment for generate_story_with_hf.")
# #         return "Sorry, the AI service is not configured correctly."

# #     headers = {
# #         "Authorization": f"Bearer {local_hf_token}",
# #         "Content-Type": "application/json"
# #     }
    
# #     # Enhanced prompt for better storytelling
# #     story_prompt = f"Write a creative and engaging story based on this prompt: {prompt}\n\nStory:"
    
# #     payload = {
# #         "inputs": story_prompt,
# #         "parameters": {
# #             "max_length": max_length,
# #             "temperature": 0.8,
# #             "top_p": 0.9,
# #             "do_sample": True,
# #             "return_full_text": False
# #         }
# #     }
    
# #     try:
# #         response = requests.post(API_URL, headers=headers, json=payload)
# #         response.raise_for_status()

# #         result = response.json()
# #         if isinstance(result, list) and len(result) > 0:
# #             return result[0].get('generated_text', 'Sorry, I couldn\'t generate a story right now.')
# #         else:
# #             return "Sorry, I couldn't generate a story right now."
            
# #     except requests.exceptions.RequestException as e:
# #         print(f"API Error: {e}")
# #         return "Sorry, there was an error generating your story. Please try again."

# # def generate_story_fallback(prompt):
# #     """Fallback story generation if API fails"""
# #     templates = [
# #         f"Once upon a time, in a world where {prompt}, there lived a young adventurer named Alex. Alex discovered something extraordinary that would change everything...",
# #         f"In the bustling city of tomorrow, where {prompt}, a mysterious event unfolded. Sarah, a brilliant scientist, found herself at the center of an incredible discovery...",
# #         f"Deep in the enchanted forest, where {prompt}, an ancient secret was about to be revealed. The wise old owl hooted warnings, but brave Maya pressed forward..."
# #     ]
    
# #     import random
# #     return random.choice(templates) + " [This is a demo story - please configure your AI API for full functionality]"

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/generate_story', methods=['POST'])
# # def generate_story():
# #     try:
# #         data = request.get_json()
# #         prompt = data.get('prompt', '').strip()
        
# #         if not prompt:
# #             return jsonify({'error': 'Please provide a story prompt'}), 400
        
# #         hf_token_from_env = os.environ.get('HF_API_TOKEN')

# #         print(f"HF_API_TOKEN from environment: {hf_token_from_env}")
# #         print(f"DEBUG: HF_API_TOKEN from environment: '{hf_token_from_env}'")
# #         print(f"DEBUG: Is token None? {hf_token_from_env is None}")
# #         print(f"DEBUG: Is token the placeholder? {hf_token_from_env == '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'}")
# #         print(f"DEBUG: Condition result (hf_token_from_env and hf_token_from_env != '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'): {hf_token_from_env and hf_token_from_env != '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'}")
        
        
# #         # Generate story using AI API
# #         if hf_token_from_env :
# #                           # and hf_token_from_env != "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":
# #             story = generate_story_with_hf(prompt)
# #             "model": "deepseek-ai/DeepSeek-R1"
# #         else:
# #             # Use fallback if no API token configured
# #             story = generate_story_fallback(prompt)
        
# #         return jsonify({
# #             'story': story,
# #             'prompt': prompt
# #         })
        
# #     except Exception as e:
# #         print(f"Error: {e}")
# #         return jsonify({'error': 'An error occurred while generating the story'}), 500

# # if __name__ == '__main__':
# #     app.run(debug=True)







# from flask import Flask, render_template, request, jsonify
# import requests
# import json
# import os
# from flask_cors import CORS
# from dotenv import load_dotenv

# load_dotenv()

# app = Flask(__name__)
# CORS(app)

# # Together AI API configuration
# TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"
# # Alternative: Use direct router endpoint
# # TOGETHER_API_URL = "https://router.huggingface.co/together/v1/chat/completions"

# def generate_story_with_together(prompt, max_length=500):
#     """Generate story using Together AI API (via HF router)"""
#     # Note: For Together AI via HF router, you need a Together AI token, not HF token
#     together_token = os.environ.get('TOGETHER_API_TOKEN') or os.environ.get('HF_API_TOKEN')
    
#     if not together_token:
#         print("API Error: TOGETHER_API_TOKEN not found in environment")
#         return None

#     headers = {
#         "Authorization": f"Bearer {together_token}",
#         "Content-Type": "application/json"
#     }
    
#     # Together AI uses OpenAI-compatible format
#     payload = {
#         "model": "meta-llama/Llama-2-7b-chat-hf",  # or "deepseek-ai/DeepSeek-R1"
#         "messages": [
#             {
#                 "role": "system",
#                 "content": "You are a creative storyteller. Write engaging, well-structured stories."
#             },
#             {
#                 "role": "user", 
#                 "content": f"Write a creative and engaging story based on this prompt: {prompt}. Make it around 300-500 words."
#             }
#         ],
#         "max_tokens": max_length,
#         "temperature": 0.8,
#         "top_p": 0.9
#     }
    
#     try:
#         print(f"Making request to Together AI: {TOGETHER_API_URL}")
#         print(f"Using token: {together_token[:10]}...")
#         print(f"Using model: {payload['model']}")
        
#         response = requests.post(TOGETHER_API_URL, headers=headers, json=payload, timeout=30)
#         print(f"Response status: {response.status_code}")
        
#         if response.status_code == 200:
#             result = response.json()
#             print(f"API Response received successfully")
            
#             if 'choices' in result and len(result['choices']) > 0:
#                 story = result['choices'][0]['message']['content']
#                 return story.strip()
#             else:
#                 print("No choices in response")
#                 return None
#         else:
#             print(f"API Error: {response.status_code}")
#             print(f"Response: {response.text}")
#             return None
            
#     except requests.exceptions.RequestException as e:
#         print(f"Request Error: {e}")
#         return None
#     except Exception as e:
#         print(f"Unexpected error: {e}")
#         return None

# def generate_story_with_hf_standard(prompt, max_length=500):
#     """Generate story using standard Hugging Face API as fallback"""
#     hf_token = os.environ.get('HF_API_TOKEN')
    
#     if not hf_token:
#         return None
    
#     # Try simpler models that work with free HF tokens
#     models = [
#         "https://api-inference.huggingface.co/models/gpt2",
#         "https://api-inference.huggingface.co/models/distilgpt2",
#         "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
#     ]
    
#     headers = {
#         "Authorization": f"Bearer {hf_token}",
#         "Content-Type": "application/json"
#     }
    
#     story_prompt = f"Write a creative story: {prompt}\n\nStory:"
    
#     for model_url in models:
#         print(f"Trying HF model: {model_url}")
        
#         payload = {
#             "inputs": story_prompt,
#             "parameters": {
#                 "max_length": max_length,
#                 "temperature": 0.8,
#                 "do_sample": True,
#                 "return_full_text": False
#             }
#         }
        
#         try:
#             response = requests.post(model_url, headers=headers, json=payload, timeout=30)
            
#             if response.status_code == 200:
#                 result = response.json()
                
#                 if isinstance(result, list) and len(result) > 0:
#                     generated_text = result[0].get('generated_text', '')
#                     if generated_text and len(generated_text.strip()) > 10:
#                         # Clean up the text
#                         if story_prompt in generated_text:
#                             generated_text = generated_text.replace(story_prompt, '').strip()
#                         return generated_text
                        
#             elif response.status_code == 503:
#                 print(f"Model loading, trying next...")
#                 continue
#             else:
#                 print(f"Error {response.status_code}: {response.text}")
#                 continue
                
#         except Exception as e:
#             print(f"Error with {model_url}: {e}")
#             continue
    
#     return None

# def generate_story_fallback(prompt):
#     """Fallback story generation if API fails"""
#     templates = [
#         f"Once upon a time, in a world where {prompt}, there lived a young adventurer named Alex. Alex discovered something extraordinary that would change everything. The journey began when Alex noticed a strange glowing object in the distance. As they approached, the mystery deepened, and Alex realized that this discovery would not only change their life but the fate of the entire world.",
#         f"In the bustling city of tomorrow, where {prompt}, a mysterious event unfolded. Sarah, a brilliant scientist, found herself at the center of an incredible discovery. The laboratory was quiet that evening when Sarah made the breakthrough that would revolutionize everything. Little did she know that her discovery would attract the attention of forces beyond her imagination.",
#         f"Deep in the enchanted forest, where {prompt}, an ancient secret was about to be revealed. The wise old owl hooted warnings, but brave Maya pressed forward through the mystical woods. Each step brought new wonders and dangers, as the forest seemed to whisper secrets of ages past. Maya's determination would soon uncover a truth that had been hidden for centuries."
#     ]
    
#     import random
#     return random.choice(templates) + "\n\n[This is a demo story - please configure your AI API for full functionality]"

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/generate_story', methods=['POST'])
# def generate_story():
#     try:
#         data = request.get_json()
#         prompt = data.get('prompt', '').strip()
        
#         if not prompt:
#             return jsonify({'error': 'Please provide a story prompt'}), 400
        
#         story = None
#         source = 'fallback'
        
#         # Try Together AI first (what you were originally trying to use)
#         together_token = os.environ.get('TOGETHER_API_TOKEN') or os.environ.get('HF_API_TOKEN')
#         if together_token:
#             print("Trying Together AI...")
#             story = generate_story_with_together(prompt)
#             if story:
#                 source = 'together_ai'
        
#         # If Together AI failed, try standard HF API
#         if not story:
#             print("Trying standard Hugging Face API...")
#             story = generate_story_with_hf_standard(prompt)
#             if story:
#                 source = 'huggingface'
        
#         # Use fallback if all APIs failed
#         if not story:
#             print("All APIs failed, using fallback")
#             story = generate_story_fallback(prompt)
        
#         return jsonify({
#             'story': story,
#             'prompt': prompt,
#             'source': source
#         })
        
#     except Exception as e:
#         print(f"Error in generate_story: {e}")
#         return jsonify({'error': 'An error occurred while generating the story'}), 500

# if __name__ == '__main__':
#     app.run(debug=True)







from flask import Flask, render_template, request, jsonify
import requests
import json
import os
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Together AI API configuration
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"
# Alternative: Use direct router endpoint
# TOGETHER_API_URL = "https://router.huggingface.co/together/v1/chat/completions"

def generate_story_with_together(prompt, max_length=500):
    """Generate story using Together AI API (via HF router)"""
    # Note: For Together AI via HF router, you need a Together AI token, not HF token
    together_token = os.environ.get('TOGETHER_API_TOKEN') or os.environ.get('HF_API_TOKEN')
    
    if not together_token:
        print("API Error: TOGETHER_API_TOKEN not found in environment")
        return None

    headers = {
        "Authorization": f"Bearer {together_token}",
        "Content-Type": "application/json"
    }
    
    # Try different models that are available on Together AI serverless
    models_to_try = [
        "meta-llama/Llama-2-7b-chat-hf",
        "meta-llama/Llama-2-13b-chat-hf", 
        "mistralai/Mistral-7B-Instruct-v0.1",
        "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO",
        "teknium/OpenHermes-2.5-Mistral-7B",
        "togethercomputer/RedPajama-INCITE-Chat-3B-v1"
    ]
    
    for model in models_to_try:
        print(f"Trying model: {model}")
        
        payload = {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a creative storyteller. Write engaging, well-structured stories."
                },
                {
                    "role": "user", 
                    "content": f"Write a creative and engaging story based on this prompt: {prompt}. Make it around 300-500 words."
                }
            ],
            "max_tokens": max_length,
            "temperature": 0.8,
            "top_p": 0.9
        }
        
        try:
            response = requests.post(TOGETHER_API_URL, headers=headers, json=payload, timeout=30)
            print(f"Response status: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                print(f"API Response received successfully")
                
                if 'choices' in result and len(result['choices']) > 0:
                    story = result['choices'][0]['message']['content']
                    return story.strip()
                else:
                    print("No choices in response")
                    continue
            elif response.status_code == 400:
                error_response = response.json()
                if "model_not_available" in error_response.get("error", {}).get("code", ""):
                    print(f"Model {model} not available, trying next...")
                    continue
                else:
                    print(f"API Error: {response.status_code}")
                    print(f"Response: {response.text}")
                    continue
            else:
                print(f"API Error: {response.status_code}")
                print(f"Response: {response.text}")
                continue
                
        except requests.exceptions.RequestException as e:
            print(f"Request Error with {model}: {e}")
            continue
        except Exception as e:
            print(f"Unexpected error with {model}: {e}")
            continue
    
    print("All Together AI models failed")
    return None
    
    try:
        print(f"Making request to Together AI: {TOGETHER_API_URL}")
        print(f"Using token: {together_token[:10]}...")
        print(f"Using model: {payload['model']}")
        
        response = requests.post(TOGETHER_API_URL, headers=headers, json=payload, timeout=30)
        print(f"Response status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"API Response received successfully")
            
            if 'choices' in result and len(result['choices']) > 0:
                story = result['choices'][0]['message']['content']
                return story.strip()
            else:
                print("No choices in response")
                return None
        else:
            print(f"API Error: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def generate_story_with_hf_standard(prompt, max_length=500):
    """Generate story using standard Hugging Face API as fallback"""
    hf_token = os.environ.get('HF_API_TOKEN')
    
    if not hf_token:
        return None
    
    # Try simpler models that work with free HF tokens
    models = [
        "https://api-inference.huggingface.co/models/gpt2",
        "https://api-inference.huggingface.co/models/distilgpt2",
        "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
    ]
    
    headers = {
        "Authorization": f"Bearer {hf_token}",
        "Content-Type": "application/json"
    }
    
    story_prompt = f"Write a creative story: {prompt}\n\nStory:"
    
    for model_url in models:
        print(f"Trying HF model: {model_url}")
        
        payload = {
            "inputs": story_prompt,
            "parameters": {
                "max_length": max_length,
                "temperature": 0.8,
                "do_sample": True,
                "return_full_text": False
            }
        }
        
        try:
            response = requests.post(model_url, headers=headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                
                if isinstance(result, list) and len(result) > 0:
                    generated_text = result[0].get('generated_text', '')
                    if generated_text and len(generated_text.strip()) > 10:
                        # Clean up the text
                        if story_prompt in generated_text:
                            generated_text = generated_text.replace(story_prompt, '').strip()
                        return generated_text
                        
            elif response.status_code == 503:
                print(f"Model loading, trying next...")
                continue
            else:
                print(f"Error {response.status_code}: {response.text}")
                continue
                
        except Exception as e:
            print(f"Error with {model_url}: {e}")
            continue
    
    return None

def generate_story_fallback(prompt):
    """Fallback story generation if API fails"""
    templates = [
        f"Once upon a time, in a world where {prompt}, there lived a young adventurer named Alex. Alex discovered something extraordinary that would change everything. The journey began when Alex noticed a strange glowing object in the distance. As they approached, the mystery deepened, and Alex realized that this discovery would not only change their life but the fate of the entire world.",
        f"In the bustling city of tomorrow, where {prompt}, a mysterious event unfolded. Sarah, a brilliant scientist, found herself at the center of an incredible discovery. The laboratory was quiet that evening when Sarah made the breakthrough that would revolutionize everything. Little did she know that her discovery would attract the attention of forces beyond her imagination.",
        f"Deep in the enchanted forest, where {prompt}, an ancient secret was about to be revealed. The wise old owl hooted warnings, but brave Maya pressed forward through the mystical woods. Each step brought new wonders and dangers, as the forest seemed to whisper secrets of ages past. Maya's determination would soon uncover a truth that had been hidden for centuries."
    ]
    
    import random
    return random.choice(templates) + "\n\n[This is a demo story - please configure your AI API for full functionality]"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_story', methods=['POST'])
def generate_story():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '').strip()
        
        if not prompt:
            return jsonify({'error': 'Please provide a story prompt'}), 400
        
        story = None
        source = 'fallback'
        
        # Try Together AI first (what you were originally trying to use)
        together_token = os.environ.get('TOGETHER_API_TOKEN') or os.environ.get('HF_API_TOKEN')
        if together_token:
            print("Trying Together AI...")
            story = generate_story_with_together(prompt)
            if story:
                source = 'together_ai'
        
        # If Together AI failed, try standard HF API
        if not story:
            print("Trying standard Hugging Face API...")
            story = generate_story_with_hf_standard(prompt)
            if story:
                source = 'huggingface'
        
        # Use fallback if all APIs failed
        if not story:
            print("All APIs failed, using fallback")
            story = generate_story_fallback(prompt)
        
        return jsonify({
            'story': story,
            'prompt': prompt,
            'source': source
        })
        
    except Exception as e:
        print(f"Error in generate_story: {e}")
        return jsonify({'error': 'An error occurred while generating the story'}), 500

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=10000, debug=True)

    
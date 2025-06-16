import boto3
import json
import base64
import os
from datetime import datetime
import time

class NovaCanvasImageGenerator:
    def __init__(self, region_name='us-east-1'):
        """Initialize the Nova Canvas image generator"""
        self.bedrock_runtime = boto3.client(
            service_name='bedrock-runtime',
            region_name=region_name
        )
        self.model_id = 'amazon.nova-canvas-v1:0'
        
        # Create output directory if it doesn't exist
        self.output_dir = 'images'
        os.makedirs(self.output_dir, exist_ok=True)
        
    def generate_image(self, prompt, filename, width=1024, height=1024, cfg_scale=8.0, seed=None):
        """
        Generate a single image using Amazon Nova Canvas
        
        Args:
            prompt (str): The text prompt for image generation
            filename (str): Output filename (without extension)
            width (int): Image width in pixels
            height (int): Image height in pixels
            cfg_scale (float): Classifier-free guidance scale (1.1 to 10.0)
            seed (int): Random seed for reproducibility
        """
        try:
            # Prepare the request body
            request_body = {
                "taskType": "TEXT_IMAGE",
                "textToImageParams": {
                    "text": prompt,
                },
                "imageGenerationConfig": {
                    "numberOfImages": 1,
                    "quality": "premium",
                    "width": width,
                    "height": height,
                    "cfgScale": cfg_scale
                }
            }
            
            # Add seed if provided
            if seed is not None:
                request_body["imageGenerationConfig"]["seed"] = seed
            
            print(f"Generating image: {filename}")
            print(f"Prompt: {prompt[:100]}...")
            
            # Call Nova Canvas
            response = self.bedrock_runtime.invoke_model(
                modelId=self.model_id,
                body=json.dumps(request_body),
                contentType='application/json'
            )
            
            # Parse response
            response_body = json.loads(response['body'].read())
            
            if 'images' in response_body and len(response_body['images']) > 0:
                # Decode base64 image
                image_data = base64.b64decode(response_body['images'][0])
                
                # Save image
                output_path = os.path.join(self.output_dir, f"{filename}.png")
                with open(output_path, 'wb') as f:
                    f.write(image_data)
                
                print(f"✅ Image saved: {output_path}")
                return output_path
            else:
                print(f"❌ No image generated for {filename}")
                return None
                
        except Exception as e:
            print(f"❌ Error generating {filename}: {str(e)}")
            return None
    
    def generate_workshop_images(self, delay_seconds=2):
        """Generate all workshop shirt images"""
        
        # Define all prompts for the workshop
        prompts = [
            {
                "filename": "01_basic_white_tshirt",
                "prompt": "A clean white cotton t-shirt on a plain white background, front view, no wrinkles, studio lighting, product photography style, minimalist, high resolution",
                "description": "Basic solid color t-shirt"
            },
            {
                "filename": "02_striped_longsleeve",
                "prompt": "A navy blue and white horizontal striped long-sleeve shirt, crew neck, regular fit, laid flat on white background, professional product photo, even lighting",
                "description": "Striped long-sleeve shirt"
            },
            {
                "filename": "03_checkered_buttonup",
                "prompt": "A red and black checkered flannel button-up shirt, classic collar, long sleeves, regular fit, hanging on white background, studio photography",
                "description": "Checkered button-up shirt"
            },
            {
                "filename": "04_oversized_hoodie",
                "prompt": "An oversized gray hoodie sweatshirt with hood up, loose fit, kangaroo pocket, long sleeves, on plain background, casual streetwear style",
                "description": "Oversized hoodie"
            },
            {
                "filename": "05_floral_blouse",
                "prompt": "A light pink blouse with small white floral pattern, V-neck, short sleeves, fitted silhouette, on white background, feminine style, soft lighting",
                "description": "Floral print blouse"
            },
            {
                "filename": "06_vintage_band_tshirt",
                "prompt": "A black vintage-style band t-shirt with distressed graphic print, crew neck, short sleeves, slightly faded, relaxed fit, on neutral background",
                "description": "Vintage band t-shirt"
            },
            {
                "filename": "07_formal_dress_shirt",
                "prompt": "A crisp white formal dress shirt, French cuffs, spread collar, long sleeves, slim fit, pressed and neat, professional product photography",
                "description": "Formal dress shirt"
            },
            {
                "filename": "08_crop_top",
                "prompt": "A bright yellow crop top, sleeveless, scoop neckline, fitted style, modern casual wear, on clean white background, good lighting",
                "description": "Crop top"
            },
            {
                "filename": "09_turtleneck_sweater",
                "prompt": "A burgundy turtleneck sweater, long sleeves, fitted silhouette, ribbed texture, fall/winter style, on neutral background, cozy aesthetic",
                "description": "Turtleneck sweater"
            },
            {
                "filename": "10_tiedye_tshirt",
                "prompt": "A tie-dye t-shirt with rainbow spiral pattern, crew neck, short sleeves, regular fit, vibrant colors, casual hippie style, bright lighting",
                "description": "Tie-dye t-shirt"
            }
        ]
        
        print(f"🚀 Starting generation of {len(prompts)} workshop images...")
        print(f"📁 Output directory: {self.output_dir}")
        print("=" * 60)
        
        successful_generations = 0
        failed_generations = 0
        
        for i, prompt_data in enumerate(prompts, 1):
            print(f"\n[{i}/{len(prompts)}] {prompt_data['description']}")
            
            result = self.generate_image(
                prompt=prompt_data['prompt'],
                filename=prompt_data['filename'],
                seed=42  # Fixed seed for reproducibility
            )
            
            if result:
                successful_generations += 1
            else:
                failed_generations += 1
            
            # Add delay between requests to avoid rate limiting
            if i < len(prompts):
                print(f"⏳ Waiting {delay_seconds} seconds...")
                time.sleep(delay_seconds)
        
        print("\n" + "=" * 60)
        print(f"🎉 Generation complete!")
        print(f"✅ Successful: {successful_generations}")
        print(f"❌ Failed: {failed_generations}")
        print(f"📁 Images saved in: {self.output_dir}/")
        
        return successful_generations, failed_generations
    
    def generate_single_test_image(self):
        """Generate a single test image to verify setup"""
        print("🧪 Generating test image...")
        
        test_prompt = "A simple red t-shirt on white background, product photography"
        result = self.generate_image(
            prompt=test_prompt,
            filename="test_shirt",
            seed=123
        )
        
        if result:
            print("✅ Test successful! Nova Canvas is working correctly.")
            return True
        else:
            print("❌ Test failed. Please check your AWS credentials and permissions.")
            return False

def main():
    """Main function to run the image generation"""
    
    print("Amazon Nova Canvas Workshop Image Generator")
    print("=" * 50)
    
    # Initialize generator
    try:
        generator = NovaCanvasImageGenerator()
        print("✅ Nova Canvas client initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize Nova Canvas client: {e}")
        print("Please check your AWS credentials and region settings.")
        return
    
    # Ask user what they want to do
    print("\nWhat would you like to do?")
    print("1. Generate test image")
    print("2. Generate all workshop images")
    print("3. Both (test first, then all images)")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        generator.generate_single_test_image()
    
    elif choice == "2":
        generator.generate_workshop_images()
    
    elif choice == "3":
        if generator.generate_single_test_image():
            print("\n" + "=" * 50)
            input("Press Enter to continue with full generation...")
            generator.generate_workshop_images()
    
    else:
        print("Invalid choice. Please run the script again.")

if __name__ == "__main__":
    main()
import os
import re
import shutil

# Paths
posts_dir = r"C:\Users\Lex-Usamn\OneDrive\Documentos\BlogLex\worldoflex\content\posts\Posts"
attachments_dir = r"C:\Users\Lex-Usamn\OneDrive\Documentos\Blog\Posts\attachments"
static_images_dir = r"C:\Users\Lex-Usamn\OneDrive\Documentos\BlogLex\worldoflex\static\images"

# Verificar se os diretórios existem
print(f"Posts directory exists: {os.path.exists(posts_dir)}")
print(f"Attachments directory exists: {os.path.exists(attachments_dir)}")
print(f"Static images directory exists: {os.path.exists(static_images_dir)}")

for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        print(f"\nProcessing file: {filename}")
        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Encontrar imagens
        images = re.findall(r'\[\[([^]]*\.png)\]\]', content)
        print(f"Found {len(images)} images in {filename}")
        
        for image in images:
            print(f"Processing image: {image}")
            markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
            content = content.replace(f"[[{image}]]", markdown_image)
            
            # Copiar imagem
            image_source = os.path.join(attachments_dir, image)
            print(f"Looking for image at: {image_source}")
            print(f"Image exists: {os.path.exists(image_source)}")
            
            if os.path.exists(image_source):
                try:
                    shutil.copy(image_source, static_images_dir)
                    print(f"Successfully copied: {image}")
                except Exception as e:
                    print(f"Error copying {image}: {str(e)}")

        # Atualizar arquivo
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("\nProcessamento concluído!")
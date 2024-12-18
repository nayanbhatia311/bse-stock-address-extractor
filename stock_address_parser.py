import pytesseract
from PIL import Image
import ollama
import re
import os
import json

def extract_text_with_ocr(image_path):
    image = Image.open(image_path)
    ocr_result = pytesseract.image_to_string(image)
    return ocr_result

def process_text_with_llama(ocr_text):
    system_prompt = "You are an assistant that extracts structured information from unstructured text."
    user_input = (
        f"Extract the company name, full address, and the state from the following text:\n"
        f"{ocr_text}\n\n"
        f"Provide the response in this format:\n"
        f"Company Name: <company_name>\n"
        f"Address: <address>\n"
        f"State: <state>"
    )

    response = ollama.chat(model='llama3.1', messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ])

    llama_output = response['message']['content']
    print("LLaMA Output:\n", llama_output)

    company_name_match = re.search(r'Company Name:\s*(.*)', llama_output)
    address_match = re.search(r'Address:\s*(.*)', llama_output)
    state_match = re.search(r'State:\s*(.*)', llama_output)

    return {
        "Company Name": company_name_match.group(1).strip() if company_name_match else "Not found",
        "Address": address_match.group(1).strip() if address_match else "Not found",
        "State": state_match.group(1).strip() if state_match else "Not found"
    }

def process_images_in_folder(folder_path, output_json_file):
    results = []

    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            image_path = os.path.join(folder_path, file_name)
            print(f"\nProcessing image: {file_name}")
            ocr_text = extract_text_with_ocr(image_path)
            print("OCR Text:\n", ocr_text)
            extracted_info = process_text_with_llama(ocr_text)

            results.append({
                "Image": file_name,
                **extracted_info
            })

    with open(output_json_file, 'w') as json_file:
        json.dump(results, json_file, indent=4)

    print(f"\nResults saved to: {output_json_file}")

def main():
    folder_path = "SearchResults"  # Folder generated by applescript 
    output_json_file = "output_results.json" 
    
    # Process images and save results
    process_images_in_folder(folder_path, output_json_file)

if __name__ == "__main__":
    main()


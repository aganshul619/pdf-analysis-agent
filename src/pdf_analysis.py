import google.generativeai as genai
import os

# Configure the API key (replace with your API key or use environment variable)
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key
genai.configure(api_key=API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')


def analyze_pdf(pdf_path, prompt):
    try:
        # Check if the PDF file exists
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found at: {pdf_path}")

        # Upload the PDF file
        print(f"Uploading PDF: {pdf_path}")
        sample_file = genai.upload_file(path=pdf_path, display_name="Input PDF")
        print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")

        # Generate content using the uploaded PDF and the provided prompt
        response = model.generate_content([sample_file, prompt])

        # Return the generated text
        return response.text

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def main():
    # Path to the PDF file (modify as needed)
    pdf_path = "sample.pdf"  # Replace with your PDF file path

    # Define the prompt for analysis (modify as needed)
    prompt = "Please summarize the content of this PDF document in 100 words or less."

    # Analyze the PDF
    result = analyze_pdf(pdf_path, prompt)

    # Print the result
    if result:
        print("\nAnalysis Result:")
        print("-" * 50)
        print(result)
    else:
        print("Failed to analyze the PDF.")


if __name__ == "__main__":
    main()
from setuptools import setup, find_packages

setup(
    name="pdf-text-extractor",
    version="0.1.0",
    packages=find_packages(
        include=["pdf_extractor", "pdf_extractor.*"]
    ),  # Explicitly include packages
    install_requires=[
        "pdf2image",
        "Pillow",
        "python-dotenv",
        "click",
        "google-generativeai",
        "openai",
        "cryptography",
    ],
    entry_points={
        "console_scripts": [
            "extract-pdf=pdf_extractor.cli:main",
        ],
    },
    python_requires=">=3.7",
)

# CSV Phone Number Cleaner 🧹🐍

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Last Commit](https://img.shields.io/github/last-commit/Bartszula/csv-data-cleaner)

A Python script for automatically cleaning and formatting phone numbers in CSV/Excel files. Removes spaces, hyphens, and special characters while preserving international number formats.

<p align="center">
  <img src="https://raw.githubusercontent.com/Bartszula/csv-data-cleaner/main/examples/screenshot.png" width="600" alt="Demo Screenshot">
</p>

## ✨ Key Features
- Cleans phone numbers by removing:
  - Spaces (` `)
  - Hyphens (`-`)
  - Parentheses `()`
  - Other special characters
- Supports UTF-8 encoding (handles international characters)
- Lightweight and dependency-free (pure Python)
- Easy integration with existing data pipelines

## 🛠 Installation
1. Clone the repository:
```bash
git clone https://github.com/Bartszula/csv-data-cleaner.git

Navigate to project directory:
cd csv-data-cleaner

🚀 Quick Start
Process a CSV file:
python clean_phones.py input.csv

This will generate a cleaned output.csv file.

📊 Example
Input (input.csv):
Name,Phone Number
John,123-456-789
Anna, (555) 123 456
Piotr,+48 789-654-321

Output (output.csv):
Name,Phone Number
John,123456789
Anna,555123456
Piotr,+48789654321

🏗 Project Structure
csv-data-cleaner/
├── clean_phones.py      # Main script
├── LICENSE              # MIT License
├── README.md            # This file
├── requirements.txt     # Dependencies
└── examples/            # Sample files
    ├── input.csv        # Sample input
    └── output.csv       # Sample output


We welcome contributions! Here's how:

Report bugs/request features via Issues

Fork the repository and submit Pull Requests

Star the project ⭐ to show your support

📜 License
MIT License - See LICENSE for details.
Free for commercial and personal use.

Custom implementations and enterprise support:
✉️ Bartszula@gmail.com
🔗 LinkedIn Profile https://www.linkedin.com/in/bartlomiej-szu%C5%82a-a53b0423a/

#!/bin/bash
# Setup script for Security Benchmark Tool

set -e

echo "========================================"
echo "Security Benchmark Tool - Setup"
echo "========================================"
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version || { echo "Python 3 not found. Please install Python 3.8 or higher."; exit 1; }

# Create virtual environment
echo ""
echo "Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created."
else
    echo "Virtual environment already exists."
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo ""
echo "Installing required packages..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo ""
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit .env and add your API keys!"
fi

echo ""
echo "========================================"
echo "Setup complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your API keys"
echo "2. Activate the virtual environment: source venv/bin/activate"
echo "3. Run the evaluation script: python eval2.py -h"
echo ""
echo "Example usage:"
echo "  python eval2.py -d utils/seceval_dataset/questions.json -e seceval -B openai -m gpt-4 -s 10"
echo ""

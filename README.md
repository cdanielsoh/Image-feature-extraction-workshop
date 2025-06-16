# Image Feature Extraction Workshop

A hands-on workshop demonstrating prompt engineering techniques for extracting product attributes from clothing images using AWS Bedrock and Amazon Nova Canvas.

## Overview

This workshop teaches you how to progressively improve prompts for extracting structured product information from clothing images, moving from basic unstructured prompts to sophisticated JSON-formatted outputs.

## Learning Objectives

- **Understand limitations** of basic prompts without constraints
- **Improve consistency** through specific attribute targeting
- **Ensure data quality** with constraint-based standardization
- **Achieve structured output** using JSON formatting for business applications

## Project Structure

```
├── workshop.ipynb          # Main workshop notebook with step-by-step exercises
├── image_generator.py      # Amazon Nova Canvas image generation utility
├── images/                 # Sample clothing product images (10 items)
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Prerequisites

- AWS account with Bedrock access
- Python 3.7+
- Jupyter Notebook environment

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure AWS credentials:**
   ```bash
   aws configure
   ```

3. **Launch the workshop:**
   ```bash
   jupyter notebook workshop.ipynb
   ```

## Workshop Flow

1. **Basic Prompt** - Understand unstructured output limitations
2. **Targeted Attributes** - Extract specific product features
3. **Constraint-Based** - Apply keyword restrictions for consistency
4. **Structured JSON** - Generate standardized, business-ready data

## Sample Images

The workshop includes 10 diverse clothing items:
- Basic white t-shirt
- Striped long sleeve
- Checkered button-up
- Oversized hoodie
- Floral blouse
- Vintage band t-shirt
- Formal dress shirt
- Crop top
- Turtleneck sweater
- Tie-dye t-shirt

## Expected Duration

**30 minutes** - Perfect for a focused learning session

## Key Technologies

- **AWS Bedrock** - Foundation model access
- **Amazon Nova Canvas** - AI image generation
- **Python/Jupyter** - Interactive development environment

---

*"Effective prompt engineering starts with clear objectives and systematic approaches."*

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# Read requirements from requirements.txt if it exists
def read_requirements():
    req_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
    if os.path.exists(req_path):
        with open(req_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return [
        "torch>=2.1.0",
        "transformers>=4.38.0",
        "accelerate>=0.28.0",
        "peft>=0.10.0",
        "bitsandbytes>=0.43.0",
        "triton>=2.1.0",
        "einops",
        "sentencepiece",
        "tqdm",
        "packaging",
        "numpy",
        "datasets>=2.16.0",  # added: commonly needed for training workflows
    ]

setup(
    name="unsloth",
    version="2024.12.0",
    author="Unsloth AI",
    author_email="info@unsloth.ai",
    description="2-5x faster, 70% less memory LLM finetuning",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/unslothai/unsloth",
    project_urls={
        "Bug Tracker": "https://github.com/unslothai/unsloth/issues",
        "Documentation": "https://docs.unsloth.ai",
        "Source Code": "https://github.com/unslothai/unsloth",
    },
    packages=find_packages(exclude=["tests*", "docs*", "examples*"]),
    python_requires=">=3.9",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov",
            "black",
            "isort",
            "flake8",
            "mypy",
        ],
        "flash-attn": [
            "flash-attn>=2.5.0",
        ],
        "colab": [
            "xformers",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords=[
        "llm",
        "finetuning",
        "lora",
        "qlora",
        "transformers",
        "machine-learning",
        "deep-learning",
        "nlp",
    ],
    include_package_data=True,
    zip_safe=False,
)

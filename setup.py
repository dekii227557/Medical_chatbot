from setuptools import find_packages, setup

setup(
    name="First_chatbot_project",
    version="0.0.0",
    author="Nguyen Minh Anh",
    author_email="minhanh2275zh@gmail.com",
    packages=find_packages(),
    install_requires=["sen", "langchain", "flask", "pydf", "pypdf", "python-dotenv", "pinecone[grpc]", "langchain-pinecone", "langchain-community", "langchain-openai", "langchain-core", "langchain-text-splitters", "langchain-experimental", "langchain-huggingface", "langchain-community", "langchain-community"]
)
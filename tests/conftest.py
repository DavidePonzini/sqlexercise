import os


# Unit tests mock generation calls and must not require a developer's .env file.
os.environ.setdefault("OPENAI_API_KEY", "test-key")

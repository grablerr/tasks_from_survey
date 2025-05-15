import re

TECH_PATTERNS = [
    r"[A-Z]+(?:[a-z]+)*\s*API",
    r"OAuth2(?:\s*токен)?",
    r"GET|POST|PUT|DELETE\s+/[\w/]+",
    r"\bмкд\b",
    r"\b[A-Za-z_]\w*\([^)]*\)",
    r"\b[a-zA-Z_]+\.[a-zA-Z_]+\b",
]

TECH_REGEX = re.compile(
    r"(" + "|".join(TECH_PATTERNS) + r")|"
    r"([a-zA-Zа-яА-ЯёЁ0-9_]+(?:-[a-zA-Z0-9]+)*)|"
    r"([^\w\s]+)",
    flags=re.UNICODE
)

def custom_tokenizer(text):
    tokens = []
    for match in TECH_REGEX.finditer(text):
        token = match.group(0)
        if token.strip():
            tokens.append(token)
    return tokens
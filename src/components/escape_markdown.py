def escape_markdown(text: str) -> str:
    # Определяем символы, которые нужно экранировать в Markdown
    replacements = {
        '_': r'\_',
        '*': r'\*',
        '[': r'\[',
        ']': r'\]',
        '(': r'\(',
        ')': r'\)',
        '~': r'\~',
        '>': r'\>',
        '#': r'\#',
        '+': r'\+',
        '-': r'\-',
        '=': r'\=',
        '|': r'\|',
        '{': r'\{',
        '}': r'\}',
        '.': r'\.',
        '!': r'\!',
    }
    
    # Последовательно заменяем каждый символ на экранированный вариант
    for char, escape_char in replacements.items():
        text = text.replace(char, escape_char)
    
    return text
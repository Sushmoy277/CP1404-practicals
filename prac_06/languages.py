"""
Estimate: 30 minutes
Actual:   32 minutes
"""

from programming_language import ProgrammingLanguage


def main():
    """Create sample languages, show string output, and list dynamic ones."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [python, ruby, visual_basic]

    dynamic_names = [language.name for language in languages if language.is_dynamic()]
    print("The dynamically typed languages are:")
    print("\n".join(dynamic_names))


main()

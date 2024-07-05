import re

def count_words(tex_file):
    with open(tex_file, 'r') as f:
        content = f.read()
        content = re.sub(r'%.*?\n', '', content)
        content = re.sub(r'\\[a-zA-Z]+\**\{[^\}]*\}', '', content)
        content = re.sub(r'\\begin\{[a-zA-Z]+\}.*?\\end\{[a-zA-Z]+\}', '', content, flags=re.DOTALL)
        words = re.findall(r'\b\w+\b', content)
        
        return len(words)

word_count = count_words("file_adjust_accordingly")
# Adjust path accordingly
print("Total word count:", word_count)

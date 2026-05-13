def merge_outputs(gpt_output, gemini_output):

    return f"""
========== CHATGPT ==========
{gpt_output}

========== GEMINI ==========
{gemini_output}
"""
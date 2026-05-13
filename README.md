## Hi there 👋

# NoGimmick

```text id="t7w17l"
███╗   ██╗ ██████╗  ██████╗ ██╗███╗   ███╗███╗   ███╗██╗ ██████╗██╗  ██╗
████╗  ██║██╔═══██╗██╔════╝ ██║████╗ ████║████╗ ████║██║██╔════╝██║ ██╔╝
██╔██╗ ██║██║   ██║██║  ███╗██║██╔████╔██║██╔████╔██║██║██║     █████╔╝
██║╚██╗██║██║   ██║██║   ██║██║██║╚██╔╝██║██║╚██╔╝██║██║██║     ██╔═██╗
██║ ╚████║╚██████╔╝╚██████╔╝██║██║ ╚═╝ ██║██║ ╚═╝ ██║██║╚██████╗██║  ██╗
╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝
```

> A terminal-native AI assistant focused on development workflows, contextual awareness, and behavior-controlled responses.

---

## Why NoGimmick?

Traditional AI assistants are optimized for:

* engagement
* conversational continuation
* generalized responses

That often results in:

* unnecessary explanations
* repetitive suggestions
* generic recommendations
* `"If you want I can..."` style outputs

NoGimmick is built to solve that problem by creating a development-focused AI environment that remains concise, operational, and context-aware.

---

## Features

```text id="jv31zf"
✓ Multi-model orchestration
✓ OpenAI + Gemini integration
✓ Context-aware prompting
✓ Terminal-first workflow
✓ Persistent environment behavior
✓ Reduced AI verbosity
✓ Developer-focused responses
✓ Clean operational output
```

#### Terminal Workflow Integration

Built specifically for:

- VS Code integrated terminal
- Linux development environments
- command-line focused workflows

---

## Tech Stack

* Python
* OpenAI API
* Gemini API
* Rich
* Typer
* YAML-based context injection

---

## Installation

### Clone Repository

```bash id="k67x1p"
git clone https://github.com/NoGimmick/NoGimmick.git
cd NoGimmick
```

---

### Create Virtual Environment

```bash id="yecqch"
python -m venv .venv
source .venv/bin/activate
```

---

### Install Dependencies

```bash id="9n8mlt"
pip install -r requirements.txt
```

---

## API Configuration

Create `.env`

```env id="pmb0um"
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
```

Generate API keys:

* [OpenAI Platform](https://platform.openai.com/api-keys?utm_source=chatgpt.com)
* [Google AI Studio](https://aistudio.google.com/app/apikey?utm_source=chatgpt.com)

---

## Run

```bash id="1rw6z7"
python app/main.py
```

---

## Example

```text id="d7x8gw"
> explain python threading briefly

========== CHATGPT ==========
...

========== GEMINI ==========
...
```

---

## Philosophy

```text id="lqmwf7"
Constrained AI > Generic AI
Focused Context > Massive Prompts
Operational Responses > Conversational Fluff
```

---

## Security

Add `.env` to `.gitignore`

```gitignore id="5vndkl"
.env
.venv/
__pycache__/
```

**NOTE:** Never expose API keys publicly.


### Current Design Philosophy

The project intentionally prioritizes:

- simplicity
- transparency
- controllable behavior
- terminal-native workflows

#### instead of:

- autonomous agents
- hidden abstractions
- excessive framework dependency
- Future Improvements

### Planned:

NoGimmick aims to evolve into a modular AI orchestration layer capable of:

- Environment-aware development assistance
- Persistent contextual memory
- Focused execution workflows
- developer-centric AI interaction

Without the conversational overhead typically associated with general-purpose AI assistants.
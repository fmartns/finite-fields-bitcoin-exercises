# Finite fields: Python exercises

Optional exercises for the blog series on finite fields and Bitcoin.

The `FieldElement` class is already set up in `field_element.py`. You implement the functions indicated in each notebook exercise. Tests live in the `.py` files.

## Setup

Clone the repository and enter the project folder:

```bash
git clone https://github.com/fmartns/finite-fields-bitcoin-exercises.git
cd finite-fields-bitcoin-exercises
python3 -m venv .venv
```

Activate the virtual environment:

```bash
# Linux or macOS
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

To open the notebook in the browser:

```bash
jupyter notebook finite_fields_exercises.ipynb
```

In VS Code or Cursor, open `finite_fields_exercises.ipynb` at the repository root with the `.venv` environment selected.

For the Portuguese blog post, use `finite_fields_exercises_pt_br.ipynb` instead.

## How to work through the exercises

1. Read the matching section of the blog post up to the **Exercise** block.
2. Open the notebook at the exercise you are on (Exercises 1–10).
3. Implement the code in the cell below the instructions.
4. Run the test cell right after.
5. Move on only when all tests pass.

If you get stuck, check `answers.py` only after trying on your own.

## License

Free to use for study.

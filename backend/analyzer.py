import ast

def analyze_code(code):

    tree = ast.parse(code)

    functions = []
    classes = []
    imports = []

    viva_questions = []
    project_tree = []
    flowchart = []

    for node in ast.walk(tree):

        # FUNCTIONS
        if isinstance(node, ast.FunctionDef):

            functions.append({
                "name": node.name,
                "parameters": len(node.args.args),
                "explanation":
                f"Function '{node.name}' takes {len(node.args.args)} parameter(s)."
            })

            viva_questions.append({
                "question":
                f"What is the purpose of {node.name}() function?",
                "answer":
                f"{node.name}() is a function defined in the program."
            })

            viva_questions.append({
                "question":
                f"How many parameters are used in {node.name}()?",
                "answer":
                str(len(node.args.args))
            })

            project_tree.append(f"Function: {node.name}()")
            flowchart.append(f"Function: {node.name}()")

        # CLASSES
        if isinstance(node, ast.ClassDef):

            classes.append({
                "name": node.name,
                "methods": [
                    n.name
                    for n in node.body
                    if isinstance(n, ast.FunctionDef)
                ]
            })

            project_tree.append(f"Class: {node.name}")
            flowchart.append(f"Class: {node.name}")

        # IMPORTS
        if isinstance(node, ast.Import):
            for n in node.names:
                imports.append(n.name)

        if isinstance(node, ast.ImportFrom):
            imports.append(node.module)

    flowchart.insert(0, "START")
    flowchart.append("END")

    # ---------------- COMPLEXITY ANALYSIS ----------------

    lines_of_code = len(
        [line for line in code.split("\n") if line.strip()]
    )

    total_functions = len(functions)
    total_classes = len(classes)
    total_imports = len(imports)

    complexity_score = total_functions + total_classes

    if complexity_score <= 2:
        complexity = "Easy"
    elif complexity_score <= 5:
        complexity = "Medium"
    else:
        complexity = "Hard"

    # ---------------- CODE QUALITY SCORE ----------------

    quality_score = 100
    suggestions = []

    if lines_of_code > 100:
        quality_score -= 20
        suggestions.append("Code is too large. Split into smaller modules.")

    if total_functions == 0:
        quality_score -= 20
        suggestions.append("Use functions for better code structure.")

    if total_imports > 10:
        quality_score -= 10
        suggestions.append("Too many imports detected.")

    if "#" not in code:
        quality_score -= 10
        suggestions.append("Add comments to improve readability.")

    if quality_score >= 90:
        suggestions.append("Excellent code structure.")
    elif quality_score >= 75:
        suggestions.append("Good code quality.")
    else:
        suggestions.append("Code quality can be improved.")

    return {
        "functions": functions,
        "classes": classes,
        "imports": imports,
        "viva_questions": viva_questions,
        "project_tree": project_tree,
        "flowchart": flowchart,

        "complexity_analysis": {
            "lines_of_code": lines_of_code,
            "functions": total_functions,
            "classes": total_classes,
            "imports": total_imports,
            "complexity": complexity
        },

        "quality_analysis": {
            "score": quality_score,
            "suggestions": suggestions
        }
    }
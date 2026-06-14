import re

def analyze_cpp(code):

    functions = []
    classes = []
    imports = []

    viva_questions = []
    project_tree = []
    flowchart = []

    # Imports
    import_pattern = r'#include\s*[<"]([^>"]+)[>"]'
    imports = re.findall(import_pattern, code)

    # Classes
    class_pattern = r'class\s+(\w+)'
    found_classes = re.findall(class_pattern, code)

    for cls in found_classes:

        classes.append({
            "name": cls,
            "methods": []
        })

        project_tree.append(f"Class: {cls}")
        flowchart.append(f"Class: {cls}")

    # Functions
    function_pattern = r'\b(?:int|float|double|char|void|string|bool)\s+(\w+)\s*\((.*?)\)'

    found_functions = re.findall(function_pattern, code)

    for func in found_functions:

        function_name = func[0]

        parameters = 0

        if func[1].strip() and func[1].strip() != "void":
            parameters = len(func[1].split(","))

        functions.append({
            "name": function_name,
            "parameters": parameters,
            "explanation":
            f"Function '{function_name}' takes {parameters} parameter(s)."
        })

        viva_questions.append({
            "question":
            f"What is the purpose of {function_name}() function?",
            "answer":
            f"{function_name}() is a function defined in the C++ program."
        })

        project_tree.append(f"Function: {function_name}()")
        flowchart.append(f"Function: {function_name}()")

    flowchart.insert(0, "START")
    flowchart.append("END")

    return {
        "functions": functions,
        "classes": classes,
        "imports": imports,
        "viva_questions": viva_questions,
        "project_tree": project_tree,
        "flowchart": flowchart
    }
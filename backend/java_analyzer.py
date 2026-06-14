import re

def analyze_java(code):

    functions = []
    classes = []
    imports = []

    viva_questions = []
    project_tree = []
    flowchart = []

    # Imports
    import_pattern = r'import\s+([\w\.\*]+);'
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
    function_pattern = r'(public|private|protected)?\s*\w+\s+(\w+)\s*\((.*?)\)'

    found_functions = re.findall(function_pattern, code)

    for func in found_functions:

        function_name = func[1]

        parameters = 0

        if func[2].strip():
            parameters = len(func[2].split(","))

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
            f"{function_name}() is a function defined in the Java program."
        })

        viva_questions.append({
            "question":
            f"How many parameters are used in {function_name}()?",
            "answer":
            str(parameters)
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
from jinja2 import Environment, FileSystemLoader
# not used when flask is available

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("main.html")
username = "Your Mom amongus"
suggestions = [
        {"task": "Sandwich", "desc":"Pls am hungri"},
        {"task": "Do nothing","desc": "Why live?"}
        ]

content = template.render(username=username, suggestions=suggestions)
print(content)


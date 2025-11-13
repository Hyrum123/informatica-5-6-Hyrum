import requests

type_operation = input("What type of operation you want to do?, we have \nSimplify, Factor, Derive, Integrate, Cosine, Sine, Tangent\n").lower()

expression = input("Awsome, now enter the expression you want to solve\n")
# equation = input("Enter your operation and your expression (seperated by a comma): ").lower().split(",")
# for element in equation:
#     print(element)

if type_operation == "derive" 

answer = requests.get("https://newton.vercel.app/api/v2/"+ type_operation + "/" + expression)
print(f"To {answer.json()["operation"]} {answer.json()["expression"]}, the answer is: {answer.json()["result"]}")
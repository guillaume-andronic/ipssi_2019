#!/usr/bin/python3

import json
fichier = open("students.json","rt")
students = json.loads(fichier.read())
print(students)
fichier.close()

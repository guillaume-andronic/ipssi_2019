#!/usr/bin/python3

with open("/mnt/c/Users/lenny/docker-compose.yml") as fd:
    for line in fd:
        chaine = "image"
        if chaine in line:
            lineb = str(line)
            linec=lineb.replace('image:','')
            lined=linec.replace('\n','')
            linee=lined.replace(' ','')
            print(linee)

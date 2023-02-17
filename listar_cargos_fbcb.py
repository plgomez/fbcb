# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import base64
"""Seleccionar INCD en variantes en el filtro de licencia por agente"""


"""tree = ET.parse('licencias_incomp_fbcb_2022_06_28.xml')
root = tree.getroot()
datos = root[2]

licencias = []
for depend in datos.iter('dep'):
    for licencia in datos.iter('licencia'):
        cargo_lic = licencia[6].text
        licencias.append(cargo_lic)

tree = ET.parse('licencias_incomp_ess_2022_06_28.xml')
root = tree.getroot()
datos = root[2]

for depend in datos.iter('dep'):
    for licencia in datos.iter('licencia'):
        cargo_lic = licencia[6].text
        licencias.append(cargo_lic)
"""
tree = ET.parse('licencias_incomp_2022_06_28.xml')
root = tree.getroot()
datos = root
licencias = []
for dep in datos.iter('dep'):
    for licencia in datos.iter('licencia'):
        cargo_lic = licencia[6].text
        licencias.append(cargo_lic)

l_tree = ET.parse('legajos_agentes_2022_06_28.xml')
l_root = l_tree.getroot()
l_datos = l_root[2]
leg_dni = {}

for legajos in l_datos.iter('legajos'):
    leg_dni[legajos[0].text] = legajos[7].text


tree = ET.parse('cargos_no_ docentes_2022_08_12.xml')
root = tree.getroot()
datos = root[2]
salida = open('cargos_no_ docentes_2022_08_12_presentismo.csv', 'w')

for cargos in datos.iter('cargos_agente'):
    en_licencia = ""
    if cargos[17].text in licencias:
        en_licencia = "Licencia por incompatibilidad"
        #print cargos[17].text

    agente = cargos[1].text
    cuil = cargos[5].text
    cargo = cargos[11].text
    agrup = cargos[34].text[:-1]
    if cargo == "AY1": cargo = "Ayudante de Cátedra"
    if cargo == "AY2": cargo = "Ayudante Alumno"
    if cargo == "JTP": cargo = "Jefe de Trabajos Prácticos"
    if cargo == "ADJ": cargo = "Profesor Adjunto"
    if cargo == "ASO": cargo = "Profesor Asociado"
    if cargo == "TIT": cargo = "Profesor Titular"
    dedicacion = cargos[11].text[-1:]
    if dedicacion == "1" : dedicacion = "Simple"
    if dedicacion == "S" : dedicacion = "Semiexclusiva"
    if dedicacion == "E" : dedicacion = "Exclusiva"
    if dedicacion == "B" : dedicacion = "Exclusiva B"
    if dedicacion == "A" : dedicacion = "Exclusiva A"
    if dedicacion == "C" : dedicacion = "Exclusiva C"
    if dedicacion == "N" : dedicacion = cargos[14].text+" Horas"
    #agente =  base64.b64encode(agente)[:10]
    caracter = cargos[9].text
    dependencia = cargos[10].text
    agrupamiento = {"MPRO": "Mantenimiento, Producción y Servicios Generales","MPR": "Mantenimiento, Producción y Servicios Generales", "ADM": "Administrativo", "AD": "Administrativo", "SGRL": "Mantenimiento, Producción y Servicios Generales", "SGR": "Mantenimiento, Producción y Servicios Generales", "TEC": "Técnico Profesional","TE": "Técnico Profesional" }
    if caracter != "BECA":
        fila = f"{agente} - DNI Nº {cuil[3:-2]} - Categoría {cargo} - Agrupamiento {agrupamiento[agrup]}\n"
        #fila = f"{agente} \t {cuil} \t {cargo} \n"
        #agente + " \t " + cuil + " \t " +  cargo + " \t " + dedicacion + " \t " + caracter + " \t" + en_licencia + " \t" + dependencia + " \n"
        salida.write(fila)    
salida.close()

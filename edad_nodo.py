# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
tree = ET.parse('legajos_agentes_2025-05-29.xml')
root = tree.getroot()
datos = root[2]

print(datos[2])

anio_actual = "2025"

edades_agentes = {}
for legajo in datos.findall('legajos'):
    nro_legajo = legajo[0].text
    anio = legajo[12].text[6:]
    edad = int(anio_actual) - int(anio)
    edades_agentes[nro_legajo] = edad

tree = ET.parse('cargos_nodocentes_2025-05-29.xml')
root = tree.getroot()
datos = root[2]


mayores_65 = open('nodos_pronto_a_jubilarse_'+anio_actual+'.csv','w')

cargos_agente = []
for cargos in datos.iter('cargos_agente'):
    leg_agente = cargos[0].text
    if leg_agente not in cargos_agente:
        cargos_agente.append(leg_agente)
        agente = cargos[1].text
        edad_agente = edades_agentes[leg_agente]
        if edad_agente >= 58:
            print(f"{agente} \t {edad_agente}")
            fila = (f"{agente} \t {edad_agente} \n")
            mayores_65.write(fila)    

mayores_65.close()

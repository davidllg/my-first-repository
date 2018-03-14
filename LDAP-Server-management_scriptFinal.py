#!/usr/bin/python3.5

#Description: Script en python. Para la gestión y administración de un servidor LDAP.
#Author: David L.
#V 1.0 BETA

# Funcionalidades #

# 1- Gestionar csv
# 2- Gestionar ldifs
# 3- Gestionar servidor ldap
#	1. Crear objeto. 
# 	2. Modificar objeto.
#	3. Eliminar objeto.
# 	4. Buscar objeto.



# Variables conf
dc1="example"
dc2="com"
privilegeUser="admin"


import shlex, subprocess

def draw():
	print("""
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,ADMINISTRACIÓN PARA CSV, LDIF y LDAP,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
´´´´´´´´´´´´´´´´´¶
´´´´´´´´´´´´´´¶´´¶´´´¶¶
´´´´´´´´´´´´´´¶´¶¶´¶¶
´´´´´´´´´¶¶¶¶´´´´´´¶¶¶¶¶¶
´´´´´´´¶¶´´´´´´´´´´´´´´´´¶¶
´´´´´¶¶´´´´´´´´¶¶´´´´´´´´´´¶¶
´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´¶¶
´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶
´´¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶´¶
´¶´´´´´´´´´´´´´´´´¶´´´´´´´´´´´´´¶
´¶´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´¶
´¶´´´´´´´´´´´´¶¶´¶´´´´´´´´´´´¶´´´¶
´¶´´´´´´´´´´¶¶¶¶¶¶´´´´´´´¶¶¶¶´´´´¶
´¶´´´´´´´´´¶¶¶¶¶¶¶´´´´´´¶¶´´¶´´´´¶
´´¶´´´´´´´´¶¶¶¶¶´¶´´´´´¶¶¶¶¶¶´´´¶
´´¶¶´´´´´´´¶´´´´´¶´´´´¶¶¶¶¶¶´´´¶¶
´´´¶¶´´´´´´¶´´´´¶´´´´¶¶¶¶´´´´´¶
´´´´¶´´´´´´¶´´´¶´´´´´¶´´´´´´´¶
´´´´¶´´´´´´¶¶¶¶´´´´´´´´´¶´´¶¶
´´´´¶¶´´´´´´´´´´´´´´´¶¶¶´´¶
´´´´´¶¶¶´´´´´´´¶¶¶¶¶´´´´´´¶
´´´´´´´´¶¶¶´´´´´¶¶´´´´´´´¶¶
´´´´´´´´´´´´¶¶´´´´´¶¶¶¶¶¶´
´´´´´´´´´´¶¶´´´´´´¶¶´¶
´´´´´´´¶¶¶¶´´´´´´´´¶´¶¶
´´´´´´´´´¶´´¶¶´´´´´¶´´´¶
´´´´¶¶¶¶¶¶´¶´´´´´´´¶´´¶´
´´¶¶´´´¶¶¶¶´¶´´´´´´¶´´´¶¶¶¶¶¶¶
´´¶¶´´´´´´¶¶¶¶´´´´´¶´¶¶´´´´´¶¶
´´¶´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´¶
´´´¶¶´´´´´´´´´¶´´´¶´´´´´´´´´´¶
´´´´¶¶¶¶¶¶¶¶¶¶¶´´´¶¶¶¶¶¶¶¶¶¶¶ ~*
""")
	
def mainMenu():
	#MAIN MENU
	print("~~~~~~~~~~ ~~~~~~~~~~ ~~~~~~~~ ~~~")
	print("~~~~~~~~~~~ MAIN MENÚ ~~~~~~~~~~~~")
	print("~ Administración de Servidor LDAP ")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("~~~ 1. Gestionar CSV ~~~~~~~~~~~~~")
	print("~~~ 2. Gestionar LDIF ~~~~~~~~~~~~")
	print("~~~ 3. Gestionar servidor LDAP ~~~")
	print("~~~ 4. Salir ~~~~~~~~~~~~~~~~~~~~~")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def modMenu():
	#subMENU LDAP MANAGEMENT
	print("~#~#~#~#~#~#~#~#~#~#~#~#~#~")
	print("~#~ 1. Crear objeto ~#~#~#~")
	print("~#~ 2. Modificar objeto ~#~")
	print("~#~ 3. Eliminar objeto ~#~#")
	print("~#~ 4. Buscar objeto ~#~#~#")
	print("~#~#~#~#~#~#~#~#~#~#~#~#~#~")

def searchBasic():
	print("1- '=' Igualdad (Todos los objetos de un tipo)")
	print("2- '<=' Valor menor o igual (Devolverá aquellos objetos que tengan un valor menor o igual en el atributo especificado)")
	print("3- '&' AND (Realizará una búsqueda de objetos cuya búsqueda sea cierta(Sólo un atributo))")

optionMainMenu=0
while optionMainMenu != 4:
	subprocess.call(shlex.split("clear"))
	draw()
	mainMenu()
	optionMainMenu = int(input("Selecciona una opción -> "))
	if(optionMainMenu == 1):
		subprocess.call(shlex.split("clear"))
		draw()
		option1 = input("Escriba el nombre del fichero para gestión de CSV: ")
		comprobaX = subprocess.getoutput('ls -la | grep '+option1+' | cut -d " " -f1 | grep x -n | cut -d ":" -f1')
		if(comprobaX == "1"):
			subprocess.call(shlex.split("./"+option1))
		else:
			print("#ERROR# ¿El archivo seleccionado tiene permisos ejecutables?")
	elif(optionMainMenu == 2):
		subprocess.call(shlex.split("clear"))
		draw()
		option1 = input("Escriba el nombre del fichero para gestión de LDIF: ")
		comprobaX = subprocess.getoutput('ls -la | grep '+option1+' | cut -d " " -f1 | grep x -n | cut -d ":" -f1')
		if(comprobaX == "1"):
			subprocess.call(shlex.split("./"+option1))
		else:
			print("#ERROR# ¿El archivo seleccionado tiene permisos ejecutables?")
	elif(optionMainMenu == 3):
		subprocess.call(shlex.split("clear"))
		draw()
		modMenu()
		option1 = int(input("Elija una opción: "))
		
		#- AÑADIR OBJETO
		if(option1 == 1):
			option2 = int(input ("""1-Insertar cambios manualmente
2-Seleccionar fichero .ldif
-> """))
			if(option2 == 1):
				cn = input("Inserte 'cn': ")
				ou = input("Inserte 'ou': ")
				gidNumber = input("inserte 'gidNumber': ")
				homeDirectory = input("Inserte 'homeDirectory': ")
				sn = input("Inserte 'sn': ")
				uid = input("Inserte 'uid': ")
				uidNumber = input("Inserte 'uidNumber': ")
				loginShell = input("Inserte 'loginShell': ")
				telephoneNumber = input("Inserte 'telephoneNumber': ")
				f = open("add-tmp.ldif", "w")
				f.write("dn: cn="+cn+",ou="+ou+",dc="+dc1+",dc="+dc2+"\n")
				f.write("objectClass: inetOrgPerson\n")
				f.write("objectClass: organizationalPerson\n")
				f.write("objectClass: person\n")
				f.write("objectClass: posixAccount\n")
				f.write("objectClass: top\n")
				f.write("cn: "+cn+"\n")
				f.write("gidNumber: "+gidNumber+"\n")
				f.write("homeDirectory: "+homeDirectory+"\n")
				f.write("sn: "+sn+"\n")
				f.write("uid: "+uid+"\n")
				f.write("uidNumber: "+uidNumber+"\n")
				f.write("loginShell: "+loginShell+"\n")
				f.write("telephonenumber: "+telephoneNumber+"\n")
				f.write("")
				f.close()
				ultimatum = input("¿Desea subir el archivo al servidor LDAP ahora mismo? [Y/n]: ")
				if(ultimatum == ""):
					subprocess.call(shlex.split("ldapadd -x -D cn="+privilegeUser+",dc="+dc1+",dc="+dc2+" -f add-tmp.ldif -W"))
					subprocess.call(shlex.split("rm -rf add-tmp.ldif"))
				elif(ultimatum == "Y"):
					fichero = input("Escriba el nombre del fichero: ")
					subprocess.call(shlex.split("ldapadd -x -D cn="+privilegeUser+",dc="+dc1+",dc="+dc2+" -f add-tmp.ldif -W"))
					subprocess.call(shlex.split("rm -rf add-tmp.ldif"))
				elif(ultimatum == "y"):
					fichero = input("Escriba el nombre del fichero: ")
					subprocess.call(shlex.split("ldapadd -x -D cn="+privilegeUser+",dc="+dc1+",dc="+dc2+" -f add-tmp.ldif -W"))
					subprocess.call(shlex.split("rm -rf add-tmp.ldif"))
				elif(ultimatum == "N"):
					print("Volviendo al menú principal...")
				elif(ultimatum == "n"):
					print("Volviendo al menú principal...")
				else:
					print("Opción inválida.")	
				subprocess.call(shlex.split("sleep 2"))
			elif(option2 == 2):
					cn = input("'cn' del Administrador: ")
					fichero = input("Fichero .ldif: ")
					subprocess.call(shlex.split("ldapadd -x -D cn="+cn+",dc="+dc1+",dc="+dc2+" -f "+fichero+" -W"))
					print("Se ha subido objeto correctamente.")
					subprocess.call(shlex.split("sleep 2"))
			else:
				print("Esa opción no está disponible, se siente.")
		#- MODIFICAR OBJETO
		elif(option1 == 2):
			option2 = int(input ("""1-Insertar cambios manualmente
2-Seleccionar fichero .ldif
-> """))
			if(option2 == 1):
				subprocess.call(shlex.split("clear"))
				draw()
				op = int(input("""Elige una operación: 
1- Añadir atributo
2- Remplazar atributo
3- Eliminar atributo
-> """))
				if(op == 1):
					cn = input("Inserte 'cn': ")
					ou = input("Inserte 'ou': ")
					add = input("Atributo a añadir: ")
					add2 = input("Valor para "+add+": ")
					f = open("modify-add.ldif", "w")
					f.write("dn: cn="+cn+",ou="+ou+",dc="+dc1+",dc="+dc2+"\n")
					f.write("changetype: modify\n")
					f.write("add: "+add+"\n")
					f.write(""+add+": "+add2+"")
					f.close()
				elif(op == 2):
					cn = input("Inserte 'cn': ")
					ou = input("Inserte 'ou': ")
					change = input("Atributo a remplazar: ")
					replace = input("Remplanzar por: ")
					f = open("modify-replace.ldif", "w")
					f.write("dn: cn="+cn+",ou="+ou+",dc="+dc1+",dc="+dc2+"\n")
					f.write("changetype: modify\n")
					f.write("replace: "+change+"\n")
					f.write(""+change+": "+replace+"\n")
					f.close()
				elif(op == 3):
					cn = input("Inserte 'cn': ")
					ou = input("Inserte 'ou': ")
					delete = input("Inserte atributo a eliminar: ")
					f = open("modify-delete.ldif", "w")
					f.write("dn: cn="+cn+",ou="+ou+",dc="+dc1+",dc="+dc2+"\n")
					f.write("changetype: modify\n")
					f.write("delete: "+delete+"")
					f.close()
				else:
					print("Opción inválida.")
				#SUBIR ARCHIVO INMEDIATAMENTE O NO.
				ultimatum = input("¿Desea subir el archivo al servidor LDAP ahora mismo? [Y/n]: ")
				if(ultimatum == ""):
					fichero = input("Escriba el nombre del fichero: ")
					subprocess.call(shlex.split("ldapmodify -x -D cn="+privilegeUser+",dc="+dc1+",dc="+dc2+" -f "+fichero+" -W"))
					subprocess.call(shlex.split("rm -rf modify*.ldif"))
				elif(ultimatum == "Y"):
					print("Ha elegido Y")
				elif(ultimatum == "y"):
					print("Ha elegido y")
				elif(ultimatum == "N"):
					print("Volviendo al menú principal...")
				elif(ultimatum == "n"):
					print("Volviendo al menú principal...")
				else:
					print("Opción inválida.")	
				subprocess.call(shlex.split("sleep 2"))
			elif(option2 == 2):
				fichero = input("Fichero .ldif con las modificaciones: ")
				subprocess.call(shlex.split("ldapmodify -x -D cn="+privilegeUser+",dc="+dc1+",dc="+dc2+" -f "+fichero+" -W"))
				print("Se ha modificado el objeto correctamente.")
				subprocess.call(shlex.split("sleep 2"))
			else:
				print("Esa opción no está disponible.")
		#- ELIMINAR OBJETO
		elif(option1 == 3):
			# Se decide si es una cuenta de usuario o una unidad organizativa.
				select = input("""Seleccione una opción:
1- Cuenta de usuario o grupo posix
2- Unidad Organizativa 
-> """)
				if(select == "1"):
					objeto = input("Ahora escriba el 'cn' del objeto que desea eliminar: ")
					ouYes = input("¿Pertenece a alguna unidad organizativa? De ser así índiquela: ")
					if(ouYes == ""):
						subprocess.call(shlex.split("ldapdelete -D cn="+privilegeUser+",dc="+dc1+",dc="+dc2+" -W -h localhost -p 389 cn="+objeto+",dc="+dc1+",dc="+dc2+""))
					else:
						subprocess.call(shlex.split("ldapdelete -D cn="+privilegeUser+",dc="+dc1+",dc="+dc2+" -W -h localhost -p 389 cn="+objeto+",ou="+ouYes+",dc="+dc1+",dc="+dc2+""))
						
				elif(select == "2"):
					ou = input("Escriba el nombre de la 'ou': ")
					subprocess.call(shlex.split("ldapdelete -D cn="+privilegeUser+",dc="+dc1+",dc="+dc2+" -W -h localhost -p 389 ou="+ou+",dc="+dc1+",dc="+dc2+""))	
				else:
					print("Esa opción no es válida.")
		#- BUSCAR OBJETO
		elif(option1 == 4):
			AoN = input("""
1-Básico
2-Avanzado (Introducir parámetros a mano)
-> """)
			if(AoN == "1"):
				searchBasic()
				optione = input("Selecciona una opción: ")
				if(optione == "1"):
					subprocess.call(shlex.split("clear"))
					draw()
					intro = 1
					while intro == 1:
						filtro = input("Ver toda las cuentas de tipo: ")
						print("-------------------------------------------------------------------")
						subprocess.call(shlex.split("ldapsearch -x -b 'dc="+dc1+",dc="+dc2+"' '"+filtro+"'"))
						intro = input("Pulse INTRO para volver al menú principal...")
						intro = 2
				elif(optione == "2"):
					subprocess.call(shlex.split("clear"))
					draw()
					intro = 1
					while intro == 1:
						filtro = input("Introduzca un atributo númerico: ")
						filtro2 = input("Introduzca un número: ")
						print("-------------------------------------------------------------------")
						subprocess.call(shlex.split("ldapsearch -x -b 'dc="+dc1+",dc="+dc2+"' '"+filtro+"<="+filtro2+"'"))
						intro = input("Pulse INTRO para volver al menú principal...")
						intro = 2
				elif(optione == "3"):
					subprocess.call(shlex.split("clear"))
					draw()
					subprocess.call(shlex.split("ldapsearch -x -b 'dc="+dc1+",dc="+dc2+"' '(&(objectClass="+filtro+"(cn=L*))'"))	
				else:
					print("Opción inválida.")
			elif(AoN == "2"):
				subprocess.call(shlex.split("clear"))
				draw()
				intro = 1
				while intro == 1:
					search = input("Inserte un filtro de busqueda: ")
					print("-------------------------------------------------------------------")
					subprocess.call(shlex.split("ldapsearch -x -b 'dc="+dc1+",dc="+dc2+"' '"+search+"'"))
					intro = input("Pulse INTRO para volver al menú principal...")
					intro = 2
					
			else:
				print("Opción inválida")
				subprocess.call(shlex.split("sleep 2"))
		else:
			print("Esa opción no está disponible.")
	elif(optionMainMenu == 4):
		subprocess.call(shlex.split("reset"))
		draw()
		print("Script finalizado.")
	else:
		draw()
		print("Esa opción no existe.")


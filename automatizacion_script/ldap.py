import os
import sys
import yaml         # Para leer el template de variables que usa el ansible
import tools

LDAP_PROJECT_START="ansible-ldap/start.yml"
LDAP_VARIABLES_ROLES="ansible-ldap/roles/general_defaults/variables_roles.yml"

def baja_usuario(username):
  """
  ldap_baja_usuario: {
    username: '',
    borrar: true,
  },
  """
  variables_roles = None
  try:
    with open(LDAP_VARIABLES_ROLES, 'r+') as stream:
      variables_roles = yaml.safe_load(stream)
      # Asigno el usuario a bajar
      variables_roles['variables_roles']['ldap_baja_usuario']['username'] = username.strip()
      variables_roles['variables_roles']['ldap_baja_usuario']['borrar'] = True
      stream.close()
    # Borro el contenido del file
    open(LDAP_VARIABLES_ROLES,'w')

    with open(LDAP_VARIABLES_ROLES, 'r+') as stream:
      # print(yaml.dump(variables_roles))
      # Guardo las variables en el archivo
      stream.write(yaml.dump(variables_roles))

  except yaml.YAMLError as exc:
    print(exc)
  except Exception as e:

    print("exit")
    print(e)

  return(tools.exec_ansible(LDAP_PROJECT_START))

def alta_usuario(username, apellido_y_nombre, delegacion, grupo_sector, habilitar=True):
  # TODO
  pass

def cambio_delegacion_usuario(username, delegacion):
  # TODO
  pass

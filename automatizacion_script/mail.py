import os
import sys
import yaml         # Para leer el template de variables que usa el ansible
import tools

MAIL_PROJECT_START="ansible-mail/start.yml"
MAIL_VARIABLES_ROLES="ansible-mail/roles/general_defaults/variables_roles.yml"

def baja_usuario(username):
  """
  baja_cuenta: {
    username: "",
    personal:  # true/false
  },
  """
  variables_roles = None
  try:
    with open(MAIL_VARIABLES_ROLES, 'r+') as stream:

      variables_roles = yaml.safe_load(stream)
      # Casilla de baja
      variables_roles['variables_roles']['baja_cuenta']['username'] = username.strip()
      variables_roles['variables_roles']['baja_cuenta']['personal'] = True
      # Baja de todas las listas
      variables_roles['variables_roles']['listas']['baja_masiva'] = True

      stream.close()

    # Borro el contenido del file
    open(MAIL_VARIABLES_ROLES,'w')
    with open(MAIL_VARIABLES_ROLES, 'r+') as stream:
      # print(yaml.dump(variables_roles))
      # Guardo las variables en el archivo
      stream.write(yaml.dump(variables_roles))

  except yaml.YAMLError as exc:
    print(exc)
  except Exception as e:

    print("exit")
    print(e)

  return(tools.exec_ansible(MAIL_PROJECT_START))

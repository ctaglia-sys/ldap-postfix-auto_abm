import os
import sys
import subprocess   # Ejecucion bash: ansible-playbook start.yml




#PROYECTOS_ANSIBLE_AUTOMATICOS = ["http://"]

def exec_ansible(project_start):

  run_ansible = subprocess.run(["ansible-playbook",project_start], 
                                universal_newlines=True, 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE)
  # print(run_ansible.returncode)
  return (run_ansible.returncode, run_ansible.stdout, run_ansible.stderr)

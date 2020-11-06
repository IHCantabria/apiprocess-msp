# DEPLOY REQUIREMENTS

🚀 Deploy requirements for IH-IT software

## App Name

    - apiprocess-msp

## App Template

    - Api (api.wsgi)
  

## System

    - Linux

## Environment

    - Dev
    - Prod

## Distribution

    - Master

## Url GIT

    - ssh://git@github.com:IHCantabria/apiprocess-msp.git

## DNS

_Production_

    - apiprocess-msp.ihcantabria.com

_Development_

    - apiprocess-msp.ihcantabria.com

## Other settings

Select only if needed:

**Python version**

`3.6`

** Others **

**Services to restart**

`apache2`

**Backup**

    - Tags
    - Snapshot
    - Clone/Backup

---

**Do you need any other configuration?**

* Ejecutar requirements.txt


* Modificar `/var/www/{{ app }}/env_{{ app }}/lib/python3.6/site-packages/msptools/config.py`:
    - valor para `filepath`: `"/dat/log/{{ app }}/apiprocess-msp.log"`



* Modificar {{ app }}/env_{{ app }}/datahub/logging.ini:

    - la ruta en la línea 34 debe ser: "/dat/{{ app }}/log/datahubclient.log"



* Permisos `0755` para directorios:
    - path: "{{ item.ruta }}"
    - owner: "{{ item.user }}"
    - group: "{{ item.grupo }}"
    - mode: "{{ item.permiso }}"
    

## Relationships

**What applications, services, or data sources is this application related to?**

`_______________________________________________________________________________`

## Credits

[IH Cantabria](https://github.com/IHCantabria)

## FAQ

- Document provided by the system administrators [David del Prado](https://ihcantabria.com/directorio-personal/tecnologo/david-del-prado-secadas/) y [Gloria Zamora](https://ihcantabria.com/directorio-personal/tecnologo/gloria-zamora/)

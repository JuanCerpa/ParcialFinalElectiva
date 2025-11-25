# Proyecto de Calidad de Software Avanzado

Este repositorio implementa un pipeline de CI/CD utilizando GitHub Actions para un proyecto en Python.

## Estrategia de CI (Parte 1)

### Diferencia entre CI y CD
* **CI (Integración Continua):** Es la práctica de integrar cambios de código frecuentemente (varias veces al día). Se verifican automáticamente mediante builds y pruebas para detectar errores lo antes posible.
* **CD (Entrega/Despliegue Continuo):** Es la extensión del CI donde, tras pasar las pruebas, el código se libera automáticamente a un repositorio (Entrega) o se despliega a producción (Despliegue).

### Herramientas Seleccionadas
* **Lenguaje:** Python (Versatilidad y herramientas claras de calidad).
* **Linter:** `flake8`. Es el estándar de la industria para verificar el estilo (PEP 8) y errores lógicos simples sin ejecutar el código.
* **Cobertura:** `pytest-cov`. Se integra nativamente con el framework de pruebas `pytest` y permite fallar el build si no se cumple el umbral.

### Umbral de Cobertura
Se ha definido un **80%**.
* *Justificación:* El 100% suele ser costoso de mantener y ofrece rendimientos decrecientes. Un 80% asegura que la lógica crítica está probada, dejando margen para código trivial (como getters/setters o configs) sin bloquear el desarrollo.

## Uso de Nektos/Act (Parte 3)

### ¿Qué es Act?
`nektos/act` es una herramienta que permite ejecutar GitHub Actions localmente. Utiliza la API de Docker para crear contenedores que simulan los runners de GitHub, permitiendo probar los workflows sin necesidad de hacer `git push`.

### Requisitos
1.  Tener **Docker** instalado y corriendo.
2.  Instalar Act (Ejemplo en Windows con Choco: `choco install act-cli` o descargando el binario).

### Ejecución Local
Para ejecutar el pipeline localmente, correr en la terminal:
```bash
act push
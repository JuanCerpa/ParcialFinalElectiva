```markdown
# Respuestas Complementarias

## Parte 4: Validación y Logs

### Identificar Fallos
1.  **Linter:** Buscar en los logs la sección "Analisis Estático". Si falla, mostrará códigos como `E501` (línea muy larga) o `F401` (import no usado) junto con el número de línea.
2.  **Pruebas:** Buscar la sección "Test y Cobertura". Si una prueba falla, aparecerá en rojo `FAILED tests/test_...`.
3.  **Cobertura:** Al final del log de pytest, aparecerá `FAIL Required test coverage of 80% not reached. Total coverage: XX%`.

### Diferencia Run Exitoso vs Fallido
* **Exitoso:** Todos los pasos tienen un check verde (✅). El proceso termina con "Job succeeded".
* **Fallido:** El paso conflictivo tiene una cruz roja (❌). El proceso se detiene inmediatamente (debido a la configuración por defecto de GitHub Actions) y retorna "Process exited with code 1".

## Parte 5: IA y Ética

### 1. Métodos de detección de código IA
* **Análisis de Estilometría:** Herramientas que analizan patrones sintácticos repetitivos y la "perplejidad" del texto. Los LLM tienden a usar estructuras muy predecibles y vocabulario estándar.
* **Marcas de agua (Watermarking):** Técnicas (como las propuestas por OpenAI o Google DeepMind) que insertan patrones estadísticos imperceptibles en la elección de tokens, que pueden ser decodificados criptográficamente para probar origen artificial.

### 2. ¿Por qué no es posible asegurar la autoría al 100%?
Los modelos de IA son probabilísticos, no deterministas. Además, un humano puede modificar manualmente el código generado ("ofuscarlo"), rompiendo los patrones estadísticos que buscan los detectores. También existen falsos positivos donde código humano muy limpio es marcado como IA.

### 3. Políticas razonables de uso
1.  **Declaración Obligatoria:** El uso de IA debe ser declarado en los comentarios del código o documentación.
2.  **Responsabilidad Humana:** El estudiante/desarrollador es responsable de cualquier bug o fallo de seguridad introducido por la IA; "la IA lo escribió mal" no es una excusa válida.
3.  **Uso como Asistente, no Reemplazo:** Permitir IA para generar boilerplate o explicar errores, pero prohibir copiar y pegar soluciones enteras sin entender la lógica subyacente.
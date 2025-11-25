# /var/www/departamentos/app.py

def application(environ, start_response):
    status = '200 OK'
    
    # 1. Tu lógica (adaptada sin inputs)
    # En lugar de pedir datos, simulamos una agenda ya llena
    agenda = {
        "Juan": "666111222",
        "Maria": "655444333",
        "Pepe": "611222333"
    }
    
    # 2. Preparamos el texto a mostrar
    # Usamos HTML básico para que se vea bien en el navegador
    contenido_html = "<h1>Agenda de Contactos (Python WSGI)</h1>"
    contenido_html += "<ul>"
    
    for nombre, telefono in agenda.items():
        contenido_html += f"<li><b>{nombre}</b>: {telefono}</li>"
        
    contenido_html += "</ul>"
    contenido_html += "<p><em>Nota: Esta agenda es de solo lectura porque corre en servidor web.</em></p>"

    # 3. Codificamos la respuesta
    output = contenido_html.encode('utf-8')

    # 4. Cabeceras
    response_headers = [('Content-type', 'text/html; charset=utf-8'),
                        ('Content-Length', str(len(output)))]
    
    start_response(status, response_headers)
    
    return [output]

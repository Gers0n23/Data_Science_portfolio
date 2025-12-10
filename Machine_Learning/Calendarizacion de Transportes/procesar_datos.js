const fs = require('fs');

// Leer el archivo de texto
const contenido = fs.readFileSync('Consolidado de Transporte.txt', 'latin1');
const lineas = contenido.split('\n');

const datos = [];
let errores = 0;

// Procesar cada línea (saltando la primera que es el encabezado)
for (let i = 1; i < lineas.length; i++) {
    const linea = lineas[i].trim();
    if (!linea) continue;

    const partes = linea.split('\t');

    if (partes.length >= 8) {
        try {
            // Limpiar el campo de importe
            let importe = partes[7].trim();
            importe = importe.replace('$', '').replace('.', '').replace(',', '.');

            // Limpiar volumen y peso
            let volumen = partes[5].trim().replace(',', '.');
            let peso = partes[6].trim().replace(',', '.');

            const registro = {
                transportista: partes[0].trim(),
                origen: partes[1].trim(),
                destino: partes[2].trim(),
                fecha: partes[3].trim(),
                periodo: partes[4].trim(),
                volumen: parseFloat(volumen),
                peso: parseFloat(peso),
                importe: parseFloat(importe)
            };

            // Validar que los números sean válidos
            if (!isNaN(registro.volumen) && !isNaN(registro.peso) && !isNaN(registro.importe)) {
                datos.push(registro);
            } else {
                errores++;
            }
        } catch (e) {
            errores++;
        }
    }
}

// Guardar el archivo JSON
fs.writeFileSync('datos_procesados.json', JSON.stringify(datos, null, 2));

console.log(`✅ Procesamiento completado`);
console.log(`   Total registros: ${datos.length}`);
console.log(`   Errores: ${errores}`);

// Mostrar estadísticas por transportista
const porTransportista = {};
datos.forEach(d => {
    porTransportista[d.transportista] = (porTransportista[d.transportista] || 0) + 1;
});

console.log('\nRegistros por transportista:');
Object.entries(porTransportista)
    .sort((a, b) => b[1] - a[1])
    .forEach(([trans, count]) => {
        console.log(`   ${trans}: ${count}`);
    });

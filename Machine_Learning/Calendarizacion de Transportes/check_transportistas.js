const fs = require('fs');

const data = JSON.parse(fs.readFileSync('datos_procesados.json', 'utf8'));
const transportistas = [...new Set(data.map(item => item.transportista))];

console.log('Transportistas encontrados:', transportistas);
console.log('Total de registros:', data.length);
console.log('\nConteo por transportista:');

const conteo = {};
data.forEach(item => {
    conteo[item.transportista] = (conteo[item.transportista] || 0) + 1;
});

Object.entries(conteo).forEach(([trans, count]) => {
    console.log(`  ${trans}: ${count} registros`);
});

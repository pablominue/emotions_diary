// Función para inicializar el gráfico de emociones
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

function initEmotionChart(labels, emotionData) {
    var ctx = document.getElementById('emotionChart').getContext('2d');

    // Definir colores específicos para cada tipo de emoción
    var emotionColors = {
        'alegria': '#f1c40f',
        'tristeza': '#3498db',
        'ira': '#e74c3c',
        'miedo': '#a147a1',
        'sorpresa': '#9b59b6',
        'confianza': '#2ecc71',
        'desagrado': '#e67e22',
        'anticipacion': '#34495e'
    };

    // Crear datasets dinámicamente basado en las emociones
    var datasets = [];

    for (var emotionType in emotionData) {
        if (emotionData.hasOwnProperty(emotionType)) {
            var dataPoints = emotionData[emotionType].map(function(entry) {
                return { x: entry.date, y: entry.intensity };
            });
            datasets.push({
                label: emotionType,
                data: dataPoints,
                backgroundColor: emotionColors[emotionType],
                borderColor: emotionColors[emotionType],
                fill: false,
                borderWidth: 2
            });
        }
    }

    var emotionChart = new Chart(ctx, {
        type: 'line',  // Puedes cambiar a 'bar' si prefieres ese tipo de gráfico
        data: {
            datasets: datasets  // Los diferentes tipos de emociones con sus colores
        },
        options: {
            scales: {
                x: {
                    type: 'time',  // Configura el eje X como una escala de tiempo
                    time: {
                        unit: 'day',  // Ajusta la unidad de tiempo (puede ser 'day', 'month', etc.)
                        tooltipFormat: 'YYYY-MM-DD',  // Formato para mostrar en los tooltips
                        displayFormats: {
                            day: 'MMM DD'  // Formato para mostrar en el eje X
                        }
                    },
                    title: {
                        display: true,
                        text: 'Fecha'
                    }
                },
                y: {
                    beginAtZero: true,
                    max: 10  // Ya que la intensidad es del 1 al 10
                }
            }
        }
    });
}
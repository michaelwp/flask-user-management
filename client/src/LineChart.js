import React from 'react';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js';
import { Line } from 'react-chartjs-2';

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);

export const options = {
    responsive: true,
    plugins: {
        legend: {
            display: false,
            position: 'bottom',
        },
        title: {
            display: true,
            text: 'Freq Dist',
        },
    },
};


const LineChart = (props) => {
    const data = {
        labels: props.data.map(row => row.text),
        datasets: [
            {
                data: props.data.map(row => row.value),
                borderColor: 'rgb(255, 99, 132)',
                tension: 0.5,
            },
        ],
    };

    return (
        <>
            <Line
                data={data}
                options={options}
            />
        </>
    );
}
export default LineChart;
import React from 'react';
import ReactWordcloud from 'react-wordcloud';

const WordCloudChart = (props) => {
    const options = {
        rotations: 2,
        rotationAngles: [-90, 0],
        fontSizes: [10,75],
    };

    const size = [600, 300];

    return (
        <ReactWordcloud
            words={props.data}
            options={options}
            size={size}
        />
    );
}
export default WordCloudChart;
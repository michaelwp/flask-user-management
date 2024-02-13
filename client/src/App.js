import React from 'react';
import axios from 'axios';
import LineChart from './LineChart'
import WordCloudChart from "./WordCloudChart";

function App() {
    const [sentence, setSentence] = React.useState("");
    const [data, setData] = React.useState([])

    const setupFreqDistKey = (data) => {
        const dataArr = []

        sortingDataDescByValue(data).forEach(e => {
            dataArr.push({
                text: e[0]
                , value: e[1]
            })
        })

        setData(dataArr)
    }


    const sortingDataDescByValue = (obj) => {
        const sortable = []
        for (const prop in obj) {
            sortable.push([prop, obj[prop]])
        }

        sortable.sort((a, b) => {
            return b[1] - a[1]
        })

        return sortable
    }

    const handleSubmit = () => {
        axios.post('http://localhost:5000/nltk/freq_dist', {
            sentence: sentence,
        }).then(function (response) {
            console.log("response:", response.data.data);
            setupFreqDistKey(response.data.data)
        }).catch(function (error) {
            console.log("error:", error);
        });
    }

    const handleSentenceChange = (event) => {
        setSentence(event.target.value)
    }

    const handleUpload = (event) => {
        const formData = new FormData();

        formData.append(
            "file",
            event.target.files[0]
            , event.target.files[0].name
        );

        axios.post('http://localhost:5000/nltk/freq_dist/upload',
            formData
        ).then(function (response) {
            console.log("response:", response.data.data);
            setupFreqDistKey(response.data.data)
        }).catch(function (error) {
            console.log("error:", error);
        });
    };

    const formControl =
        <>
            <div className="row m-3">
                <div className="col-1"/>
                <div className="col-10">
                    <textarea
                        className="form-control"
                        placeholder="sentence"
                        id="floatingTextarea"
                        rows={5}
                        onChange={handleSentenceChange}
                    />
                </div>
                <div className="col-1"/>
            </div>
            <div className="row m-3">
                <div className="col">
                    <button className="btn btn-primary m-1" onClick={handleSubmit}>Submit</button>
                    <input type="file" onChange={handleUpload}/>
                </div>
            </div>
        </>

    return (
        <div className="container m-5 text-center">
            <div className="row m-3">
                <div className="col">
                    <h1>NLTK</h1>
                </div>
            </div>
            <div className="row m-3">
                <div className="col">
                    {formControl}
                </div>
            </div>
            <div className="row m-3">
                <div className="col" >
                    <div style={{backgroundColor:'white'}}><WordCloudChart data={data}/></div>
                </div>
                <div className="col">
                    <div style={{backgroundColor:'white'}}><LineChart data={data.slice(0,25)}/></div>
                </div>
            </div>
        </div>
    );
}

export default App;

import React, { useState } from 'react';
import ExcelUpload from './components/ExcelUpload';
import ResultsView from './components/ResultsView';

const App: React.FC = () => {
    const [data, setData] = useState<any[]>([]);

    const handleDataUpload = (uploadedData: any[]) => {
        setData(uploadedData);
    };

    return (
        <div>
            <h1>Excel Analyzer</h1>
            <ExcelUpload onDataUpload={handleDataUpload} />
            <ResultsView data={data} />
        </div>
    );
};

export default App;
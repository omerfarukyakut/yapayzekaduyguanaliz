import React from 'react';

interface ResultsViewProps {
    data: any[]; // Replace 'any' with a more specific type based on your data structure
}

const ResultsView: React.FC<ResultsViewProps> = ({ data }) => {
    return (
        <div>
            <h2>Excel Dosyasının Sonuçları</h2>
            {data.length > 0 ? (
                <table>
                    <thead>
                        <tr>
                            {/* Replace with actual headers based on your data */}
                            <th>Başlık 1</th>
                            <th>Başlık 2</th>
                            <th>Başlık 3</th>
                        </tr>
                    </thead>
                    <tbody>
                        {data.map((item, index) => (
                            <tr key={index}>
                                {/* Replace with actual data fields based on your data structure */}
                                <td>{item.field1}</td>
                                <td>{item.field2}</td>
                                <td>{item.field3}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            ) : (
                <p>Henüz sonuç yok. Lütfen bir Excel dosyası yükleyin.</p>
            )}
        </div>
    );
};

export default ResultsView;
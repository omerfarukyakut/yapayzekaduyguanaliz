import React, { useState } from 'react';

const ExcelUpload: React.FC<{ onFileUpload: (data: any) => void }> = ({ onFileUpload }) => {
    const [file, setFile] = useState<File | null>(null);

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const selectedFile = event.target.files?.[0];
        if (selectedFile) {
            setFile(selectedFile);
        }
    };

    const handleFileUpload = async () => {
        if (file) {
            const data = await readExcelFile(file);
            onFileUpload(data);
        }
    };

    const readExcelFile = (file: File): Promise<any> => {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = (event) => {
                const binaryStr = event.target?.result;
                // Here you would parse the Excel file and return the data
                // For example, using a library like xlsx
                resolve(binaryStr); // Replace with actual parsed data
            };
            reader.onerror = (error) => reject(error);
            reader.readAsBinaryString(file);
        });
    };

    return (
        <div>
            <input type="file" accept=".xlsx, .xls" onChange={handleFileChange} />
            <button onClick={handleFileUpload} disabled={!file}>
                Upload Excel
            </button>
        </div>
    );
};

export default ExcelUpload;
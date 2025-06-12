interface ExcelData {
    sheetName: string;
    headers: string[];
    rows: Array<Record<string, any>>;
}

interface UploadResponse {
    success: boolean;
    message: string;
    data?: ExcelData;
}

export type { ExcelData, UploadResponse };
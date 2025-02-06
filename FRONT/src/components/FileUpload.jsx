"use client";
import React, { useState } from 'react';
import JsonViewer from "./JsonViewer"; 

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');
  const [jsonData, setJsonData] = useState(null);

  // Maneja la selección del archivo
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  // Maneja el envío del archivo
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file) {
      setMessage('Por favor selecciona un archivo.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:5000/upload', {
        method: 'POST',
        body: formData,
      });

      const result = await response.json();

      if (response.ok) {
        setMessage('Archivo subido y procesado correctamente');
        setJsonData(result.json_data); // Establece los datos JSON en el estado
      } else {
        setMessage(result.message);
      }
    } catch (error) {
      setMessage('Error al subir el archivo');
    }
  };

  return (
    <div className="flex justify-center items-center bg-gray-100">
      <div className="p-6 bg-white rounded-lg shadow-md">
        <form onSubmit={handleSubmit} className="space-y-4">
          <label htmlFor="file-upload" className="block text-lg font-semibold">
            Subir archivo PDF:
          </label>
          <input
            type="file"
            accept="application/pdf"
            onChange={handleFileChange}
            className="block w-full p-2 border border-gray-300 rounded-md"
          />
          <button
            type="submit"
            className="w-full py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition"
          >
            Subir
          </button>
        </form>
        {message && (
          <div className="mt-4 p-4 bg-green-100 text-center rounded-md border border-green-400">
            {message}
          </div>
        )}
        {jsonData && <JsonViewer jsonData={jsonData} />}
      </div>
    </div>
  );
};

export default FileUpload;

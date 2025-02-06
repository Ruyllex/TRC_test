const JsonViewer = ({ jsonData }) => {
    return (
      <div className="mt-6 p-4 bg-white rounded-lg shadow-md">
        <h3 className="text-xl font-semibold mb-4">Datos procesados:</h3>
        <div className="p-4 bg-gray-100 rounded-md overflow-auto">
          {/* Aquí mostramos el JSON todo en una línea */}
          <pre className="whitespace-pre-wrap text-gray-700 text-sm">
            {JSON.stringify(jsonData, null, 2)}
          </pre>
        </div>
      </div>
    );
  };
  
  
export default JsonViewer;
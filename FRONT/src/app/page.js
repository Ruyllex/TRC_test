import FileUpload from "../components/FileUpload";
import Title from "../components/Title";

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-50 p-4">
      <Title text="Subir Archivo PDF" />
      <FileUpload />
    </div>
  );
}
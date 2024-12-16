import React, { useState } from 'react';

function FileUpload() {
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    setUploading(true);
    // Simulating file upload
    await new Promise(resolve => setTimeout(resolve, 2000));
    setUploading(false);
    alert('File uploaded successfully!');
    setFile(null);
  };

  return (
    <section id="upload" className="py-16 bg-white-500 ">
      <div className="container mx-auto px-4 ">
        <h2 className="text-3xl font-bold text-center mb-8">Upload Your Dataset</h2>
        <form onSubmit={handleSubmit} className="max-w-md mx-auto">
          <div className="mb-4">
            <label htmlFor="file-upload" className="block text-sm font-medium text-gray-700 mb-2">
              Choose a file
            </label>
            <input
              id="file-upload"
              name="file-upload"
              type="file"
              accept=" "
              onChange={handleFileChange}
              className="block w-full text-sm text-gray-500
                file:mr-4 file:py-2 file:px-4
                file:rounded-full file:border-0
                file:text-sm file:font-semibold
                file:bg-blue-50 file:text-blue-700
                hover:file:bg-blue-100
              "
            />
          </div>
          <button
            type="submit"
            disabled={!file || uploading}
            className={`w-full py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 ${
              (!file || uploading) && 'opacity-50 cursor-not-allowed'
            }`}
          >
            {uploading ? 'Uploading...' : 'Upload'}
          </button>
        </form>
      </div>
    </section>
  );
}

export default FileUpload;


import React from "react";



export function FileUpload(props) {
  const ImageStyle = { width: '250px', height: '300px' };

  const [image, setImage] = React.useState(null);
  const [createObjectURL, setCreateObjectURL] = React.useState(null);

  const uploadToClient = (event) => {
    if (event.target.files && event.target.files[0]) {
      const i = event.target.files[0];

      setImage(i);
      setCreateObjectURL(URL.createObjectURL(i));
    }
  };

  const uploadToServer = async (event) => {
    const body = new FormData();
    body.append("file", image);
    const response = await fetch("http://172.187.216.226:5000/upload", {
      method: "POST",
      body
    });
  };

  return (
    <div>
      <input type="file" name="myImage" accept="image/*" onChange={uploadToClient} />
      {image ? <img src={createObjectURL} style={ImageStyle} className="image" alt="preview" /> : null}
      <button type="submit" onClick={uploadToServer}>
        <h2 className={`mb-3 text-2xl font-semibold`}>
          Send  image to server
        </h2>
      </button>
    </div>
  );
}

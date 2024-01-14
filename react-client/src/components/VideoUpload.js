import React from "react";







export function VideoUpload(props) {

  const [image, setImage] = React.useState(null);
  const [createObjectURL, setCreateObjectURL] = React.useState(null);
  const inputRef = React.useRef();
  const [source, setSource] = React.useState();
  const { width, height } = props;

  const ImageStyle = { width: '250px', height: '300px' };

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    const url = URL.createObjectURL(file);
    console.log(file);
    setSource(url);
    setImage(file);
  };
  const uploadToClient = (event) => {
    if (event.target.files && event.target.files[0]) {
      const i = event.target.files[0];

      setImage(i);
      setCreateObjectURL(URL.createObjectURL(i));
    }
  };

  console.log(image);
  const uploadToServer = async (event) => {
    const body = new FormData();
    body.append("file", image);
    const response = await fetch("http://172.187.216.226:5000/uploadvideo", {
      method: "POST",
      body
    });
  };

  return (
    <div>
      <input
        ref={inputRef}
        className="VideoInput_input"
        type="file"
        onChange={handleFileChange}
        accept=".mov,.mp4" />
      <button type="submit" onClick={uploadToServer}>
        <h2 className={`mb-3 text-2xl font-semibold`}>
          Send  video to server
        </h2>
      </button>
      <video
        className="VideoInput_video"
        width="320"
        height="240"
        controls
        src={source} />
    </div>
  );
}

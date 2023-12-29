import React from "react";
import { VideoCameraIcon } from '@heroicons/react/24/outline';
import { TbTruckDelivery } from "react-icons/tb";

export default function SideNav() {
  const menuItems = [
    { icon: <TbTruckDelivery size={25} className="mr-4" />, text: "Orders" },
  ];
  return (
    <>
      <div className="max-w-[1640px] mx-auto flex justify-between items-center p-4 shadow-sm">
        <div className="bg-blue-500 fixed top-0 left-0 w-[300px] h-screen bg-white z-10 duration-300">
          <h2 className="text-2l p-4">
            <FileUpload />
          </h2>
          <nav>
            <ul className="flex flex-col p-4 text-gray-800">
              {menuItems.map(({ icon, text }, index) => {
                return (
                  <div key={index} className=" py-4">
                    <li className="text-xl flex cursor-pointer  w-[50%] rounded-full mx-auto p-2 hover:text-white hover:bg-black">
                      {icon} {text}
                    </li>
                  </div>
                );
              })}
            </ul>
          </nav>
        </div>
      </div>

    </>
  );
}


export function FileUpload(props) {
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
    const response = await fetch("http://localhost:5000/upload", {
      method: "POST",
      body
    });
  };

  return (
    <div>
      <p>
        <input type="file" name="myImage" onChange={uploadToClient} />
      </p>
      <button type="submit" onClick={uploadToServer}
        className="mt-10 flex h-[48px] grow items-center justify-center gap-2 rounded-md bg-gray-50 p-3 text-sm font-medium hover:bg-sky-100 hover:text-blue-600 md:flex-none md:justify-start md:p-8 md:px-3"
      >
        <br />
        <p>
          Send Video file to server
        </p>
        <VideoCameraIcon className="mr-4" />
      </button>
    </div>
  );
}
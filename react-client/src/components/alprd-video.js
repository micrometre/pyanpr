export default function AlprVideo() {
    return (
      <>
        <div className="rounded-xl bg-gray-50 p-2 shadow-sm">
          <div className="flex p-4">
            <h2 className="font-semibold">
                <video width="320" height="240" controls>
                  <source src='http://localhost:5000/video' type="video/mp4" />
                  Your browser does not support the video tag.
                </video>
            </h2>
          </div>
        </div>
  
      </>
    );
  }
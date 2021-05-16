import React from "react";

const ResultVideo = ({ video }) => {
  if (!video) {
    return <div>
           </div>;
  }

  return (
    <div>
      <video width="320" height="240" controls>
        <source src="/media/video/21/G2fOum_KWQU_subtitled_XH7yFbW.mp4" type="video/mp4">
        </source>
        Your browser does not support this video format.

      </video>
    </div>
  );
};

export default ResultVideo;

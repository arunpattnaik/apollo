import React from "react";
import Main from "./main";

const Home = async () => {
  const response = await fetch("http://localhost:8000/api/videos", {
    next: { revalidate: 0 },
  });

  return (
    <div>
      <Main files={await response.json()} />
    </div>
  );
};

export default Home;

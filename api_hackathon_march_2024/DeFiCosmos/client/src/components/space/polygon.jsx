import React, { useRef, useEffect } from "react";

const Polygon = () => {
  const sun = useRef(null);
  const planet = [useRef(null), useRef(null), useRef(null), useRef(null), useRef(null)];
  const dimIntegers = [0.2, 0.5, 0.3, 0.2, 0.7];
  const gradientPlanet1 = { clr1: `#F40752`, clr2: `#F9AB8F` };
  const gradientPlanet2 = { clr1: `#492957`, clr2: `#744A6D` };
  const gradientPlanet3 = { clr1: `#B597F6`, clr2: `#96C6EA` };
  const gradientPlanet4 = { clr1: `#B597F6`, clr2: `#96C6EA` };
  const gradientPlanet5 = { clr1: `#B597F6`, clr2: `#96C6EA` };
  const planetStyles = [
    {
      background: `linear-gradient(to right, ${gradientPlanet1.clr1}, ${gradientPlanet1.clr2})`,
      borderRadius: "100%",
      boxShadow: `0 0 ${(2 * dimIntegers[0]).toString() + "px"} ${
        gradientPlanet1.clr1
      }`,
      height: `${dimIntegers[0]}vw`,
      width: `${dimIntegers[0]}vw`,
    },
    {
      background: `linear-gradient(to right, ${gradientPlanet2.clr1}, ${gradientPlanet2.clr2})`,
      borderRadius: "100%",
      boxShadow: `0 0 ${(2 * dimIntegers[1]).toString() + "px"} ${
        gradientPlanet2.clr1
      }`,
      height: `${dimIntegers[1]}vw`,
      width: `${dimIntegers[1]}vw`,
    },
    {
      background: `linear-gradient(to right, ${gradientPlanet3.clr1}, ${gradientPlanet3.clr2})`,
      borderRadius: "100%",
      boxShadow: `0 0 ${(2 * dimIntegers[2]).toString() + "px"} ${
        gradientPlanet3.clr1
      }`,
      height: `${dimIntegers[2]}vw`,
      width: `${dimIntegers[2]}vw`,
    },
    {
      background: `linear-gradient(to right, ${gradientPlanet4.clr1}, ${gradientPlanet4.clr2})`,
      borderRadius: "100%",
      boxShadow: `0 0 ${(2 * dimIntegers[2]).toString() + "px"} ${
        gradientPlanet4.clr1
      }`,
      height: `${dimIntegers[2]}vw`,
      width: `${dimIntegers[2]}vw`,
    },
    {
      background: `linear-gradient(to right, ${gradientPlanet5.clr1}, ${gradientPlanet5.clr2})`,
      borderRadius: "100%",
      boxShadow: `0 0 ${(2 * dimIntegers[2]).toString() + "px"} ${
        gradientPlanet5.clr1
      }`,
      height: `${dimIntegers[2]}vw`,
      width: `${dimIntegers[2]}vw`,
    },
  ];
  const planetRadius = [25, 37, 40, 50, 67];
  const planetRadian = [
    Math.PI * 2 * 0.2,
    Math.PI * 2 * 0.3,
    Math.PI * 2 * 0.9,
    Math.PI * 2 * 0.4,
    Math.PI * 2 * 0.1,
  ];
  const planetVelocity = [0.5, 0.8, 0.7, 0.1, 0.2];
  const sunStyle = {
    background: `linear-gradient(to right, #ff5282 ,#f28367)`,
    borderRadius: "100%",
    height: `3vw`,
    width: `3vw`,
    zIndex: 1
  };
  const containerStyle = { height: `3vw`, width: `3vw` };
  const rotate = (refArray, planetRadius, planetVelocity, planetRadian) => {
    const intervalId = setInterval(() => {
      refArray.forEach((ref, index) => {
        const planet = ref.current;
        if (planet) {
          const sunCenterX = sun.current.offsetWidth / 2;
          const sunCenterY = sun.current.offsetHeight / 2;
          const planetCenterX =
            sunCenterX -
            planet.offsetWidth / 2 +
            Math.cos(planetRadian[index]) * planetRadius[index] * 2;
          const planetCenterY =
            sunCenterY -
            planet.offsetHeight / 2 +
            Math.sin(planetRadian[index]) * planetRadius[index];

          planet.style.left = `${planetCenterX}px`;
          planet.style.top = `${planetCenterY}px`;
          planetRadian[index] += planetVelocity[index] * 0.02;

          const isBehindSun = planetCenterY < sunCenterY;
          planet.style.zIndex = !isBehindSun ? 2 : 0;
        }
      });
    }, 10);

    return intervalId;
  };

  useEffect(() => {
    console.log("called rotate");
    const intervalID = rotate(
      planet,
      planetRadius,
      planetVelocity,
      planetRadian
    );
    return () => clearInterval(intervalID);
  }, [planetRadian, planetRadius, planetVelocity, planet]);
  return (
    <div className="system-container" style={containerStyle}>
      <div className="polygon-sun sun" ref={sun} style={sunStyle}></div>
      <div
        className="polygon-planets planets"
        ref={planet[0]}
        style={planetStyles[0]}
      ></div>
      <div
        className="polygon-planets planets"
        ref={planet[1]}
        style={planetStyles[1]}
      ></div>
      <div
        className="polygon-planets planets"
        ref={planet[2]}
        style={planetStyles[2]}
      ></div>
       <div
        className="polygon-planets planets"
        ref={planet[3]}
        style={planetStyles[3]}
      ></div>
       <div
        className="polygon-planets planets"
        ref={planet[4]}
        style={planetStyles[4]}
      ></div>
    </div>
  );
};

export default Polygon;

import React, { useRef, useEffect } from "react";

const Base = () => {
  const sun = useRef(null);
  const planet = [useRef(null), useRef(null), useRef(null), useRef(null)];
  const dimIntegers = [0.5, 1, 0.8, 0.2];
  const gradientPlanet1 = { clr1: `#BEB15B`, clr2: `#D5CFAC` };
  const gradientPlanet2 = { clr1: `#0B2C24`, clr2: `#247A4D` };
  const gradientPlanet3 = { clr1: `#9BF8F4`, clr2: `#6F7BF7` };
  const gradientPlanet4 = { clr1: `#BC1B68`, clr2: `#D3989B` };
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
  ];
  const planetRadius = [35, 87, 60, 50];
  const planetRadian = [
    Math.PI * 2 * 0.5,
    Math.PI * 2 * 0.7,
    Math.PI * 2 * 0.9,
    Math.PI * 2 * 0.3,
  ];
  const planetVelocity = [0.9, 0.5, 0.7, 0.2];
  const sunStyle = {
    position: `absolute`,
    background: `linear-gradient(to right, #F9C58D ,#F492F0)`,
    borderRadius: "100%",
    height: `4vw`,
    width: `4vw`,
    zIndex: 1,
  };
  const containerStyle = { height: `4vw`, width: `4vw` };
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
      <div className="base-sun" ref={sun} style={sunStyle}></div>
      <div
        className="base-planets planets"
        ref={planet[0]}
        style={planetStyles[0]}
      ></div>
      <div
        className="base-planets planets"
        ref={planet[1]}
        style={planetStyles[1]}
      ></div>
      <div
        className="base-planets planets"
        ref={planet[2]}
        style={planetStyles[2]}
      ></div>
      <div
        className="base-planets planets"
        ref={planet[3]}
        style={planetStyles[3]}
      ></div>
    </div>
  );
};

export default Base;

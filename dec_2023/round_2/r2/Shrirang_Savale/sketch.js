// sketch.js
var radius;

function setup() {
  createCanvas(windowWidth, windowHeight);
  radius = 0.9 * min(width, height) / 2;
  background(255, 255, 255);
  drawLines(); // Call the drawLines function
}

function drawLines() {
  beginShape(LINES); // Start drawing a shape with lines
  stroke(0, 0, 0, 15); // Set the stroke color inside beginShape()

  for (var i = 0; i < 100; i++) {
    // Find a random point on a circle
    var angle1 = random(0, 2 * PI);
    var xpos1 = width / 2 + radius * cos(angle1);
    var ypos1 = height / 2 + radius * sin(angle1);

    // Find another random point on the circle
    var angle2 = random(0, 2 * PI);
    var xpos2 = width / 2 + radius * cos(angle2);
    var ypos2 = height / 2 + radius * sin(angle2);

    // Add the points to the shape
    vertex(xpos1, ypos1);
    vertex(xpos2, ypos2);
  }

  endShape(); // Finish drawing the shape
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
  radius = 0.9 * min(width, height) / 2;
  background(255, 255, 255);
  drawLines(); // Call the drawLines function after resizing
}

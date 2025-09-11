const needle = document.getElementById('needle');
const speedLabel = document.getElementById('speed-label');

let currentSpeed = 0;

function updateSpeedometer(speed) {
    let displaySpeed = speed;
    if (speed > 88) {
        displaySpeed = 880 + (speed - 88);
    }

    const rotation = (displaySpeed / 880) * 180; // Map speed to 0-180 degrees
    needle.style.transform = `rotate(${rotation}deg)`;
    speedLabel.textContent = `${Math.round(displaySpeed)} MPH`;
}

// Simulate speed changes
document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowUp') {
        currentSpeed += 5;
    } else if (event.key === 'ArrowDown') {
        currentSpeed = Math.max(0, currentSpeed - 5);
    }
    updateSpeedometer(currentSpeed);
});

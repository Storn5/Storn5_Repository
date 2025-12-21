let shaking = 0;

theButton.onmousedown = () => {
    console.log("clicked");
    shaking = 30;
};

function frame(timestamp) {
    if (shaking > 1) {
        shaking--;
        let width = 25 + Math.random() * 6 - 3;
        let height = 40 + Math.random() * 10 - 5;
        theButton.style.width = `${width}%`;
        theButton.style.height = `${height}px`;
    } else if (shaking == 1) {
        shaking = 0;
        theButton.style.width = `25%`;
        theButton.style.height = `40px`;
    }

    window.requestAnimationFrame(frame);
}

window.requestAnimationFrame(frame);
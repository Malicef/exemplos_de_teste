const audioContext = new (window.AudioContext || window.webkitAudioContext)();
const progress = document.getElementById("progress");
const currentTimeSpan = document.getElementById("currentTime");
const durationSpan = document.getElementById("duration");

let sourceNode;
let audioBuffer;
let gainNode = audioContext.createGain();
let filterNode = audioContext.createBiquadFilter();
let isFilterActive = false;
let startTime = 0;
let pausedAt = 0;
let isPlaying = false;

filterNode.type = "lowpass";
filterNode.frequency.value = 1000;
// Carrega o áudio ao iniciar
fetch('assets/musica.mp3.crdownload')
  .then(res => res.arrayBuffer())
  .then(buffer => audioContext.decodeAudioData(buffer))
  .then(decoded => {
    audioBuffer = decoded;
  });

function formatTime(seconds){
    const minutes = Math.floor(seconds/60);
    const secs = Math.floor(seconds % 60).toString().padStart(2, '0');
    return `${minutes}:${secs}`;
}

function createSource() {
    if (sourceNode) {
      sourceNode.onended = null;
      try { sourceNode.stop(); } catch(e) {}
      sourceNode.disconnect();
    }
    
    sourceNode = audioContext.createBufferSource();
    sourceNode.buffer = audioBuffer;
  
    sourceNode.onended = () => {
      isPlaying = false;
      pausedAt = 0; 
    };
  
    if (isFilterActive) {
      sourceNode.connect(filterNode).connect(gainNode).connect(audioContext.destination);
    } else {
      sourceNode.connect(gainNode).connect(audioContext.destination);
    }
}

function updateProgress() {
    if (isPlaying && sourceNode && audioBuffer){
        const current = audioContext.currentTime - startTime;
        currentTimeSpan.textContent = formatTime(current);
        progress.value = (current / audioBuffer.duration) * 100;
        requestAnimationFrame(updateProgress);
    }
}

function pauseAudio() {
    if (isPlaying && sourceNode) {
        sourceNode.stop();
        pausedAt = audioContext.currentTime - startTime;
        isPlaying = false;
      }
}

function stopAudio() {
    if (isPlaying && sourceNode) {
      sourceNode.stop();
      isPlaying = false;
    }
    pausedAt = 0;
  }

document.getElementById("pause").addEventListener("click", pauseAudio);
document.getElementById("stop").addEventListener("click", stopAudio);

// // PLAY
document.getElementById("play").addEventListener("click", () => {
    if (!audioBuffer || isPlaying) return;
    
    createSource();
    sourceNode.start(0, pausedAt);
    startTime = audioContext.currentTime - pausedAt;
    isPlaying = true;
});

// Atualiza a duração do play
document.getElementById("play").addEventListener("click", () => {
    if(audioBuffer){
        durationSpan.textContent = formatTime(audioBuffer.duration);
        requestAnimationFrame(updateProgress);
    }
});

// VOLUME
document.getElementById("volume").addEventListener("input", (e) => {
  const volume = e.target.value / 100;
  gainNode.gain.setValueAtTime(volume, audioContext.currentTime);
});

// FILTRO
document.getElementById("toggleFilter").addEventListener("click", () => {
    isFilterActive = !isFilterActive;
  
    if (isPlaying) {
      sourceNode.stop();
      createSource();
      sourceNode.start(0, pausedAt);
      startTime = audioContext.currentTime - pausedAt;
      isPlaying = true;
      updateProgress();
    }
  });

progress.addEventListener("input", () => {
    if(audioBuffer){
        const newTime = (progress.value)/100 * audioBuffer.duration;
    pausedAt = newTime;
    if (isPlaying){
        sourceNode.stop();
        createSource();
        sourceNode.start(0, pausedAt);
        startTime = audioContext.currentTime - pausedAt;
    }
    }
})


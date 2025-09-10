import React, { useState } from 'react';
import { motion } from 'framer-motion';

const remixStyles = [
  'Grikify', 'Shrekify', 'DonkeySrcify', 'Emojify', 'Redditify', 'Githubify', 'Apify',
  'Vectorize', 'Improvize', 'Ethicify', 'Autonify', 'Synchronize', 'Randomize', 'ToneDown', 'LevelOut'
];

const toneLevels = ['Extreme', 'Bold', 'Balanced', 'Subtle', 'Minimal'];
const themes = ['Grok', 'Shrek', 'Donkey', 'Emoji', 'Reddit', 'GitHub', 'API', 'Vector', 'Ethics', 'Automation'];
const animationTypes = ['Fade', 'Slide', 'Bounce', 'Spin', 'Morph', 'Pulse', 'Flip', 'Zoom'];
const imageGenerators = ['Stable Diffusion', 'DALL-E', 'Gemini', 'Midjourney', 'DreamStudio'];

function getRandom(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

export default function UIUXRemixerDashboard() {
  const [remix, setRemix] = useState({
    style: getRandom(remixStyles),
    tone: getRandom(toneLevels),
    theme: getRandom(themes),
    animation: getRandom(animationTypes),
    imageGen: getRandom(imageGenerators)
  });

  const handleRemix = () => {
    setRemix({
      style: getRandom(remixStyles),
      tone: getRandom(toneLevels),
      theme: getRandom(themes),
      animation: getRandom(animationTypes),
      imageGen: getRandom(imageGenerators)
    });
  };

  return (
    <div style={{ background: '#181818', color: '#fff', minHeight: '100vh', padding: '2rem', fontFamily: 'Inter, sans-serif' }}>
      <motion.h1 initial={{ opacity: 0, y: -40 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.7 }} style={{ fontSize: '2.5rem', fontWeight: 700, marginBottom: '1.5rem' }}>
        UIUX Remixer Dashboard
      </motion.h1>
      <motion.div initial={{ scale: 0.9 }} animate={{ scale: 1 }} transition={{ duration: 0.5 }} style={{ background: '#232323', borderRadius: '1rem', padding: '2rem', boxShadow: '0 8px 32px #0006', maxWidth: 500, margin: '0 auto' }}>
        <div style={{ fontSize: '1.25rem', marginBottom: '1rem' }}>
          <strong>Remix Style:</strong> {remix.style}
        </div>
        <div style={{ fontSize: '1.25rem', marginBottom: '1rem' }}>
          <strong>Tone:</strong> {remix.tone}
        </div>
        <div style={{ fontSize: '1.25rem', marginBottom: '1rem' }}>
          <strong>Theme:</strong> {remix.theme}
        </div>
        <div style={{ fontSize: '1.25rem', marginBottom: '1rem' }}>
          <strong>Animation:</strong> {remix.animation}
        </div>
        <div style={{ fontSize: '1.25rem', marginBottom: '2rem' }}>
          <strong>Image Generator:</strong> {remix.imageGen}
        </div>
        <motion.button whileHover={{ scale: 1.1 }} whileTap={{ scale: 0.95 }} onClick={handleRemix} style={{ background: 'linear-gradient(90deg,#6ee7b7,#3b82f6)', color: '#181818', border: 'none', borderRadius: '0.5rem', padding: '0.75rem 2rem', fontWeight: 600, fontSize: '1.1rem', cursor: 'pointer', boxShadow: '0 2px 8px #0003' }}>
          Remix!
        </motion.button>
      </motion.div>
    </div>
  );
}

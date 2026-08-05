import {animate,stagger} from "https://cdn.jsdelivr.net/npm/animejs@4/lib/anime.iife.min.js"

export function initCardsAnim() {
  anime.animate(".card", {
    opacity: [0, 1],
    translateY: [24, 0],
    delay: anime.stagger(120),
    duration: 700,
    ease: "outBack",
  });
}

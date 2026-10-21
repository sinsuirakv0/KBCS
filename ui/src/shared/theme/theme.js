import {siteBorderColor} from '../game/site-settings.js';
const themes = new Set(["original", "dark", "light"]);

function renderTheme(theme) {
  document.documentElement.style.setProperty('--color-border',siteBorderColor(theme,Number(document.documentElement.dataset.siteBorder??50)));
  if (theme === "original") document.documentElement.removeAttribute("data-theme");
  else document.documentElement.dataset.theme = theme;
  document.querySelectorAll("[data-theme-value]").forEach((button) => {
    button.setAttribute("aria-pressed", String(button.dataset.themeValue === theme));
  });
}

export function setTheme(theme) {
  if (!themes.has(theme)) return;
  renderTheme(theme);
  try {
    localStorage.setItem("kbc-theme", theme);
    const saved=JSON.parse(localStorage.getItem("kbc-preferences")||"null");
    if(saved?.version===1&&saved.site?.theme!==theme)localStorage.setItem("kbc-preferences",JSON.stringify({...saved,site:{...saved.site,theme}}));
  } catch {
    // 保存に失敗しても現在の画面には反映する。
  }
}

export function initializeThemeControls() {
  renderTheme(document.documentElement.dataset.theme || "original");
  document.querySelectorAll("[data-theme-value]").forEach((button) => {
    button.addEventListener("click", () => setTheme(button.dataset.themeValue));
  });
  window.addEventListener("storage", (event) => {
    if (event.key === "kbc-theme" || event.key === null) renderTheme(themes.has(event.newValue) ? event.newValue : "original");
  });
}

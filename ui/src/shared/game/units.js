const dataUrl = "/api/catalog";

let pending;
export function loadUnitDatabase() {
  if (!pending) pending = fetch(dataUrl).then(async response => {
    if (!response.ok) throw new Error("キャラデータを取得できませんでした。");
    const data = await response.json();
    if (data.schemaVersion !== 9 || !Array.isArray(data.units)) throw new Error("キャラデータの形式が不正です。");
    return data;
  }).catch(error => { pending = null; throw error; });
  return pending;
}

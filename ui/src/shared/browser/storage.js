export function readStoredItems(storageKey) {
  try {
    const items = JSON.parse(localStorage.getItem(storageKey) || "[]");
    return Array.isArray(items) ? items : [];
  } catch {
    return [];
  }
}

export function readStoredValue(storageKey, fallback = null) {
  try {
    const value = localStorage.getItem(storageKey);
    return value === null ? fallback : JSON.parse(value);
  } catch {
    return fallback;
  }
}

export function writeStoredItems(storageKey, items) {
  try {
    localStorage.setItem(storageKey, JSON.stringify(items));
    return true;
  } catch {
    return false;
  }
}

export function clearStoredItems(storageKey) {
  try {
    localStorage.removeItem(storageKey);
    return true;
  } catch {
    return false;
  }
}

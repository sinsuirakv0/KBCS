import {normalizeSimulationProfile,migrateSimulationProfile} from './simulation-profile.js';
const storageKey='kbcs:simulation-profile';
export function readSimulationProfile(legacy={}){
  try{const value=JSON.parse(localStorage.getItem(storageKey)||'null');if(value?.schemaVersion===1)return normalizeSimulationProfile({...value,cannon:value.cannon??migrateSimulationProfile(legacy).cannon});}catch{}
  return migrateSimulationProfile(legacy);
}
export function writeSimulationProfile(profile){
  try{localStorage.setItem(storageKey,JSON.stringify(normalizeSimulationProfile(profile)));return true;}catch{return false;}
}

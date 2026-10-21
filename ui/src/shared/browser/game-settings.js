import {deriveSimulationSettings} from "../../../simulation-profile.js";
import {readSimulationProfile} from "../../../simulation-store.js";
import {readStoredValue} from './storage.js';
import {gameSettingFields,normalizeGameSettings,defaultGameSettings} from '../game/game-settings.js';
import {defaultSiteSettings,normalizeSiteSettings,encodeSettings,decodeSettings} from '../game/site-settings.js';
import {setTheme} from '../theme/theme.js';
import {copyText} from './clipboard.js';

const storageKey='kbc-game-settings',siteKey='kbc-site-settings',preferencesKey='kbc-preferences';
let dialog,context,applyDatabase=false;
export function gameSettingsFieldsHtml(group,prefix='') {
  return gameSettingFields.filter(field=>field.group===group).map(({key,label,min,max,options,labels})=>'<label>'+label+(group!=='display'&&group!=='cannon'&&!key.endsWith('Level')?' %':'')+(options?'<select name="'+key+'"'+(prefix?' id="'+prefix+'-'+key+'"':'')+'>'+options.map((value,index)=>'<option value="'+value+'">'+(labels?.[index]??value+'件')+'</option>').join('')+'</select>':'<input name="'+key+'"'+(prefix?' id="'+prefix+'-'+key+'"':'')+' type="number" min="'+min+'" max="'+max+'" required step="1">')+'</label>').join('');
}
function readPreferences(){const value=readStoredValue(preferencesKey);return value?.version===1?value:null;}
export function readGameSettings(){const legacy=normalizeGameSettings(readPreferences()?.database||readStoredValue(storageKey));return {...legacy,...deriveSimulationSettings(readSimulationProfile(legacy))};}
export function updateGameSettings(values){return saveSettings({site:readSiteSettings(),database:normalizeGameSettings({...readGameSettings(),...values})});}
function readSiteSettings(){return normalizeSiteSettings(readPreferences()?.site||{...readStoredValue(siteKey),theme:document.documentElement.dataset.theme||'original'});}
function applySiteSettings(value){
  const root=document.documentElement;root.dataset.siteBorder=value.border;setTheme(value.theme);
  root.style.setProperty('--site-scale',value.scale/100);
}
function saveSettings(value){
  // サイト・DB設定は一つのキーへ保存し、途中まで書き換わる状態を作らない。
  try{localStorage.setItem(preferencesKey,JSON.stringify({version:1,...value}));return true;}catch{return false;}
}
function switchPanel(name){
  for(const panel of dialog.querySelectorAll('[data-settings-panel]'))panel.hidden=panel.dataset.settingsPanel!==name;
  for(const button of dialog.querySelectorAll('[data-settings-tab]'))button.setAttribute('aria-selected',String(button.dataset.settingsTab===name));
}
function fillSettings(value){
  const form=dialog.querySelector('form');
  for(const [key,item] of Object.entries(value.site))form.elements.namedItem('site-'+key).value=item;
  for(const {key} of gameSettingFields){const field=form.elements.namedItem(key);if(field)field.value=value.database[key];}
  for(const key of ['scale','border'])dialog.querySelector('[data-value="'+key+'"]').value=value.site[key]+(key==='scale'?'%':'');
}
function collectSettings(){
  const form=dialog.querySelector('form'),formElementValue=key=>form.elements.namedItem(key).value;
  const values=Object.fromEntries(new FormData(form));
  return {site:normalizeSiteSettings(Object.fromEntries(Object.keys(defaultSiteSettings).map(key=>[key,formElementValue('site-'+key)]))),database:normalizeGameSettings({...readGameSettings(),...values})};
}
export function openSiteSettings(panel='site'){
  initializeSiteSettings();
  applyDatabase=panel==='database';
  const saved=readGameSettings(),current=applyDatabase?context?.readCurrent()||{}:{};
  fillSettings({site:readSiteSettings(),database:normalizeGameSettings({...saved,...current,...Object.fromEntries(gameSettingFields.filter(field=>field.group==='display').map(({key})=>[key,saved[key]]))})});
  dialog.querySelector('output[role="status"]').textContent='';dialog.querySelector('textarea').value='';switchPanel(panel);
  if(!dialog.open)dialog.showModal();
}
export function initializeSiteSettings(){
  if(dialog)return;
  dialog=document.createElement('dialog');dialog.className='site-settings-dialog';dialog.setAttribute('aria-labelledby','site-settings-title');
  const fields=gameSettingsFieldsHtml;
  dialog.innerHTML='<form novalidate><div class="settings-heading"><h2 id="site-settings-title">設定</h2><button type="button" data-close>閉じる</button></div><div class="settings-tabs" role="tablist" aria-label="設定の分類"><button type="button" role="tab" data-settings-tab="site" aria-controls="settings-site">サイト</button><button type="button" role="tab" data-settings-tab="database" aria-controls="settings-database">DB・データ</button><button type="button" role="tab" data-settings-tab="transfer" aria-controls="settings-transfer">エクスポート・インポート</button></div>'+
    '<section id="settings-site" data-settings-panel="site"><h3>サイトの表示</h3><div class="game-settings-fields"><label>配色<select name="site-theme"><option value="original">濃紺</option><option value="dark">ダーク</option><option value="light">ライト</option></select></label><label>サイトの大きさ<input name="site-scale" type="range" min="75" max="150" step="1"><output data-value="scale"></output></label><label>線の濃さ<input name="site-border" type="range" min="0" max="100" step="1"><output data-value="border"></output></label></div><p>100%が現在の大きさです。線の濃さ50は標準。設定画面の操作サイズは固定です。</p><button type="button" data-reset="site">表示を標準に戻す</button></section>'+
    '<section id="settings-database" data-settings-panel="database" hidden><fieldset><legend>表示の初期値</legend><div class="game-settings-fields">'+fields('display')+'</div></fieldset><button type="button" data-profile-settings>お宝・施設を開く</button></section>'+
    '<section id="settings-transfer" data-settings-panel="transfer" hidden><p>表示とDBの基本設定を移せます。お宝・施設の個別設定はアプリ内に保存します。</p><label>設定文字列<textarea rows="5" maxlength="12000" spellcheck="false" autocapitalize="off" autocomplete="off"></textarea></label><div class="settings-actions"><button type="button" data-export>文字列を生成</button><button type="button" data-copy>文字列をコピー</button><button type="button" data-import>文字列を読み込む</button></div><p>読み込み後に各項目を確認し、「保存して反映」で確定します。</p></section><output class="settings-status" role="status" aria-live="polite"></output><div class="settings-actions"><button type="submit">保存して反映</button></div></form>';
  document.body.append(dialog);
  const form=dialog.querySelector('form'),status=dialog.querySelector('output[role="status"]'),text=dialog.querySelector('textarea');
  dialog.querySelector('[data-close]').addEventListener('click',()=>dialog.close());
  dialog.querySelector('[data-profile-settings]').addEventListener('click',()=>{dialog.close();window.dispatchEvent(new Event('kbcs:open-simulation-settings'));});
  for(const button of dialog.querySelectorAll('[data-settings-tab]'))button.addEventListener('click',()=>switchPanel(button.dataset.settingsTab));
  for(const key of ['scale','border'])form.elements.namedItem('site-'+key).addEventListener('input',event=>{dialog.querySelector('[data-value="'+key+'"]').value=event.target.value+(key==='scale'?'%':'');});
  for(const button of dialog.querySelectorAll('[data-reset]'))button.addEventListener('click',()=>{if(button.dataset.reset==='database')applyDatabase=true;const current=collectSettings();fillSettings({...current,[button.dataset.reset]:button.dataset.reset==='site'?defaultSiteSettings:defaultGameSettings});status.textContent='標準値を読み込みました。保存するまでは変更されません。';});
  for(const button of dialog.querySelectorAll('[data-preset]'))button.addEventListener('click',()=>{applyDatabase=true;for(const field of gameSettingFields.filter(field=>!['display','cannon'].includes(field.group)))form.elements.namedItem(field.key).value=button.dataset.preset==='max'?field.max:field.min;});
  dialog.querySelector('[data-export]').addEventListener('click',()=>{if(!form.checkValidity()){switchPanel('database');form.reportValidity();return;}const values=collectSettings();text.value=encodeSettings(values.site,values.database);status.textContent='現在の入力内容から文字列を生成しました。';});
  dialog.querySelector('[data-copy]').addEventListener('click',async()=>{try{if(!text.value)throw Error();await copyText(text.value);status.textContent='設定文字列をコピーしました。';}catch{status.textContent='文字列を選択してコピーしてください。';text.focus();text.select();}});
  dialog.querySelector('[data-import]').addEventListener('click',()=>{try{const imported=decodeSettings(text.value);fillSettings(imported);applyDatabase=true;status.textContent='読み込みました。内容を確認して保存してください。';}catch(error){status.textContent=error.message;}});
  form.addEventListener('input',event=>{if(gameSettingFields.some(field=>field.key===event.target.name))applyDatabase=true;});
  form.addEventListener('submit',event=>{
    event.preventDefault();if(!form.checkValidity()){switchPanel('database');form.reportValidity();return;}const values=collectSettings();
    if(!saveSettings(values)){status.textContent='ブラウザへ保存できませんでした。保存済み設定は変更していません。';return;}
    applySiteSettings(values.site);if(applyDatabase)context?.onApply(values.database);dialog.close();
  });
  document.querySelector('[data-site-settings]')?.addEventListener('click',()=>openSiteSettings());
  window.addEventListener('storage',event=>{if(event.key===preferencesKey||event.key===siteKey||event.key===null)applySiteSettings(readSiteSettings());});
  applySiteSettings(readSiteSettings());
}
export function initializeGameSettings(toolbar,readCurrent,onApply){
  context={readCurrent,onApply};initializeSiteSettings();
  const button=document.createElement('button');button.type='button';button.textContent='お宝・施設';button.addEventListener('click',()=>window.dispatchEvent(new Event('kbcs:open-simulation-settings')));toolbar.append(button);
}

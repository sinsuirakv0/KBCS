import {loadStageDatabase,loadStageMap} from './src/shared/game/stages.js';
import {loadEnemyDatabase} from './src/shared/game/enemies.js';
import {loadUnitDatabase} from './src/shared/game/units.js';
import {stageSummaryHtml,stageRulesHtml,stageRewardsHtml,stageSpawnsHtml} from './src/features/stages/view.js';
import {stageMapUrl,resolveStageRoute} from './src/features/stages/model.js';
import {escapeHtml,formatNumber} from './src/shared/game/database-view.js';
import {readGameSettings} from './src/shared/browser/game-settings.js';
import {readPageParams,writePageParams,bindDetailNavigation} from './native-state.js';
import {saveElementImage} from './src/shared/browser/capture.js';
import {calculateNative} from './native-calculation.js';
import {catalog} from './simulation-profile.js';

const element=id=>document.getElementById(id),params=readPageParams('stage-detail');
const settings=readGameSettings();
let database,enemies,units,map,bases=[],selected=params.get('stage')??'',crown=1;
let calculationRevision=0;
element('stage-time').value=params.get('time')|| (settings.seconds?'seconds':'frames');
element('stage-spawn-details').checked=params.get('details')==='true';
for(const key of ['clears','combo'])element('stage-xp-'+key).value=Math.max(0,Math.min(key==='combo'?100:2147483647,Math.trunc(Number(params.get(key)))||0));
element('stage-xp-okame').checked=params.get('okame')==='true';

function saveState(){
  const state=new URLSearchParams({crown:String(crown),stage:selected,time:element('stage-time').value,details:String(element('stage-spawn-details').checked)});
  for(const key of ['clears','combo'])state.set(key,element('stage-xp-'+key).value);
  state.set('okame',String(element('stage-xp-okame').checked));
  writePageParams('stage-detail',state);
}
async function renderCalculations(visible){
  const revision=++calculationRevision;
  const condition={clears:Number(element('stage-xp-clears').value),combo:Number(element('stage-xp-combo').value),okame:Number(element('stage-xp-okame').checked),studyLevel:settings.studyLevel,treasure:settings.studyTreasureBonus};
  element('stage-xp-profile').textContent='勉強力Lv'+condition.studyLevel+' / お宝＋'+condition.treasure+'%';
  try{
    if(database.gameVersion!==catalog.version)throw Error('DBとXP計算の対応版が一致しません。');
    const materialDrops=map.materials?visible.map(stage=>({count:map.materials.counts[stage.index],multiplier:map.materials.multipliers[crown-1],miss:map.materials.miss,weights:map.materials.weights})):[];
    const data=await calculateNative({legendExperience:visible.map(stage=>({base:stage.xp,...condition})),materialDrops});
    if(revision!==calculationRevision)return;
    for(const [index,stage] of visible.entries()){
      const output=data.legendExperience[index].stages;
      const target=element('stage-output').querySelector('[data-stage-experience="'+stage.id+'"]');
      target.textContent=formatNumber(output[4]);target.title=['基礎×9','繰返し減衰','勉強力・お宝','コンボ','おかめ'].map((label,index)=>label+'：'+formatNumber(output[index])).join('\n');
      element('stage-sheet-'+stage.id).querySelector('[data-stage-xp-detail]').textContent=target.title.replaceAll('\n',' / ');
      if(map.materials){
        const plan=data.materialDrops[index],materials={...plan,items:map.materials.items.map(item=>({...item,...plan.items[item.slot]}))};
        element('stage-rewards-'+stage.id).innerHTML=stageRewardsHtml(database,stage,units,map,crown,materials);
      }
    }
  }catch(error){if(revision===calculationRevision)for(const node of element('stage-output').querySelectorAll('[data-stage-experience]'))node.textContent=error.message;}
}
function sourceHtml(stage){
  const row=(label,value)=>'<tr><th>'+label+'</th><td><code>'+escapeHtml(JSON.stringify(value))+'</code></td></tr>';
  return '<details class="stage-native-source"><summary>計算内訳・元データ</summary><div data-stage-xp-detail></div><div>'+escapeHtml(stage.source)+'</div><table class="stage-sheet"><tbody>'+row('設定',stage.rawSettings)+row('ヘッダー',stage.rawHeader)+row('報酬 '+map.source+' : '+stage.metadataRow,stage.rawRewards)+row('報酬モード / 末尾値',[stage.rewardMode,stage.rewardOnce])+(map.materials?row('開発素材 '+map.materials.source+' : '+map.materials.sourceRow,map.materials.raw):'')+'</tbody></table><div class="db-meta">報酬の比較値は最終取得確率ではありません。</div><div class="db-table-wrap"><table class="stage-sheet"><thead><tr><th>元行</th><th>読込後の14整数</th></tr></thead><tbody>'+stage.spawns.map(spawn=>row(spawn.sourceRow,spawn.native)).join('')+'</tbody></table></div></details>';
}
function render(){
  settings.seconds=element('stage-time').value==='seconds';
  element('stage-crown').innerHTML=map.stars.map((_,index)=>'<button type="button" data-crown="'+(index+1)+'" aria-label="'+(index+1)+'冠" aria-pressed="'+(crown===index+1)+'"><img src="/icons/stages/crown-'+(index<crown?'on':'off')+'.png" alt="" width="25" height="24"><span>'+(index+1)+'</span></button>').join('');
  element('stage-crown-rate').textContent=formatNumber(map.stars[crown-1])+'%';
  const visible=selected===''?bases:bases.filter(stage=>String(stage.index)===selected);
  element('stage-visible-count').textContent=map.key+' / '+visible.length+'ステージ / '+crown+'冠';
  element('stage-map-info').innerHTML=stageRulesHtml(database,{index:-1},map,crown,units,settings.seconds);
  element('stage-output').innerHTML=visible.map(stage=>'<section class="stage-entry" id="stage-sheet-'+stage.id+'"><div class="stage-heading"><h2>'+(stage.index+1)+'. '+escapeHtml(stage.name)+'</h2><button type="button" data-stage-capture="'+stage.id+'">画像保存</button></div>'+stageSummaryHtml(stage,map,crown,settings)+stageSpawnsHtml(stage,map,crown,enemies,settings,{details:element('stage-spawn-details').checked})+'<div id="stage-rewards-'+stage.id+'">'+stageRewardsHtml(database,stage,units,map,crown)+'</div>'+sourceHtml(stage)+'</section>').join('');
  renderCalculations(visible);
  for(const button of element('stage-navigation').querySelectorAll('[data-stage-choice]'))button.setAttribute('aria-current',button.dataset.stageChoice===selected?'page':'false');
  saveState();
}
function selectStage(value){selected=value;render();element('main').scrollTop=0;}
element('stage-navigation').addEventListener('click',event=>{const button=event.target.closest('[data-stage-choice]');if(button)selectStage(button.dataset.stageChoice);});
element('stage-crown').addEventListener('click',event=>{const button=event.target.closest('[data-crown]');if(button){crown=Number(button.dataset.crown);render();}});
for(const id of ['stage-time','stage-spawn-details','stage-xp-clears','stage-xp-combo','stage-xp-okame'])element(id).addEventListener('change',()=>{if(map)render();});
window.addEventListener('kbcs:simulation-change',event=>{Object.assign(settings,event.detail);if(map)render();});
bindDetailNavigation('enemy-detail','/pages/tunit-detail/',(target,link)=>{
  const section=link.closest('.stage-entry'),row=link.closest('[data-stage-spawn]');
  const spawn=section&&row?bases.find(stage=>'stage-sheet-'+stage.id===section.id)?.spawns[Number(row.dataset.stageSpawn)]:null;
  const factor=(map?.stars[crown-1]??100)/100;
  return new URLSearchParams(spawn?{health:spawn.health*factor,attack:spawn.attack*factor}:{});
});
element('stage-output').addEventListener('click',async event=>{
  const button=event.target.closest('[data-stage-capture]');if(!button)return;
  button.disabled=true;
  try{await saveElementImage(element('stage-sheet-'+button.dataset.stageCapture),button.dataset.stageCapture+'-'+crown+'crown');element('stage-message').textContent='画像を保存しました。';}
  catch(error){element('stage-message').textContent=error.message;}
  finally{button.disabled=false;}
});
async function load(){
  element('stage-retry').hidden=true;
  try{
    [database,enemies,units]=await Promise.all([loadStageDatabase(),loadEnemyDatabase(),loadUnitDatabase()]);
    const route=resolveStageRoute(database,params);map=route.map;
    bases=await loadStageMap(database,map.key);
    selected=route.selected?String(bases.find(stage=>stage.id===route.selected).index):'';
    crown=Math.max(1,Math.min(map.stars.length,Math.trunc(Number(params.get('crown')))||1));
    document.title=map.name+' | KBCS';element('stage-title').textContent=map.key+' '+map.name;
    element('stage-version').textContent='JP データv'+database.gameVersion;
    const index=database.maps.findIndex(value=>value.key===map.key);
    element('stage-navigation').innerHTML='<div class="db-toolbar">'+[[database.maps[index-1],'前'],[database.maps[index+1],'次']].map(([value,label])=>value?'<a href="'+stageMapUrl(value,crown)+'">'+label+'のマップ</a>':'').join('')+'</div><div class="workspace-stage-list"><button type="button" data-stage-choice="">すべて（'+bases.length+'）</button>'+bases.map(stage=>'<button type="button" data-stage-choice="'+stage.index+'">'+(stage.index+1)+'. '+escapeHtml(stage.name)+'</button>').join('')+'</div>';
    element('stage-status').hidden=true;element('stage-content').hidden=false;render();
  }catch(error){element('stage-status').hidden=false;element('stage-status').textContent=error.message;element('stage-retry').hidden=false;}
}
element('stage-retry').addEventListener('click',load);load();

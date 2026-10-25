import {catalog,deriveSimulationSettings} from './simulation-profile.js';
import {readSimulationProfile,writeSimulationProfile} from './simulation-store.js';
import {readGameSettings} from './src/shared/browser/game-settings.js';
import {escapeHtml} from './src/shared/game/database-view.js';

const campaigns=['日本編','未来編','宇宙編'];
const normalized=text=>String(text).normalize('NFKC').toLocaleLowerCase().replace(/\s+/g,'');
const input=(value,max,label,attributes,min=0)=>'<input type="number" min="'+min+'" max="'+max+'" step="1" value="'+value+'" aria-label="'+escapeHtml(label)+'" '+attributes+'>';

export function createSimulationSettings(host,options={}){
  let profile=options.profile??readSimulationProfile(readGameSettings());
  const root=document.createElement('div');root.className='simulation-settings';
  const facilityRows=catalog.facilities.map(item=>'<div class="simulation-facility" data-facility-row="'+item.id+'" data-search="'+escapeHtml(item.name+' '+item.description)+'"><div class="simulation-facility-name" title="'+escapeHtml(item.description)+'"><img src="'+item.icon+'" alt="" width="28" height="28"><span>'+escapeHtml(item.name)+'</span></div><div class="simulation-level"><span>Lv</span>'+input(profile.facilities[item.id].level,item.maxLevel,item.name+'のレベル','data-facility="'+item.id+'" data-part="level"',1)+(item.maxPlus?'<span>＋</span>'+input(profile.facilities[item.id].plus,item.maxPlus,item.name+'の＋レベル','data-facility="'+item.id+'" data-part="plus"'):'')+'</div></div>').join('');
  const treasureSections=[];
  for(let campaign=0;campaign<3;campaign++)for(let chapter=1;chapter<=3;chapter++){
    const name=campaigns[campaign]+chapter+'章';
    treasureSections.push('<details class="simulation-chapter" data-campaign="'+campaign+'" data-chapter="'+chapter+'"><summary>'+name+'<span data-chapter-count></span></summary>'+catalog.treasures.filter(item=>item.campaign===campaign&&item.chapter===chapter).map(item=>'<label class="simulation-treasure" data-treasure-row="'+item.id+'" data-search="'+escapeHtml(name+' '+item.name+' '+item.description)+'"><span title="'+escapeHtml(item.description)+'">'+escapeHtml(item.name)+'</span><span>'+input(profile.treasures[item.id],100,name+' '+item.name+'の発動率','data-treasure="'+item.id+'"')+'%</span></label>').join('')+'</details>');
  }
  root.innerHTML='<details class="simulation-section" id="simulation-facilities"><summary>施設Lv<span>10項目</span></summary><input type="search" data-facility-filter aria-label="施設を絞り込み" placeholder="施設名・効果で絞り込み"><div class="simulation-actions"><button type="button" data-preset="facility-max">表示中を最大</button><button type="button" data-preset="facility-min">表示中を初期Lv</button></div><div class="simulation-facility-list">'+facilityRows+'</div></details>'+
    '<details class="simulation-section" id="simulation-treasures"><summary>お宝<span data-treasure-count>99項目</span></summary><input type="search" data-treasure-filter aria-label="お宝を絞り込み" placeholder="お宝名・効果で絞り込み"><div class="simulation-filters"><select data-campaign-filter aria-label="お宝の編"><option value="">すべての編</option>'+campaigns.map((name,index)=>'<option value="'+index+'">'+name+'</option>').join('')+'</select><select data-chapter-filter aria-label="お宝の章"><option value="">すべての章</option><option value="1">1章</option><option value="2">2章</option><option value="3">3章</option></select></div><label class="simulation-incomplete"><input type="checkbox" data-incomplete>100%未満のみ</label><div class="simulation-actions"><button type="button" data-preset="treasure-max">絞込分を100%</button><button type="button" data-preset="treasure-min">絞込分を0%</button></div>'+treasureSections.join('')+'<p data-treasure-empty hidden>該当するお宝はありません。</p></details><p class="simulation-save-state" role="status" aria-live="polite"></p><details class="simulation-scope"><summary>現在の反映範囲</summary><p>体力・攻撃力・再生産・敵の獲得金・クリスタル・仮面は現在の表へ反映します。属性果実・土台・装飾はダメージ計算へ反映します。勉強力・経験値のお宝はステージXPへ反映します。ほかの項目も保存し、戦闘や統率力などの処理を追加するときに使います。</p><p>定義：JP '+catalog.version+'。旧合計値は1章から順に配分して引き継ぎます。</p></details>';
  if(options.onChange)root.querySelector('.simulation-scope').remove();
  host.append(root);
  const cannon=document.createElement('details');cannon.className='simulation-section simulation-cannon';
  const cannonNames=['なし','スロウ砲','鉄壁砲','かみなり砲','水鉄砲','エンジェル砲','キャノンブレイク砲','呪い砲'];
  cannon.innerHTML='<summary>土台・装飾</summary>'+[['base','土台'],['decoration','装飾']].map(([part,label])=>'<div class="simulation-cannon-row"><label>'+label+'<select data-cannon="'+part+'" data-part="id" aria-label="'+label+'">'+cannonNames.map((name,index)=>'<option value="'+index+'">'+name+'</option>').join('')+'</select></label><label>Lv<input type="number" min="0" max="20" step="1" data-cannon="'+part+'" data-part="level" aria-label="'+label+'Lv"></label></div>').join('');
  root.querySelector('#simulation-facilities').after(cannon);
  const status=root.querySelector('.simulation-save-state');
  const visible=selector=>[...root.querySelectorAll(selector)].filter(row=>!row.hidden&&!row.closest('.simulation-chapter[hidden]'));
  const dispatch=()=>window.dispatchEvent(new CustomEvent('kbcs:simulation-change',{detail:deriveSimulationSettings(profile)}));
  const save=()=>{
    const saved=options.onChange?(options.onChange(profile),true):writeSimulationProfile(profile);status.textContent=options.onChange?'':saved?'保存済み':'保存できませんでした';
    if(saved&&!options.onChange)dispatch();
    updateCounts();
  };
  function updateCounts(){
    for(const section of root.querySelectorAll('.simulation-chapter')){
      const rows=[...section.querySelectorAll('[data-treasure-row]')].filter(row=>!row.hidden);
      section.querySelector('[data-chapter-count]').textContent=rows.length+'項目';
    }
  }
  function filterTreasures(){
    const query=normalized(root.querySelector('[data-treasure-filter]').value),campaign=root.querySelector('[data-campaign-filter]').value,chapter=root.querySelector('[data-chapter-filter]').value,incomplete=root.querySelector('[data-incomplete]').checked;
    let count=0;
    for(const section of root.querySelectorAll('.simulation-chapter')){
      const matches=(!campaign||section.dataset.campaign===campaign)&&(!chapter||section.dataset.chapter===chapter);
      let sectionCount=0;
      for(const row of section.querySelectorAll('[data-treasure-row]')){
        row.hidden=!(matches&&normalized(row.dataset.search).includes(query)&&(!incomplete||profile.treasures[row.dataset.treasureRow]<100));
        if(!row.hidden)sectionCount++;
      }
      section.hidden=!sectionCount;count+=sectionCount;
      if(sectionCount&&(query||campaign||chapter||incomplete))section.open=true;
    }
    root.querySelector('[data-treasure-count]').textContent=count+' / 99項目';root.querySelector('[data-treasure-empty]').hidden=count>0;updateCounts();
  }
  root.addEventListener('input',event=>{
    const target=event.target;
    if(target.matches('[data-facility-filter]')){const query=normalized(target.value);for(const row of root.querySelectorAll('[data-facility-row]'))row.hidden=!normalized(row.dataset.search).includes(query);return;}
    if(target.matches('[data-treasure-filter],[data-campaign-filter],[data-chapter-filter],[data-incomplete]')){filterTreasures();return;}
    if(!target.matches('[data-facility],[data-treasure],[data-cannon]')||target.value===''||!target.checkValidity())return;
    if(target.dataset.cannon)profile.cannon[target.dataset.cannon][target.dataset.part]=Number(target.value);
    else if(target.dataset.treasure)profile.treasures[target.dataset.treasure]=Number(target.value);
    else profile.facilities[target.dataset.facility][target.dataset.part]=Number(target.value);
    save();
  });
  root.addEventListener('change',event=>{
    if(!event.target.matches('[data-facility],[data-treasure],[data-cannon]')||event.target.checkValidity())return;
    const target=event.target;target.value=target.dataset.cannon?profile.cannon[target.dataset.cannon][target.dataset.part]:target.dataset.treasure?profile.treasures[target.dataset.treasure]:profile.facilities[target.dataset.facility][target.dataset.part];
  });
  root.addEventListener('click',event=>{
    const button=event.target.closest('[data-preset]');if(!button)return;
    const maximum=button.dataset.preset.endsWith('max');
    if(button.dataset.preset.startsWith('facility'))for(const row of visible('[data-facility-row]')){
      const item=catalog.facilities.find(item=>item.id===row.dataset.facilityRow);profile.facilities[item.id]={level:maximum?item.maxLevel:1,plus:maximum?item.maxPlus:0};
    }else for(const row of visible('[data-treasure-row]'))profile.treasures[row.dataset.treasureRow]=maximum?100:0;
    fill();save();filterTreasures();
  });
  function fill(){for(const field of root.querySelectorAll('[data-facility],[data-treasure],[data-cannon]'))field.value=field.dataset.cannon?profile.cannon[field.dataset.cannon][field.dataset.part]:field.dataset.treasure?profile.treasures[field.dataset.treasure]:profile.facilities[field.dataset.facility][field.dataset.part];}
  if(!options.onChange)window.addEventListener('storage',event=>{if(event.key==='kbcs:simulation-profile'){profile=readSimulationProfile();fill();filterTreasures();dispatch();}});
  fill();updateCounts();
  return {open(){root.querySelector('#simulation-treasures').open=true;root.scrollIntoView({block:'nearest'});root.querySelector('[data-treasure-filter]').focus();}};
}

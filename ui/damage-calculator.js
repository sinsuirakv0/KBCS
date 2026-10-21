import {calculateNative} from './native-calculation.js';
import {catalog} from './simulation-profile.js';
import {loadEnemyDatabase} from './src/shared/game/enemies.js';
import {escapeHtml,formatNumber,propertyIconHtml} from './src/features/units/view.js';

const specialFlags=[['witch-killer','witch',32,'魔女'],['eva-killer','eva',64,'使徒'],['colossus','colossus',128,'超生命体'],['behemoth','behemoth',256,'超獣'],['sage','sage',512,'超賢者'],['villain','villain',1024,'怪人']];
const stages=['元の一撃','クリティカル','攻撃力上昇','撃破後の強化玉','弱体化','渾身','めっぽう強い','超ダメージ／打たれ強い','極ダメージ／超打たれ強い','魔女','使徒','超生命体','超獣','超賢者','怪人特効','加算玉／攻撃耐性','軽減玉','土台','装飾','メタル','無効'];

export function createDamageCalculator(database,unit,readCurrent){
  const panel=document.createElement('details');panel.id='unit-damage-panel';panel.className='unit-related';
  panel.innerHTML='<summary>ダメージ・被ダメージ</summary><div class="unit-damage-results" role="status"></div><details><summary>計算の内訳</summary><div class="unit-damage-stages db-table-wrap"></div></details><details><summary>計算対象</summary><p class="db-meta">各段の直接攻撃を個別に整数計算。波動・烈波・爆波の追加発生、バリア・悪魔シールド・回避・生き残り・再生は別の命中／状態処理です。メタルキラーは入力した現在HPに対する有効な1撃を表示します。</p></details>';
  document.getElementById('unit-growth-panel').before(panel);
  const host=document.createElement('details');host.className='simulation-section unit-damage-settings';
  host.innerHTML='<summary>ダメージ計算の条件</summary><label>形態<select data-damage-form>'+unit.forms.map(form=>'<option value="'+form.code+'">'+escapeHtml(form.name)+'</option>').join('')+'</select></label><label>相手を検索<input type="search" list="damage-enemy-list" data-enemy-query placeholder="敵名・ID" autocomplete="off"></label><datalist id="damage-enemy-list"></datalist><button type="button" data-apply-enemy>相手の属性を適用</button><div class="unit-damage-targets">'+database.targets.map(target=>'<label title="'+escapeHtml(target.label)+'"><input type="checkbox" data-target="'+target.key+'">'+propertyIconHtml(database,target.key,target.label,18,false)+'<span>'+escapeHtml(target.label)+'</span></label>').join('')+'</div><div class="unit-damage-specials">'+specialFlags.map(([key,target,,label])=>'<label><input type="checkbox" data-special="'+target+'">'+(database.propertyAtlas.icons[key]?propertyIconHtml(database,key,label,18,false):'')+escapeHtml(label)+'</label>').join('')+'</div><label><input type="checkbox" data-castle>城</label><label><input type="checkbox" data-cursed>古代の呪い</label><label><input type="checkbox" data-strengthen>攻撃力上昇を発動</label><label><input type="checkbox" data-critical>クリティカルを発動</label><label><input type="checkbox" data-savage>渾身の一撃を発動</label><label>弱体化後の攻撃力（%）<input type="number" data-weaken min="0" max="100" step="1" value="100"></label><label>相手の一撃<input type="number" data-incoming min="0" max="100000000" step="1" value="1000"></label><label data-target-hp-label>相手の現在HP<input type="number" data-target-hp min="1" max="10000000" step="1" value="100000"></label><label><input type="checkbox" data-incoming-critical>相手のクリティカル</label><label>相手の攻撃<select data-incoming-type><option value="normal">直接攻撃</option><option value="wave">波動</option><option value="surge">烈波</option><option value="blast">爆波</option><option value="toxic">毒撃</option></select></label><label data-poison-label hidden>毒撃（最大HPの%）<input type="number" data-poison min="1" max="100" step="1" value="20"></label>';
  document.getElementById('workspace-right').querySelector('.workspace-panel-content').prepend(host);
  const outline=document.querySelector('.workspace-outline[aria-label="キャラ詳細の項目"]');
  const link=document.createElement('a');link.href='#unit-damage-panel';link.textContent='ダメージ計算';link.addEventListener('click',()=>{panel.open=true;});outline?.prepend(link);
  const results=panel.querySelector('.unit-damage-results'),trace=panel.querySelector('.unit-damage-stages');
  let revision=0,enemies,lookup;
  const storageKey='kbcs:damage:'+unit.id;
  const controls=[...host.querySelectorAll('input,select')];
  for(const field of controls){const [key,value]=Object.entries(field.dataset)[0];field.name=key+(value?':'+value:'');}
  let saved={};try{saved=JSON.parse(sessionStorage.getItem(storageKey)||'{}');}catch{}
  for(const field of controls)if(saved[field.name]!=null){if(field.type==='checkbox')field.checked=saved[field.name]===true;else if(field.tagName!=='SELECT'||[...field.options].some(option=>option.value===saved[field.name]))field.value=saved[field.name];}
  const save=()=>{try{sessionStorage.setItem(storageKey,JSON.stringify(Object.fromEntries(controls.map(field=>[field.name,field.type==='checkbox'?field.checked:field.value]))));}catch{}};
  const selected=selector=>host.querySelector(selector).checked;
  const number=selector=>Number(host.querySelector(selector).value);
  const formSelect=host.querySelector('[data-damage-form]');
  if(!saved.damageForm)formSelect.value=readCurrent().form.code;
  async function loadEnemies(){
    if(enemies)return;
    const data=await loadEnemyDatabase();enemies=data.enemies;
    host.querySelector('datalist').innerHTML=enemies.map(enemy=>'<option value="'+escapeHtml(enemy.id+' '+enemy.name)+'"></option>').join('');
  }
  host.addEventListener('toggle',()=>{if(host.open)loadEnemies().catch(error=>{results.textContent=error.message;});});
  host.querySelector('[data-apply-enemy]').addEventListener('click',async()=>{
    try{
      await loadEnemies();const query=host.querySelector('[data-enemy-query]').value.trim();
      const enemy=enemies.find(enemy=>query===String(enemy.id)||query===enemy.name||query===enemy.id+' '+enemy.name);
      if(!enemy){results.textContent='候補から相手を選択してください。';return;}
      for(const input of host.querySelectorAll('[data-target]'))input.checked=enemy.attributes.includes(input.dataset.target);
      for(const input of host.querySelectorAll('[data-special]'))input.checked=enemy.attributes.includes(input.dataset.special)||enemy.species.includes(input.dataset.special)||enemy.abilities.some(ability=>ability.key===input.dataset.special);
      lookup=enemy;save();panel.open=true;update();
    }catch(error){results.textContent=error.message;}
  });
  host.addEventListener('input',event=>{save();if(event.target.matches('[data-enemy-query]'))return;if(event.target.matches('[data-target],[data-special]'))lookup=null;panel.open=true;update();});
  panel.addEventListener('toggle',()=>{if(panel.open){host.open=true;update();}});
  function request(profile,current,incoming=false){
    const abilities=profile.form.abilities,ability=key=>abilities.find(value=>value.key===key);
    const targets=[...host.querySelectorAll('[data-target]:checked')].map(input=>input.dataset.target);
    const cursed=selected('[data-cursed]')&&(ability('curse-immune')?.resistance||0)<100;
    const matches=!selected('[data-castle]')&&!cursed&&targets.some(key=>profile.form.targets.includes(key));
    const combos=current.combos||{},hit={abilities:0,weaken:incoming||(ability('weaken-immune')?.resistance||0)>=100?100:number('[data-weaken]'),
      fruit:matches?Math.max(0,...targets.filter(key=>profile.form.targets.includes(key)).map(key=>current.settings.fruitByTarget?.[key]||0)):0,
      castle:Number(!incoming&&selected('[data-castle]')),castleBreaker:Number(Boolean(ability('castle'))),
      metal:Number(incoming?Boolean(ability('metal-body')):targets.includes('metal')),
      blocked:Number(!incoming&&!selected('[data-castle]')&&Boolean(ability('target-only'))&&!matches),
      strongCombo:combos.strong||0,massiveCombo:combos.massive||0,resistantCombo:combos.resistant||0,
      witchCombo:combos['witch-killer']||0,evaCombo:combos['eva-killer']||0,villainRate:combos.villain||0,
      behemothRate:catalog.combatParameters[incoming?'battle_super_beast_hunter_df':'battle_super_beast_hunter'],
      sageRate:catalog.combatParameters[incoming?'battle_super_sage_hunter_damage2':'battle_super_sage_hunter_damage1']};
    if(matches)for(const [key,flag] of [['strong',1],['massive',2],['extreme',4],['resistant',8],['super-resistant',16]])if(ability(key))hit.abilities|=flag;
    for(const [key,target,flag] of specialFlags)if(ability(key)&&selected('[data-special="'+target+'"]'))hit.abilities|=flag;
    if(combos.villain>0&&selected('[data-special="villain"]'))hit.abilities|=1024;
    if(incoming){
      const type=host.querySelector('[data-incoming-type]').value;
      hit.attack=type==='toxic'?0:number('[data-incoming]');hit.rawAttack=0;hit.critical=Number(selected('[data-incoming-critical]'));
      hit.resistance=type==='toxic'?0:ability(type+'-immune')?.resistance||0;
      const base=catalog.cannonParts.base.find(part=>part.id===current.settings.cannonBase);
      const decoration=catalog.cannonParts.decoration.find(part=>part.id===current.settings.cannonDecoration);
      hit.baseReduction=type!=='toxic'&&base&&targets.includes(base.effect)?base.rates[current.settings.cannonBaseLevel]||0:0;
      hit.decorationReduction=type!=='toxic'&&decoration?.effect===type?decoration.rates[current.settings.cannonDecorationLevel]||0:0;
      hit.immune=Number(type==='wave'&&Boolean(ability('wave-block'))||hit.resistance>=100);
    }else{
      hit.strengthen=selected('[data-strengthen]')&&ability('strengthen')?ability('strengthen').power-100+(combos.strengthen||0):0;
      hit.savage=ability('savage')?.power?ability('savage').power-100:0;
    }
    return hit;
  }
  async function update(){
    if(!panel.open)return;
    const version=++revision;
    try{
      const current=readCurrent(),form=unit.forms.find(form=>form.code===formSelect.value)||current.form;
      const profile=current.calculate(form),ability=key=>profile.form.abilities.find(value=>value.key===key);
      for(const [selector,key] of [['[data-strengthen]','strengthen'],['[data-critical]','critical'],['[data-savage]','savage']])host.querySelector(selector).disabled=!ability(key);
      host.querySelector('[data-weaken]').disabled=(ability('weaken-immune')?.resistance||0)>=100;
      const type=host.querySelector('[data-incoming-type]').value;
      host.querySelector('[data-poison-label]').hidden=type!=='toxic';
      const checks=['[data-weaken]',type==='toxic'?'[data-poison]':'[data-incoming]'];
      if(selected('[data-target="metal"]')&&ability('metal-killer')&&!selected('[data-castle]'))checks.push('[data-target-hp]');
      if(checks.map(selector=>host.querySelector(selector)).some(input=>!input.disabled&&(!input.checkValidity()||input.value===''))){results.textContent='入力値を確認してください。';return;}
      const hit=request(profile,current),critical=Math.min(100,(ability('critical')?.probability||0)+(ability('critical')?.probability?current.combos?.critical||0:0)),savage=ability('savage')?.probability||0;
      const unitDamage=profile.stats.attacks.map((attack,index)=>({hit:{...hit,attack,rawAttack:form.attacks[index]},criticalChance:profile.form.abilityHits?.[index]===0?0:critical,savageChance:profile.form.abilityHits?.[index]===0?0:savage,forceCritical:selected('[data-critical]'),forceSavage:selected('[data-savage]')}));
      const incoming=request(profile,current,true);
      const enemyDamage=[{hit:incoming,criticalChance:incoming.critical?100:0,savageChance:0,forceCritical:false,forceSavage:false}];
      const metalPercent=ability('metal-killer')?.percent||0;
      const metalActive=hit.metal&&!hit.blocked&&!hit.castle&&metalPercent>0;
      host.querySelector('[data-target-hp-label]').hidden=!metalActive;
      const metalHit=profile.stats.attacks.findIndex((_,index)=>profile.form.abilityHits?.[index]!==0);
      const percentages=metalActive&&metalHit>=0?[metalPercent]:[];
      const metalKiller=percentages.length?[{hp:number('[data-target-hp]'),percentages}]:[];
      const decoration=catalog.cannonParts.decoration.find(part=>part.id===current.settings.cannonDecoration);
      const poison=type==='toxic'?[{maxHp:profile.stats.hp,percent:number('[data-poison]'),resistance:ability('toxic-immune')?.resistance||0,decorationReduction:decoration?.effect==='toxic'?decoration.rates[current.settings.cannonDecorationLevel]||0:0,immune:Number((ability('toxic-immune')?.resistance||0)>=100)}]:[];
      const response=await calculateNative({unitDamage,enemyDamage,metalKiller,poison});if(version!==revision)return;
      const outgoing=response.unitDamage,received=type==='toxic'?response.poison[0].damage:response.enemyDamage[0].selected.damage;
      const extra=response.metalKiller[0]?.damage.reduce((sum,value)=>sum+value,0)||0;
      const total=key=>outgoing.reduce((sum,row)=>sum+(key==='selected'?row.selected.damage:row[key]),0),cycle=profile.stats.attackCycle;
      const row=(label,value)=>'<tr><th>'+label+'</th><td>'+formatNumber(value)+'</td></tr>';
      results.innerHTML='<div class="unit-damage-heading">'+escapeHtml(form.name)+(lookup?' / '+escapeHtml(lookup.name):'')+'</div><table class="db-table"><tbody>'+row('体力',profile.stats.hp)+row('通常の直接ダメージ',total('normal'))+row('選択条件の直接ダメージ',total('selected'))+row('直接ダメージの期待値',total('expected'))+row('選択条件の直接DPS',cycle>0?total('selected')*30/cycle:null)+row('直接DPSの期待値',cycle>0?total('expected')*30/cycle:null)+(metalActive?row('メタルキラー（有効な1撃）',extra)+row('有効な1撃の合計',(outgoing[metalHit]?.selected.damage||0)+extra):'')+row('受ける一撃',received)+'</tbody></table>';
      trace.innerHTML=type==='toxic'?'<table class="db-table"><tbody>'+['味方の最大HP','最大HPの割合・最低1','毒撃耐性・最低1','毒撃用の装飾'].map((label,index)=>'<tr><th>'+label+'</th><td>'+formatNumber(response.poison[0].stages[index])+'</td></tr>').join('')+'</tbody></table>':'<table class="db-table"><thead><tr><th>段階</th>'+outgoing.map((_,index)=>'<th>第'+(index+1)+'撃</th>').join('')+'<th>被ダメージ</th></tr></thead><tbody>'+stages.map((label,index)=>'<tr><th>'+label+'</th>'+outgoing.map(row=>'<td>'+formatNumber(row.selected.stages[index])+'</td>').join('')+'<td>'+formatNumber(response.enemyDamage[0].selected.stages[index])+'</td></tr>').join('')+'</tbody></table>';
    }catch(error){if(version===revision)results.textContent=error.message;}
  }
  return {update};
}

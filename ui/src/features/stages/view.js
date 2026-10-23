import {escapeHtml,formatNumber,formatTime} from '../../shared/game/database-view.js';
import {enemyImageHtml,enemyAttributesHtml} from '../../shared/game/enemy-view.js';
import {imageHtml} from '../../shared/game/unit-view.js';
import {enemyDetailUrl,calculateEnemyStats} from '../../shared/game/enemy-stats.js';
import {rarityNames} from '../../shared/game/unit-stats.js';
import {applicableLimits,effectiveSpawn,stageDetailUrl} from './model.js';

const decimal=new Intl.NumberFormat('ja-JP',{maximumFractionDigits:3});
const percent=value=>decimal.format(value)+'%';
const row=(label,value)=>'<tr><th scope="row">'+label+'</th><td>'+value+'</td></tr>';
const table=body=>'<table class="stage-sheet"><tbody>'+body+'</tbody></table>';
export function stageSummaryHtml(stage,map,crown=1,settings={seconds:true},enemies){
  const seconds=settings.seconds,spawn=stage.spawns.find(spawn=>spawn.enemy===stage.enemyCastle),enemy=spawn&&enemies?.enemies[spawn.enemy],options=spawn?{...settings,...effectiveSpawn(spawn,map,crown)}:settings;
  const castle=enemy?formatNumber(calculateEnemyStats(enemy,options).hp)+'<small> <a href="'+escapeHtml(enemyDetailUrl(enemy,options))+'">敵ID '+enemy.id+'</a></small>':(stage.castleHealth==null?'—':formatNumber(stage.castleHealth));
  const wideRow=(label,value)=>'<tr><th scope="row">'+label+'</th><td colspan="3">'+value+'</td></tr>';
  return '<table class="stage-sheet" aria-label="'+escapeHtml(stage.name)+'"><tbody><tr><th>統率力</th><td class="stage-number">'+formatNumber(stage.energy)+'</td><th>敵最大数</th><td class="stage-number">'+(stage.maxEnemies==null?'—':formatNumber(stage.maxEnemies))+'</td></tr><tr><th>城体力</th><td class="stage-number">'+(stage.timeLimit?'スコア制':castle)+'</td><th>ステージ幅</th><td class="stage-number">'+(stage.width==null?'—':formatNumber(stage.width))+'</td></tr><tr><th>難易度</th><td>'+(stage.difficulty==null?'—':'★'+stage.difficulty)+'</td><th>コンテニュー</th><td>'+(stage.width==null?'—':stage.noContinue?'不可':'可')+'</td></tr>'+
    '<tr><th>城バリア</th><td>'+(stage.width==null?'—':stage.bossGuard?'あり':'なし')+'</td><th>制限時間</th><td>'+(stage.width==null?'—':stage.timeLimit?formatTime(stage.timeLimit,seconds):'なし')+'</td></tr>'+wideRow('敵生産間隔',stage.spawnInterval?.every(Number.isFinite)?[...new Set(stage.spawnInterval)].map(value=>formatTime(value,seconds)).join('〜'):'—')+wideRow('XP','<span data-stage-experience="'+stage.id+'"></span>')+
    (stage.variants?wideRow('抽選候補',stage.variants.length+'パターン / '+escapeHtml(stage.patternLabel||'')):'')+(stage.energy==null?wideRow('未収録の項目','敵出現の定義だけが残っているステージです。統率力・報酬などは推測せず未収録として表示します。'):'')+'</tbody></table>';
}
function unitLink(units,id,formIndex){
  const unit=units.units.find(unit=>unit.id===id),form=unit?.forms.find(form=>form.index===formIndex)||unit?.forms[0];
  return unit?'<a href="/pages/unit-detail/?id='+id+'&form='+(form?.code||'f')+'">'+imageHtml(units,form,32,25)+escapeHtml(form.name)+'</a>':'ID '+id;
}
function limitHtml(limit,units){
  const parts=[];
  if(limit.rarities)parts.push('レア度：'+rarityNames.filter((_,index)=>limit.rarities&(1<<index)).join('・'));
  if(limit.maxUnits)parts.push('同時出撃 '+limit.maxUnits+'体まで');
  if(limit.slots)parts.push(limit.slots===1?'編成1ページ目のみ':'編成ページ制限 '+limit.slots);
  if(limit.minCost||limit.maxCost)parts.push('生産コスト '+(limit.minCost?formatNumber(limit.minCost)+'円以上':'')+(limit.minCost&&limit.maxCost?'・':'')+(limit.maxCost?formatNumber(limit.maxCost)+'円以下':''));
  if(limit.group)parts.push(escapeHtml(limit.group.label)+'（'+(limit.group.type===2?'使用不可':'使用可能')+'）：'+limit.group.units.map(id=>unitLink(units,id)).join(' / '));
  return parts.join(' / ')||'指定なし';
}
function conditionHtml(condition,database){
  if(condition.message)return escapeHtml(condition.message);
  const codes=condition.group?.condition||[condition.code];
  const values=codes.map(code=>{const value=Math.abs(code),type=Math.floor(value/100000),map=database.maps.find(map=>map.nativeId===value%100000);return map?'<a href="/pages/stage-search/?q='+map.key+'">'+escapeHtml(map.name)+'</a> '+(code<0?'未達成':'クリア')+(condition.group?.stage!=null?'（ステージ'+(condition.group.stage+1)+'）':'')+(type!==1&&type!==3?' <span class="db-meta">条件区分'+type+'</span>':''):'条件ID '+code;});
  return values.join(' / ')+(condition.group?.count?'（'+condition.group.count+'条件以上）':'');
}
function ruleValueHtml(rule,seconds){
  const p=rule.parameters,rarities=values=>values.map((value,index)=>rarityNames[index]+' '+value).join(' / ');
  switch(rule.id){
    case 0:return '開始時のお金 '+formatNumber(p[0])+'円（通常の増加なし）';
    case 1:return '生産時間 '+formatTime(p[0],seconds)+'に固定';
    case 2:return rarities(p)+'体まで編成';
    case 3:return rarities(p)+'体まで生産';
    case 4:return '全キャラ '+formatNumber(p[0])+'円';
    case 5:return rarities(p)+'%（生産コスト）';
    case 6:return rarities(p)+'%（生産時間）';
    case 7:return '戦闘中の生産 合計'+p[0]+'体まで';
    case 8:return rarityNames.filter((_,index)=>p[0]&(1<<index)).join('・')+' / 生産時に追加'+p[1]+'体 / 間隔'+formatTime(p[2],seconds);
    case 9:return 'にゃんこ砲の攻撃力 '+percent(p[0]);
    case 10:return [p[0]?'味方 '+(p[0]===1?'速度'+p[1]+'に固定':percent(p[1])):'',p[2]?'敵 '+(p[2]===1?'速度'+p[3]+'に固定':percent(p[3])):''].filter(Boolean).join(' / ');
    case 12:return 'フィーバーゲージ '+formatNumber(p[1])+'Pt / 継続 '+formatTime(p[2],seconds);
    default:return '<details><summary>データ内の設定値</summary><span class="db-meta">ルールID '+rule.id+' / '+p.join(', ')+'</span></details>';
  }
}
export function stageRulesHtml(database,stage,map,crown,units,seconds,{includeMap=true}={}){
  const limits=applicableLimits(map,stage,crown).filter(limit=>includeMap||limit.stage>=0),conditions=map.conditions.filter(condition=>(includeMap||condition.minStage!=null)&&(condition.minStage==null||stage.index>=condition.minStage));
  const other=map.stars.flatMap((_,index)=>index+1===crown?[]:applicableLimits(map,stage,index+1).filter(limit=>includeMap||limit.stage>=0).map(limit=>({crown:index+1,limit})));
  const body=((includeMap||limits.length)?row('出撃制限',limits.length?limits.map(limit=>limitHtml(limit,units)).join('<br>'):'この冠の指定なし'):'')+
    (other.length?row('他の冠','<details><summary>出撃制限を確認</summary>'+other.map(({crown,limit})=>'<div>'+crown+'冠：'+limitHtml(limit,units)+'</div>').join('')+'</details>'):'')+
    (includeMap&&map.rules.length?row('特殊ルール','<details><summary>'+escapeHtml(map.ruleName||'ルールの説明')+'</summary>'+(map.ruleDescription?'<div class="stage-description">'+escapeHtml(map.ruleDescription)+'</div>':'')+'<ul>'+map.rules.map(rule=>'<li>'+escapeHtml(rule.label)+'：'+ruleValueHtml(rule,seconds)+'</li>').join('')+'</ul></details>'):'')+
    (includeMap&&map.scoreBonus?row('スコアボーナス','<strong>'+escapeHtml(map.scoreBonus.name)+'</strong><div class="stage-description">'+escapeHtml(map.scoreBonus.description)+'</div>'):'')+
    (stage.pointRules?row('イベントPt','<details><summary>'+escapeHtml(stage.pointRules.name)+'</summary>'+stage.pointRules.sections.filter(section=>section.description).map(section=>'<strong>'+escapeHtml(section.name)+'</strong><div class="stage-description">'+escapeHtml(section.description)+'</div>').join('')+'</details>'):'')+
    (conditions.length?row('表示・挑戦条件','<div class="stage-conditions">'+conditions.map(condition=>'<div class="stage-description">'+condition.kind+'：'+conditionHtml(condition,database)+'</div>').join('')+'</div>'):'')+
    (stage.bossGuard?row('城バリア','ボスが残っている間、敵城への攻撃を防ぎます。'):'')+
    (stage.levelSeal?row('Lv封印','基本Lv解放値 '+stage.levelSeal.level+' / ＋Lv解放 '+(stage.levelSeal.plus?'あり':'なし')+'<div class="db-meta">魔界編のクリア状況によって実際に使えるLvは変わります。</div>'):'')+
    (stage.ex||stage.exLottery?.length?row('連戦・EX',exLinksHtml(database,stage)):'')+
    (includeMap&&map.notes?.length?row('マップ固有の仕様','<details><summary>確認する</summary>'+map.notes.map(note=>'<p class="stage-description">'+escapeHtml(note)+'</p>').join('')+'</details>'):'');
  return body?table(body):'';
}
function exLinksHtml(database,stage){
  const direct=stage.ex?Array.from({length:Math.max(0,stage.ex.max-stage.ex.min+1)},(_,index)=>({map:stage.ex.map,nativeMap:stage.ex.nativeMap,stage:stage.ex.min+index})):[];
  const links=entries=>entries.map(entry=>{const map=database.maps.find(map=>map.key===entry.map),candidate=database.stages.find(stage=>stage.map===entry.map&&stage.index===entry.stage);return '<div>'+(candidate?'<a href="'+stageDetailUrl(candidate)+'">'+escapeHtml(map.name+' / '+candidate.name)+'</a>':'EXマップ '+entry.nativeMap+' / ステージ '+entry.stage)+'</div>';}).join('');
  return (stage.ex?'<div>直接移行 '+percent(stage.ex.chance)+'</div>'+links(direct):'')+(stage.exLottery?.length?'<div>追加抽選の候補</div>'+links(stage.exLottery):'');
}

export function stageRewardsHtml(database,stage,units,map,crown=1,materials){
  const rewardHtml=reward=>{
    const item=database.rewards[reward.id],name=item?.name||'報酬 '+reward.id;
    const image=item?.layers?.length?orbHtml(item):item?.unit!=null?unitLink(units,item.unit,item.form):item?.icon?'<img src="'+escapeHtml(database.imageBase+item.icon)+'" alt="" loading="lazy">':'';
    return '<span class="stage-reward" title="報酬ID '+reward.id+'">'+image+(item?.unit!=null?'':escapeHtml(name))+' ×'+formatNumber(reward.count)+(item?.evolution?'<span>進化権</span>':'')+'</span>';
  };
  const orbHtml=item=>'<span class="unit-orb-image" role="img" aria-label="'+escapeHtml(item.name)+'" style="width:32px;height:32px">'+item.layers.map(layer=>{const [x,y,width,height]=layer.rect,scale=32/width;return '<span class="unit-property-image" style="width:32px;height:'+height*scale+'px"><img src="'+escapeHtml(database.imageBase+layer.path)+'" alt="" loading="lazy" style="width:'+layer.width*scale+'px;height:'+layer.height*scale+'px;left:'+(-x*scale)+'px;top:'+(-y*scale)+'px"></span>';}).join('')+'</span>';
  const drops=stage.drops.map(reward=>'<div>'+(reward.chance==null?'':percent(reward.chance)+' ')+rewardHtml(reward)+'</div>').join('');
  return table(row(map?.series==='D'?'初回クリア報酬':'クリア報酬',drops||'データ内の指定なし')+(stage.orderedRewards?row('報酬の抽選','この形式は確率を数値化していません。表示はデータ内の報酬候補です。'):'')+
    (stage.scoreRewards.length?row('スコア報酬',stage.scoreRewards.map(reward=>'<div>'+formatNumber(reward.score)+'点以上 '+rewardHtml(reward)+'</div>').join('')):'')+
    (stage.clearRewards.length?row('クリア回数報酬',stage.clearRewards.map(reward=>'<div>'+reward.clear+'回目 '+rewardHtml(reward)+'</div>').join('')):'')+
    (materials?.items.length?row('城の開発素材','<details><summary>素材候補と確率</summary><div>抽選 '+materials.draws+'回 / '+crown+'冠</div><table class="stage-sheet"><thead><tr><th>素材</th><th>抽選1回</th><th>1クリアで1個以上</th><th>期待数</th></tr></thead><tbody>'+materials.items.map(item=>'<tr><td>'+rewardHtml({...item,count:1})+'</td><td>'+percent(item.chance*100)+'</td><td>'+percent(item.atLeastOne*100)+'</td><td>'+decimal.format(item.expected)+'個</td></tr>').join('')+'</tbody></table><div class="db-meta">ハズレ：抽選1回 '+percent(materials.miss*100)+' / 全抽選で素材なし '+percent(materials.none*100)+'。トレジャーレーダーの対象外です。</div></details>'):'')
  );
}
export function stageFormationHtml(stage,units){
  if(!stage.formation)return '';
  const choice=stage.formation.choices.find(choice=>choice.index===stage.formation.selected)||stage.formation.choices[0];
  if(!choice)return table(row('固定編成','編成内容は未収録です。'));
  return table(row('固定編成','<div class="stage-formation">'+choice.units.map(entry=>{const unit=units.units.find(unit=>unit.id===entry.id),form=unit?.forms.find(form=>form.index===entry.form)||unit?.forms[0];return unit?'<a href="/pages/unit-detail/?id='+entry.id+'&form='+(form?.code||'f')+(entry.level!=null?'&level='+(entry.level+entry.plus):'')+'" title="'+escapeHtml(form.name)+'">'+imageHtml(units,form,44,34)+'<span>'+escapeHtml(form.name)+'</span><small>'+(entry.level==null?'Lv指定なし':'Lv'+entry.level+(entry.plus?'+'+entry.plus:''))+(entry.form==null?' / 形態指定なし':' / 第'+(entry.form+1)+'形態')+'</small></a>':'ID '+entry.id;}).join('')+'</div>')+row('にゃんこ砲',choice.cannon===0?'ノーマル砲':'砲ID '+choice.cannon));
}
export function stageSpawnsHtml(stage,map,crown,enemyDatabase,settings,{details=false,stats=false}={}){
  if(stage.missing)return '<p>このステージの固定の敵出現データは収録されていません。</p>';
  const seconds=settings.seconds;
  const cells=stage.spawns.map((original,index)=>{
    const spawn=effectiveSpawn(original,map,crown),enemy=enemyDatabase.enemies[spawn.enemy],options={...settings,health:spawn.health,attack:spawn.attack};
    const status=enemy?calculateEnemyStats(enemy,options):null,url=enemy?enemyDetailUrl(enemy,options):'';
    const range=values=>values[0]===values[1]?formatTime(values[0],seconds):values.map(value=>formatTime(value,seconds)).join('〜');
    const gate=stage.damageCondition?formatNumber(spawn.castle)+'以上':percent(spawn.castle)+'以下';
    return '<tr data-stage-spawn="'+index+'"><td class="stage-enemy-icon">'+(enemy?'<a href="'+escapeHtml(url)+'" aria-label="'+escapeHtml(enemy.name)+'の詳細">'+enemyImageHtml(enemyDatabase,enemy,28)+'</a>':'—')+'</td><td class="stage-enemy-cell">'+(enemy?'<a href="'+escapeHtml(url)+'">'+escapeHtml(enemy.name)+'</a>':'敵ID '+spawn.enemy)+(spawn.boss?'<small>ボス'+(spawn.boss===2?' / 指定2':'')+'</small>':'')+'</td><td><div class="enemy-properties">'+(enemy?enemyAttributesHtml(enemyDatabase,enemy):'')+'</div></td><td>'+percent(spawn.health)+(spawn.health!==spawn.attack?'<small>攻撃 '+percent(spawn.attack)+'</small>':'')+'</td><td>'+(spawn.count===0?'無制限':spawn.count)+'</td><td>'+gate+'</td><td>'+formatTime(spawn.first,seconds)+(spawn.afterCastle?'<small>城条件達成後</small>':'')+'</td><td>'+(spawn.count===1?'—':range(spawn.interval))+'</td>'+
      (stats?'<td>'+formatNumber(status?.hp)+'</td><td>'+formatNumber(status?.attack)+'</td><td>'+formatNumber(status?.dps)+'</td>':'')+
      '<td class="stage-spawn-detail">'+spawn.layers.join('〜')+'</td><td class="stage-spawn-detail">'+formatNumber(spawn.score)+'</td><td class="stage-spawn-detail">'+(spawn.kills?spawn.kills+'体':'なし')+'</td></tr>';
  }).join('');
  return '<div class="db-table-wrap"><table class="db-table db-search-table stage-spawns'+(details?' show-detail':'')+'"><thead><tr>'+['アイコン','敵名','属性・種族','倍率（体力／攻撃）','出現数',stage.scoreMode||stage.timeLimit?'累積ダメージ条件':'敵城体力','初登場','再出現',...(stats?['体力','攻撃力','DPS']:[])].map(label=>'<th>'+label+'</th>').join('')+'<th class="stage-spawn-detail">レイヤー</th><th class="stage-spawn-detail">基礎点</th><th class="stage-spawn-detail">撃破条件</th></tr></thead><tbody>'+cells+'</tbody></table></div>';
}
export function stageMapInfoHtml(map,seconds){
  const pair=(label,value)=>'<th scope="row">'+label+'</th><td>'+value+'</td>';
  return table('<tr>'+pair('ステージ数',map.stages.length)+pair('冠倍率',map.stars.map((value,index)=>(index+1)+'冠 '+percent(value)).join(' / '))+'</tr><tr>'+pair('クリア可能回数',map.clearLimit?map.clearLimit+'回':'制限なし')+pair('インターバル',map.interval?formatTime(map.interval*60*30,seconds):'なし')+'</tr><tr>'+pair('クリア後の表示',map.hiddenAfterClear?'非表示':'表示')+pair('アビス',map.abyss?'あり':'なし')+'</tr>');
}

export function stageMapOverviewHtml(database,map,crown,units,seconds){
  return stageMapInfoHtml(map,seconds)+stageRulesHtml(database,{index:-1},map,crown,units,seconds);
}

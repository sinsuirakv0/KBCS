from pathlib import Path
import hashlib,json,re,sys
source=Path(sys.argv[1] if len(sys.argv)>1 else '../kbc-web').resolve()
lab=Path(sys.argv[2] if len(sys.argv)>2 else '../KBC-rakv0-lab/unit-db').resolve()
# Rust側のID対応表を置き去りにしたまま、上流の解釈だけを更新しない。
compiler_hash=hashlib.sha256((lab/'talents.mjs').read_bytes()).hexdigest()
if compiler_hash!='e75a5f9536de0c779256f41e37dc72c10b3647a08bbea29bedfd85d67a88de9b':
    raise SystemExit('本能の解釈元が変更されています。talent-effects.jsonと変換器版を確認し、同期元SHAを更新してください。')
output=Path('ui')
old_layout=json.loads((output/'layout-fragments.json').read_text(encoding='utf-8-sig')) if (output/'layout-fragments.json').exists() else {}
enemy_definitions=json.loads(Path('crates/kbcs-data/resources/enemy-fields.json').read_text(encoding='utf-8-sig'))
for name,key in [('compile.mjs','compilerSha256'),('castles.mjs','castlesSha256')]:
    if hashlib.sha256((lab.parent/'enemy-db'/name).read_bytes()).hexdigest()!=enemy_definitions[key]:
        raise SystemExit('敵の解釈元が変更されています。enemy-fields.jsonとRust変換器を確認してください。')
if hashlib.sha256((lab/'icons.mjs').read_bytes()).hexdigest()!=enemy_definitions['iconsSha256']:
    raise SystemExit('特性アイコンの対応元が変更されています。property-icons.jsonを確認してください。')
queue=['src/app/main.js','src/features/units/search.js','src/features/units/growth.js','src/features/units/combo-builder.js','src/features/enemies/search.js','src/features/enemies/detail.js','src/features/enemies/style.css','src/shared/ui/site.css','src/features/units/style.css','src/features/stages/search.js','src/features/stages/view.js','src/features/stages/style.css']
seen=set();manifest={}
def save(path,text):
    target=output/path;target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(text,encoding='utf-8-sig' if any(ord(c)>127 for c in text) else 'utf-8')

def replace_once(text,old,new):
    if text.count(old)!=1:raise SystemExit('同期元の構造を確認してください: '+old[:100])
    return text.replace(old,new,1)

def adapt_page_state(name,text):
    pages={'src/features/units/search.js':'unit-search','src/features/enemies/search.js':'enemy-search','src/features/enemies/detail.js':'enemy-detail','src/features/stages/search.js':'stage-search'}
    page=pages.get(name)
    if not page:return text
    text='import {readPageParams,writePageParams,clearPageParams,bindDetailNavigation} from "/native-state.js";\n'+text
    text=replace_once(text,'new URLSearchParams(location.search)','readPageParams("'+page+'")')
    text=text.replace('function writeUrl()', 'function saveState()').replace('writeUrl();','saveState();')
    if page=='unit-search':
        text=replace_once(text,'  const url = location.pathname + (query.size ? "?" + query : "");\n  history.replaceState(null, "", url);\n  try { sessionStorage.setItem("kbc-unit-search-url", url); } catch {}','  writePageParams("unit-search",query);')
        start=text.index('function searchDetailUrl(');end=text.index('\nfunction propertiesHtml',start)
        text=text[:start]+'''function searchDetailUrl(unit,form) {return unitDetailUrl(unit,form);}
bindDetailNavigation('unit-detail','/pages/unit-detail/',()=>{
  const params=new URLSearchParams({setup:'1'});
  for(const key of Object.keys(defaultUnitSettings))params.set(key,String(state[key]));
  params.set('calc',JSON.stringify({talents:state.applyTalents}));
  return params;
});
'''+text[end:]
    elif page=='enemy-search':
        text=replace_once(text,"  const url=location.pathname+(query.size?'?'+query:'');history.replaceState(null,'',url);\n  try{sessionStorage.setItem('kbc-enemy-search-url',url);}catch{}",'  writePageParams("enemy-search",query);')
        text=replace_once(text,"element('enemy-reset').addEventListener('click',()=>{location.href='/pages/tunit-search/';});","element('enemy-reset').addEventListener('click',()=>{clearPageParams('enemy-search');location.href='/pages/tunit-search/';});")
        text+="\nbindDetailNavigation('enemy-detail','/pages/tunit-detail/',()=>writeEnemySettings(new URLSearchParams(),state));\n"
    elif page=='stage-search':
        text=replace_once(text,"  const url=location.pathname+(query.size?'?'+query:'');history.replaceState(null,'',url);\n  try{sessionStorage.setItem('kbc-stage-search-url',url);}catch{}",'  writePageParams("stage-search",query);')
        text=text.replace("element('stage-reset').addEventListener('click',()=>{location.href='/pages/stage-search/';});","element('stage-reset').addEventListener('click',()=>{clearPageParams('stage-search');location.href='/pages/stage-search/';});")
    else:
        text=replace_once(text,"import {copyText} from '../../shared/browser/clipboard.js';\n",'')
        text=replace_once(text,"  history.replaceState(null,'',location.pathname+'?'+query);",'  writePageParams("enemy-detail",query);')
        text=re.sub(r"^  element\('enemy-source'\)\.href=.*\n",'',text,flags=re.M)
        text=re.sub(r"^  try \{const url=sessionStorage.getItem\('kbc-enemy-search-url'\).*\n",'',text,flags=re.M)
        text=replace_once(text,"element('enemy-copy').disabled=false;",'')
        text=replace_once(text,"initializeGameSettings(element('enemy-copy').parentElement,","initializeGameSettings(element('enemy-version').parentElement,")
        text=re.sub(r"\nelement\('enemy-copy'\)\.addEventListener\('click',async\(\)=>\{.*?\n\}\);\n",'\n',text,flags=re.S)
        text+="\nbindDetailNavigation('enemy-detail','/pages/tunit-detail/',target=>writeEnemySettings(new URLSearchParams(),!comparison.same&&Number(target.searchParams.get('id'))===comparison.id?comparison.settings:settings));\n"
    return text

while queue:
    name=queue.pop()
    if name in seen:continue
    seen.add(name)
    path=source/name
    original=path.read_text(encoding='utf-8-sig')
    manifest[name]=hashlib.sha256(path.read_bytes()).hexdigest()
    text=original
    if name=='src/app/main.js':text+='\nimport {initializeWorkspace} from "/workspace.js";\ninitializeWorkspace();\n'
    if name=='src/features/units/search.js':
        text=re.sub(r"import \{loadUnitBattleRuntime\} from .*?;\n",'import {applyUnitTalents,calculateTalentStats} from "/talents.js";\n',text)
        text=text.replace('[database,runtime] = await Promise.all([loadUnitDatabase(),loadUnitBattleRuntime()]);','database = await loadUnitDatabase();')
        text=text.replace('let database,runtime,', 'let database,').replace('runtime.calculateUnitBattle(', 'calculateTalentStats(').replace('runtime.applyUnitTalents(', 'applyUnitTalents(')
    if name=='src/shared/game/units.js':text=text.replace('import dataUrl from "virtual:kbc-unit-data";','const dataUrl = "/api/catalog";')
    if name=='src/shared/game/stages.js':
        text=text.replace("import url from 'virtual:kbc-stage-data';",'const url="/api/stages";')
        start=text.index('export async function loadStageDetail(')
        text=text[:start]+'''export async function loadStageDetail(database,id){
  const stage=database.stages.find(stage=>stage.id===id);
  if(!stage)throw Error('ステージIDが見つかりません。');
  return stage;
}
export async function loadStageMap(database,key){return database.stages.filter(stage=>stage.map===key);}
'''
        text=text.replace('const chunks=new Map();\n','')
    if name=='src/features/stages/model.js':
        text=text.replace("?'EOC1':null)","?'N000':null)")
    if name=='src/features/stages/view.js':
        text=text.replace("spawn.enemy===stage.enemyCastle?'敵城':stage.scoreMode||stage.timeLimit?", "stage.damageCondition?")
        text=text.replace("(spawn.boss?'<small>ボス（衝撃波あり）</small>':'')", "(spawn.boss?'<small>ボス'+(spawn.boss===2?' / 指定2':'')+'</small>':'')")
        text=text.replace("'味方 '+spawn.kills+'体'", "spawn.kills+'体'")
        text=text.replace("spawn.castle?percent(spawn.castle)+'以下':'条件なし'", "percent(spawn.castle)+'以下'")
        text=text.replace('stage.spawns.map(original=>','stage.spawns.map((original,index)=>')
        text=text.replace("return '<tr><td class=\"stage-enemy-icon\">'", "return '<tr data-stage-spawn=\"'+index+'\"><td class=\"stage-enemy-icon\">'")
    if name=='src/features/stages/search.js':
        text=text.replace("stageGimmicks.map(([key,label])=>", "stageGimmicks.filter(([key])=>database.stages.some(stage=>stage.flags.includes(key))).map(([key,label])=>")
        text=text.replace("+'マップ';element('stage-empty')", "+'マップ / '+rows.reduce((count,entry)=>count+entry.stages.length,0)+'ステージ';element('stage-empty')")
    if name=='src/shared/game/unit-view.js':text=text.replace("import unitImages from 'virtual:kbc-unit-images';","const unitImages = {};")
    if name=='src/shared/game/enemies.js':
        text=text.replace("import url from 'virtual:kbc-enemy-data';",'const url="/api/enemies";')
        text=re.sub(r"import (\w+) from '([^']+\.png)';",lambda match:'const '+match[1]+'="/icons/enemies/'+Path(match[2]).name+'";',text)
    if name=='src/shared/browser/capture.js':text=text.replace("import('html2canvas')","import('/vendor/html2canvas.js')")
    if name=='src/features/enemies/view.js':
        start=text.index("  html+='<label>会計力 Lv");end=text.index("  for(const [key,label]",start)
        text=text[:start]+text[end:]
        start=text.index('export function enemyConditionControls(');end=text.index('export function enemyComparisonHtml',start)
        controls=text[start:end]
        controls=replace_once(controls,"  return '<div class=\"db-toolbar\">'+html+", "  return html?'<div class=\"db-toolbar\">'+html+")
        controls=replace_once(controls,"ではありません。</p>';","ではありません。</p>':'';")
        text=text[:start]+controls+text[end:]
    if name=='src/shared/game/game-settings.js':
        text=replace_once(text,'export function researchReduction(settings) {','export function researchReduction(settings) {\n  if(Number.isFinite(settings.researchReductionOverride))return settings.researchReductionOverride;')
        text=replace_once(text,'(includeTreasure ? .005*accountingTreasure : 0)','(includeTreasure ? (settings.accountingTreasureBonus??.005*accountingTreasure) : 0)')
    if name=='src/shared/browser/game-settings.js':
        text='import {deriveSimulationSettings} from "../../../simulation-profile.js";\nimport {readSimulationProfile} from "../../../simulation-store.js";\n'+text
        text=replace_once(text,"export function readGameSettings(){return normalizeGameSettings(readPreferences()?.database||readStoredValue(storageKey));}","export function readGameSettings(){const legacy=normalizeGameSettings(readPreferences()?.database||readStoredValue(storageKey));return {...legacy,...deriveSimulationSettings(readSimulationProfile(legacy))};}")
        text=replace_once(text,"for(const {key} of gameSettingFields)form.elements.namedItem(key).value=value.database[key];","for(const {key} of gameSettingFields){const field=form.elements.namedItem(key);if(field)field.value=value.database[key];}")
        text=replace_once(text,'database:normalizeGameSettings(values)','database:normalizeGameSettings({...readGameSettings(),...values})')
        start=text.index("    '<section id=\"settings-database\"");end=text.index("    '<section id=\"settings-transfer\"",start)
        text=text[:start]+'''    '<section id="settings-database" data-settings-panel="database" hidden><fieldset><legend>表示の初期値</legend><div class="game-settings-fields">'+fields('display')+'</div></fieldset><button type="button" data-profile-settings>お宝・施設を開く</button></section>'+\n'''+text[end:]
        text=replace_once(text,"dialog.querySelector('[data-close]').addEventListener('click',()=>dialog.close());","dialog.querySelector('[data-close]').addEventListener('click',()=>dialog.close());\n  dialog.querySelector('[data-profile-settings]').addEventListener('click',()=>{dialog.close();window.dispatchEvent(new Event('kbcs:open-simulation-settings'));});")
        text=text.replace('サイト表示とDB設定を1つの文字列で移せます。検索中の条件・キャラ・本能玉は含みません。','表示とDBの基本設定を移せます。お宝・施設の個別設定はアプリ内に保存します。')
        text=replace_once(text,"button.textContent='共通設定';button.addEventListener('click',()=>openSiteSettings('database'));","button.textContent='お宝・施設';button.addEventListener('click',()=>window.dispatchEvent(new Event('kbcs:open-simulation-settings')));")
    if name=='src/features/units/combo-model.js':
        text=replace_once(text,"['eva-killer',23]","['eva-killer',23],['villain',25]")
    if name=='src/features/units/growth.js':
        text=replace_once(text,'current.settings.attackTreasure,current.options.talents','current.settings.attackTreasure,current.settings.healthTreasureBonus,current.settings.attackTreasureBonus,current.options.combos,current.options.talents')
        text=replace_once(text,'属性倍率・コンボ・本能玉は含みません。','発動中の体力・攻撃力コンボを含みます。属性倍率・本能玉は含みません。')
    if name=='src/shared/game/unit-stats.js':
        text='import {inheritSimulationSettings} from "../../../simulation-profile.js";\n'+text
        text=replace_once(text,'  return value;','  return inheritSimulationSettings(value,defaults);')
        start=text.index('export function unitDetailUrl(');end=text.index('export function readUnitSettings',start)
        text=text[:start]+'''export function unitDetailUrl(unit,form) {
  return "/pages/unit-detail/?"+new URLSearchParams({id:String(unit.id),form:form.code});
}

'''+text[end:]
    if name=='src/shared/game/enemy-stats.js':
        text='import {inheritSimulationSettings} from "../../../simulation-profile.js";\n'+text
        text=replace_once(text,'  return {...base,health:','  return inheritSimulationSettings({...base,health:')
        text=replace_once(text,'base[key]]))};','base[key]]))},defaults);')
        start=text.index('export function enemyDetailUrl(');end=text.index('\n//',start)
        text=text[:start]+'''export function enemyDetailUrl(enemy) {
  return '/pages/tunit-detail/?id='+enemy.id;
}
'''+text[end:]
    text=adapt_page_state(name,text)
    # 別パネルへ配置した入力も、元フォームの所属で判定する。
    if name=='src/features/units/search.js':
        for event in ['input','change']:
            text=replace_once(text,'element("unit-search-form").addEventListener("'+event+'", requestRender);','document.addEventListener("'+event+'",event=>{if(event.target.form===element("unit-search-form"))requestRender();});')
        text+="\nwindow.addEventListener('kbcs:simulation-change',event=>{Object.assign(state,event.detail);if(database){initializeControls();page=1;render();}});\n"
    if name=='src/features/enemies/search.js':
        for event in ['input','change']:
            text=replace_once(text,"element('enemy-filters').addEventListener('"+event+"',update);","document.addEventListener('"+event+"',event=>{if(event.target.form===element('enemy-filters'))update();});")
        text+="\nwindow.addEventListener('kbcs:simulation-change',event=>{Object.assign(state,event.detail);for(const key of ['alien','starred'])element('enemy-'+key).value=state[key];if(database)update();});\n"
    if name=='src/features/enemies/detail.js':
        text=replace_once(text,"settings:{...defaultEnemySettings}","settings:readEnemySettings(new URLSearchParams(),readGameSettings())")
        text=replace_once(text,'readEnemySettings(new URLSearchParams(value.settings||{}))','readEnemySettings(new URLSearchParams(value.settings||{}),readGameSettings())')
        text=text.replace("element('enemy-content').addEventListener(","element('workspace-body').addEventListener(")
        text=text.replace("  if(event.target.id==='enemy-compare-query')return;","  if(event.target.id==='enemy-compare-query'||event.target.closest('.simulation-settings'))return;")
        text+="\nwindow.addEventListener('kbcs:simulation-change',event=>{Object.assign(settings,event.detail);Object.assign(comparison.settings,event.detail);if(enemy){element('enemy-condition-controls').innerHTML=enemyConditionControls(enemy,settings,'enemy-current-');renderPeerControls();render();}});\n"
    # ブラウザのネイティブES modulesで扱えるようCSSはHTML側から読む。
    if name.endswith('.js'):text=re.sub(r'import\s+["\'][^"\']+\.css["\'];?\s*','',text)
    dependencies=re.findall(r'(?:from\s*|import\s*|@import\s*)["\']([^"\']+)["\']',text)
    for dependency in dependencies:
        if dependency.startswith('.'):
            resolved=(path.parent/dependency).resolve()
            if resolved.relative_to(source).as_posix() in ['simulation-profile.js','simulation-store.js']:continue
            queue.append(resolved.relative_to(source).as_posix())
    save(name,text)
logo=output/'images/kbc-logo.png';logo.parent.mkdir(parents=True,exist_ok=True);logo.write_bytes((source/'images/kbc-logo.png').read_bytes())
head='''<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="dark light"><title>KBCS</title><link rel="icon" href="/images/kbc-logo.png"><link rel="stylesheet" href="/src/shared/ui/site.css"><link rel="stylesheet" href="/src/features/units/style.css"><link rel="stylesheet" href="/native.css"><script type="module" src="/src/app/main.js"></script>'''
header='''<a class="skip-link" href="#main">本文へ移動</a><header class="site-header"><a class="brand" href="/" aria-label="KBCS ホーム"><img src="/images/kbc-logo.png" alt="" width="28" height="28"><span>KBCS</span></a><nav class="site-nav" aria-label="サイト"><a href="/">ホーム</a><a href="/pages/unit-search/">キャラ検索</a><a href="/pages/tunit-search/">敵検索</a><a href="/pages/stage-search/">ステージ</a></nav><div class="theme-switcher" role="group" aria-label="表示テーマ">'''+''.join('<button type="button" class="theme-button" data-theme-value="'+key+'" aria-label="'+label+'" title="'+label+'"><span class="theme-dot theme-dot-'+key+'" aria-hidden="true"></span></button>' for key,label in [('original','濃紺'),('dark','ダーク'),('light','ライト')])+'''</div><button type="button" class="site-settings-trigger" data-site-settings>設定</button></header>'''
html=(source/'pages/unit-search/index.html').read_text(encoding='utf-8-sig').replace('<!-- site:head -->',head).replace('<!-- site:header -->',header).replace('<!-- site:title-hidden -->','<h1 class="visually-hidden">キャラ検索</h1>').replace('<!-- site:footer -->','')
# 表示用説明は元Webと同じ内容に限定し、展開時だけ表示する。
html=html.replace('<p id="unit-search-calculation-note"','<details class="unit-related"><summary>計算条件の注記</summary><p id="unit-search-calculation-note"').replace('研究力「最大」はLv30・お宝300%。</p>','研究力「最大」はLv30・お宝300%。</p></details>')
save('pages/unit-search/index.html',html)
for page,title in [('tunit-search','敵検索'),('tunit-detail','敵詳細')]:
    enemy_head=head.replace('<link rel="stylesheet" href="/native.css">','<link rel="stylesheet" href="/src/features/enemies/style.css"><link rel="stylesheet" href="/native.css">')
    html=(source/('pages/'+page+'/index.html')).read_text(encoding='utf-8-sig').replace('<!-- site:head -->',enemy_head).replace('<!-- site:header -->',header).replace('<!-- site:title-hidden -->','<h1 class="visually-hidden">'+title+'</h1>').replace('<!-- site:footer -->','')
    html=re.sub(r'<button id="enemy-copy"[^>]*>.*?</button>','',html)
    html=re.sub(r'\s*<div class="unit-source">.*?</div>','',html)
    html=html.replace('お宝・施設は共通設定を使い、共有リンクの条件を優先します。','お宝・施設は共通設定を使います。')
    save('pages/'+page+'/index.html',html)
stage_head=head.replace('<link rel="stylesheet" href="/native.css">','<link rel="stylesheet" href="/src/features/stages/style.css"><link rel="stylesheet" href="/native.css">')
html=(source/'pages/stage-search/index.html').read_text(encoding='utf-8-sig').replace('<!-- site:head -->',stage_head).replace('<!-- site:header -->',header).replace('<!-- site:title-hidden -->','<h1 class="visually-hidden">ステージ検索</h1>').replace('<!-- site:footer -->','')
html=html.replace('条件に一致するステージを含むマップを表示します。ステージ数は一致数 / 全数。詳細は全ステージの表示から始まります。','0番台：レジェンドストーリー')
html=html.replace('id="stage-show-enemies" type="checkbox"','id="stage-show-enemies" type="checkbox" checked').replace('stage-search-table hide-stage-enemies','stage-search-table')
save('pages/stage-search/index.html',html)
save('pages/stage-detail/index.html','''<!doctype html>
<html lang="ja"><head>'''+stage_head+'''<script type="module" src="/stage-detail.js"></script></head>
<body data-page="stage-detail"><div class="site-shell">'''+header+'''<main id="main" class="page-main stage-page">
<div class="db-toolbar"><a href="/pages/stage-search/">ステージ検索へ</a><span id="stage-version" class="db-meta"></span></div>
<div class="stage-heading"><h1 id="stage-title">ステージ詳細</h1></div>
<p id="stage-status" role="status">ステージデータを読み込んでいます。</p><button id="stage-retry" type="button" hidden>再読み込み</button>
<nav id="stage-navigation" aria-label="このマップのステージ"></nav>
<div id="stage-detail-controls"><div class="stage-crown-control"><span>冠</span><div id="stage-crown" role="group" aria-label="冠を選択"></div><span id="stage-crown-rate"></span></div><label>単位<select id="stage-time"><option value="seconds">秒</option><option value="frames">F</option></select></label><label><input id="stage-spawn-details" type="checkbox">レイヤー・基礎点・撃破数</label><details><summary>XP計算</summary><label>クリア済み回数<input id="stage-xp-clears" type="number" min="0" max="2147483647" value="0"></label><label>XPコンボ合計（%）<input id="stage-xp-combo" type="number" min="0" max="100" value="0"></label><label><input id="stage-xp-okame" type="checkbox">おかめはちもく</label><div id="stage-xp-profile" class="db-meta"></div></details></div>
<section id="stage-content" hidden><p id="stage-visible-count" class="db-meta"></p><div id="stage-map-info"></div><div id="stage-output"></div></section>
<output id="stage-message" role="status"></output></main></div></body></html>''')
for name in ['crown-on.png','crown-off.png']:
    path=source/'icons/stages'/name
    target=output/'icons/stages'/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(path.read_bytes())
    manifest['icons/stages/'+name]=hashlib.sha256(path.read_bytes()).hexdigest()
for path in output.rglob('*.html'):
    text=path.read_text(encoding='utf-8-sig')
    if old_layout.get('header'):text=text.replace(old_layout['header'],header)
    save(path.relative_to(output),text.replace('/pages/enemy-search/','/pages/tunit-search/'))
save('pages/enemy-search/index.html','<!doctype html><meta charset="UTF-8"><meta http-equiv="refresh" content="0;url=/pages/tunit-search/"><a href="/pages/tunit-search/">敵検索</a>')
for name in ['base.png','burrow.png','revive.png']:
    target=output/'icons/enemies'/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes((source/'icons/enemies'/name).read_bytes())
save('icons/enemies/docs/README.md',(source/'icons/enemies/docs/README.md').read_text(encoding='utf-8-sig'))
package=source/'node_modules/html2canvas'
vendor=package/'dist/html2canvas.esm.js'
save('vendor/html2canvas.js',vendor.read_text(encoding='utf-8-sig'))
save('vendor/html2canvas.LICENSE',(package/'LICENSE').read_text(encoding='utf-8-sig'))
save('layout-fragments.json',json.dumps({'head':head,'header':header},ensure_ascii=False))
talentSource=(lab/'battle.mjs').read_text(encoding='utf-8-sig')
talentFunctions=talentSource[:talentSource.index('export function calculateUnitBattle')]
talentFunctions=re.sub(r'^import .*;\r?\n','',talentFunctions)
save('talent-effects.js',talentFunctions)
save('upstream.json',json.dumps({'repository':'sinsuirakv0/kbc-web','files':manifest,'enemies':{'compilerSha256':enemy_definitions['compilerSha256'],'castlesSha256':enemy_definitions['castlesSha256'],'iconsSha256':enemy_definitions['iconsSha256']},'vendor':{'html2canvas':{'version':json.loads((package/'package.json').read_text())['version'],'sha256':hashlib.sha256(vendor.read_bytes()).hexdigest(),'license':'MIT'}},'talents':{'source':str(lab/'battle.mjs'),'sha256':hashlib.sha256((lab/'battle.mjs').read_bytes()).hexdigest(),'compilerSha256':compiler_hash,'functions':['applyUnitTalents']}},ensure_ascii=False,indent=2))
print('Copied',len(seen),'reachable Web UI files')

import {createLevelControl} from '../../shared/browser/level-control.js';
import {escapeHtml,formatNumber} from './view.js';

const element=id=>document.getElementById(id);
const compact=new Intl.NumberFormat('ja-JP',{notation:'compact',maximumFractionDigits:1});
export function createUnitGrowth(readCurrent) {
  const levelControl=createLevelControl(element('unit-growth-level'),'成長グラフの確認Lv');
  let rows=[],key='',sourceLevel=0,current;
  function draw() {
    levelControl.sync();
    const selected=Math.max(1,Math.min(rows.length,Number(element('unit-growth-level').value)||1));
    const row=rows[selected-1],previous=rows[selected-2],last=rows.at(-1);
    const width=Math.max(280,element('unit-growth-chart').clientWidth),height=230,left=52,right=12,top=12,bottom=30;
    const plotWidth=width-left-right,plotHeight=height-top-bottom;
    const maximum=Math.max(1,...rows.flatMap(row=>[row.hp,row.attack]));
    const base=10**Math.floor(Math.log10(Math.max(1,maximum/4))),step=[1,2,5,10].find(value=>value*base>=maximum/4)*base;
    const upper=Math.ceil(maximum/step)*step;
    const x=level=>left+(level-1)/Math.max(1,last.level-1)*plotWidth,y=value=>top+(1-value/upper)*plotHeight;
    const xStep=Math.max(10,Math.ceil(last.level/Math.max(2,Math.floor(plotWidth/65))/10)*10);
    const levels=[...new Set([1,...Array.from({length:Math.floor(last.level/xStep)},(_,index)=>(index+1)*xStep),last.level])];
    const grid=Array.from({length:Math.round(upper/step)+1},(_,index)=>index*step).map(value=>'<line class="unit-radar-grid" x1="'+left+'" y1="'+y(value)+'" x2="'+(width-right)+'" y2="'+y(value)+'"/><text x="'+(left-6)+'" y="'+y(value)+'" text-anchor="end" dominant-baseline="middle">'+compact.format(value)+'</text>').join('');
    const ticks=levels.map(level=>'<text x="'+x(level)+'" y="'+(height-12)+'" text-anchor="middle">'+level+'</text>').join('');
    const lines=['hp','attack'].map((name,index)=>'<polyline class="unit-growth-series series-'+index+'" points="'+rows.map(row=>x(row.level)+','+y(row[name])).join(' ')+'"/><circle class="series-'+index+'" cx="'+x(selected)+'" cy="'+y(row[name])+'" r="3"/>').join('');
    const marker='<line class="unit-growth-current" x1="'+x(current.level)+'" x2="'+x(current.level)+'" y1="'+top+'" y2="'+(height-bottom)+'"/>';
    element('unit-growth-chart').innerHTML='<svg viewBox="0 0 '+width+' '+height+'" role="img" aria-label="'+escapeHtml(current.form.name)+'のLv別体力・攻撃力"><title>'+escapeHtml(current.form.name)+'の成長</title>'+grid+marker+lines+ticks+'<text x="'+(width-right)+'" y="'+(height-12)+'" text-anchor="end" dy="12">Lv</text></svg>';
    element('unit-growth-point').textContent='Lv'+selected+'：体力 '+formatNumber(row.hp)+(previous?'（前Lv +'+formatNumber(row.hp-previous.hp)+'）':'')+' / 攻撃力 '+formatNumber(row.attack)+(previous?'（前Lv +'+formatNumber(row.attack-previous.attack)+'）':'');
    const checkpoints=[...new Set([1,10,20,30,40,50,60,80,100,120,140,160,180,200,current.level,selected,last.level])].filter(level=>level<=last.level).sort((a,b)=>a-b);
    element('unit-growth-values').innerHTML='<table class="db-table"><thead><tr><th>Lv</th><th>体力</th><th>前Lvから</th><th>攻撃力</th><th>前Lvから</th></tr></thead><tbody>'+checkpoints.map(level=>{const row=rows[level-1],previous=rows[level-2];return '<tr'+(level===selected?' class="is-selected"':'')+'><th scope="row">'+level+'</th><td>'+formatNumber(row.hp)+'</td><td>'+(previous?'+'+formatNumber(row.hp-previous.hp):'—')+'</td><td>'+formatNumber(row.attack)+'</td><td>'+(previous?'+'+formatNumber(row.attack-previous.attack):'—')+'</td></tr>';}).join('')+'</tbody></table>';
  }
  function update() {
    if(!element('unit-growth-panel').open)return;
    current=readCurrent();
    const next=JSON.stringify([current.unit.id,current.form.code,current.settings.healthTreasure,current.settings.attackTreasure,current.settings.healthTreasureBonus,current.settings.attackTreasureBonus,current.options.combos,current.options.talents,current.options.talentLevels]);
    if(key!==next){rows=current.buildRows();key=next;}
    element('unit-growth-level').max=rows.length;
    if(sourceLevel!==current.level||element('unit-growth-name').dataset.form!==current.form.code)element('unit-growth-level').value=current.level;
    sourceLevel=current.level;element('unit-growth-name').dataset.form=current.form.code;
    element('unit-growth-name').textContent=current.form.name+' / Lv1〜'+rows.length+' / 表のLv'+current.level;
    element('unit-growth-note').textContent='表と同じお宝・本能Lvで計算。発動中の体力・攻撃力コンボを含みます。属性倍率・本能玉は含みません。進化条件より低いLvも成長の比較用に表示します。'+(current.superTalents?'選択中の超本能はLv60から反映。':'');
    draw();
  }
  element('unit-growth-panel').addEventListener('toggle',update);
  element('unit-growth-level').addEventListener('input',draw);
  element('unit-growth-current').addEventListener('click',()=>{element('unit-growth-level').value=current.level;draw();});
  let lastWidth=0;
  new ResizeObserver(entries=>{const width=entries[0].contentRect.width;if(width!==lastWidth){lastWidth=width;if(rows.length&&element('unit-growth-panel').open)draw();}}).observe(element('unit-growth-chart'));
  update();return {update};
}

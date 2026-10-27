import {readBattleJson} from './battle-support.js';
const list=document.getElementById('inventory-list'),status=document.getElementById('inventory-status'),search=document.getElementById('inventory-search');
let mode='display',items=[],counts=new Map(),characters=new Map();
function render(){
 const query=search.value.trim().toLocaleLowerCase();list.replaceChildren();
 for(const item of items){
  if(query&&!(`${item.id} ${item.name}`.toLocaleLowerCase().includes(query)))continue;
  const row=document.createElement('div');row.className='inventory-row';
  const picture=document.createElement('span');picture.className='inventory-icon';
  if(item.icon){const image=new Image();image.src='/api/asset/'+item.icon;image.alt='';image.loading='lazy';picture.append(image);}
  else if(item.layers)for(const layer of item.layers){const image=document.createElement('span');image.style.cssText=`position:absolute;width:100%;height:100%;background-image:url('/api/asset/${layer.path}');background-size:${layer.width/layer.rect[2]*100}% ${layer.height/layer.rect[3]*100}%;background-position:${layer.rect[0]/Math.max(1,layer.width-layer.rect[2])*100}% ${layer.rect[1]/Math.max(1,layer.height-layer.rect[3])*100}%`;picture.append(image);}
  const name=document.createElement('span');name.textContent=item.name;const count=counts.get(item.id)||{displayCount:0,earned:0};
  const character=characters.get(item.unit);
  if(character){const detail=document.createElement('small');detail.style.display='block';detail.textContent=[character.owned?'入手済み':'未入手',`Lv${character.level}${character.plus?'＋'+character.plus:''}`,character.third?'第3形態解放':'',character.fourth?'第4形態解放':''].filter(Boolean).join(' / ');name.append(detail);}
  row.append(picture,name);
  if(mode==='display'){
   const input=document.createElement('input');input.type='number';input.min='0';input.max=String(Number.MAX_SAFE_INTEGER);input.step='1';input.value=count.displayCount;input.setAttribute('aria-label',item.name+'の表示数');
   input.addEventListener('change',async()=>{const value=Number(input.value);if(!Number.isSafeInteger(value)||value<0){input.value=count.displayCount;return;}input.disabled=true;try{const response=await readBattleJson('/api/inventory',{method:'PUT',headers:{'Content-Type':'application/json'},body:JSON.stringify({id:item.id,count:value})});counts=new Map(response.items.map(v=>[v.id,v]));count.displayCount=value;status.textContent='保存しました';}catch(error){input.value=count.displayCount;status.textContent=error.message;}finally{input.disabled=false;}});row.append(input);
  }else{const output=document.createElement('output');output.textContent=count.earned.toLocaleString();row.append(output);}
  list.append(row);
 }
}
for(const [id,value] of [['display-tab','display'],['earned-tab','earned']])document.getElementById(id).addEventListener('click',()=>{mode=value;for(const tab of document.querySelectorAll('[role=tab]'))tab.setAttribute('aria-selected',String(tab.id===id));list.setAttribute('aria-labelledby',id);document.getElementById('inventory-hint').textContent=mode==='display'?'終了画面に表示する所持数を設定します。報酬を獲得すると、この数に加算されます。':'シミュレーターで獲得した累計です。表示設定を変更しても変わりません。';render();});
search.addEventListener('input',render);
try{const [catalog,saved]=await Promise.all([readBattleJson('/api/inventory/catalog'),readBattleJson('/api/inventory')]);items=catalog.items;characters=new Map(saved.characters.map(v=>[v.unitId,v]));counts=new Map(saved.items.map(v=>[v.id,v]));for(const value of saved.items)if(!items.some(v=>v.id===value.id))items.push({id:value.id,name:'報酬 '+value.id});items.sort((a,b)=>a.id-b.id);render();}catch(error){status.textContent=error.message;}

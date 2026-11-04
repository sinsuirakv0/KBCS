import {NativeWebGLRenderer} from './src/features/motion/native-webgl-renderer.js';
import {propertyIconHtml} from './src/shared/game/database-view.js';

const size=[64,48],pageSize=64;
const actions=new Map([[0,'移動'],[1,'待機'],[2,'攻撃'],[3,'KB'],[4,'昇天'],[5,'吹き飛ばし'],[6,'吹き飛ばし'],[7,'衝撃波'],[10,'登場'],[11,'潜行開始'],[12,'潜行'],[13,'潜行終了'],[14,'蘇生待ち'],[15,'蘇生中'],[16,'復帰'],[18,'ワープ開始'],[19,'ワープ待ち'],[20,'ワープ終了'],[21,'死亡時烈波']]);
const number=value=>value.toLocaleString('ja-JP'),remaining=value=>value<0?'∞':number(value);

export function actorState(actor){
 if(actor.retiredFrame>=0)return '退場';
 if(actor.hp<=0&&actor.action===3)return '死亡KB';
 return actions.get(actor.action)||'状態 '+actor.action;
}
export function actorPortrait(actor){
 if(actor.retiredFrame>=0||actor.action===4||actor.action===21)return 'kb';
 if(actor.action===14||actor.reviveWait>0&&actor.action!==15&&actor.action!==19)return 'bone';
 return actor.retiredFrame>=0||actor.hp<=0||actor.action===4||actor.action===21?'kb':'icon';
}
export function actorStatuses(actor){
 const states=[];
 if(actor.barrierMax>0)states.push(['enemy-barrier',number(actor.barrier)+'/'+number(actor.barrierMax),'バリア耐久',actor.barrier<=0]);
 if(actor.shieldMax>0)states.push(['aku-shield',number(actor.shield)+'/'+number(actor.shieldMax),'悪魔シールド耐久',actor.shield<=0]);
 if(actor.revivesMax!==0||actor.reviveWait>0||[14,15,16].includes(actor.action))states.push(['revive',remaining(actor.revives)+(actor.reviveWait>0?' · '+actor.reviveWait+'F':''),'残り蘇生回数・待機']);
 if(actor.burrowsMax!==0)states.push(['burrow',remaining(actor.burrows),'残り潜行回数']);
 for(const [key,value,label]of [['stop',actor.stop,'停止'],['slow',actor.slow,'鈍足'],['weaken',actor.weaken,'攻撃力低下'],['curse',actor.curse,'呪い']])if(value>0)states.push([key,value+'F'+(key==='weaken'?' · '+actor.weakenRate+'%':''),label]);
 if(actor.survive>0)states.push(['survive',actor.survive===1?'発動':'使用済','生き残る']);
 return states;
}

// 再表示する古い個体も生成順へ戻し、既に正しい位置にある行は移動しない。
export function orderActorRows(container,nodes){
 let next=container.firstElementChild;
 for(const node of nodes){if(node!==next)container.insertBefore(node,next);next=node.nextElementSibling;}
}

// 開始前に一度だけGPUへ姿勢を渡す。戦闘中は小さな完成済みCanvasを共有する。
export async function prepareInspectorAssets(assets,textures,images,database,signal){
 const surface=document.createElement('canvas');[surface.width,surface.height]=size;
 const renderer=new NativeWebGLRenderer(surface,{alpha:true,trackTextures:true}),cache=new Map();
 const makePose=pose=>{
  if(!pose)return null;
  const key=JSON.stringify(pose);if(cache.has(key))return cache.get(key);
  const image=images.get(textures[pose.texture]);if(!image)return null;
  const packets=pose.packets.filter(packet=>packet.opacity>0&&pose.cuts[packet.cut]?.width>0&&pose.cuts[packet.cut]?.height>0);
  const xs=packets.flatMap(packet=>packet.points.filter((_,index)=>index%2===0)),ys=packets.flatMap(packet=>packet.points.filter((_,index)=>index%2===1));
  if(!xs.length)return null;
  const left=Math.min(...xs),top=Math.min(...ys),width=Math.max(1,Math.max(...xs)-left),height=Math.max(1,Math.max(...ys)-top),scale=Math.min((size[0]-4)/width,(size[1]-4)/height);
  renderer.beginFrame(...size,[0,0,0,0]);
  const iw=image.naturalWidth||image.width,ih=image.naturalHeight||image.height;
  renderer.drawPackets(image,packets.map(packet=>{const cut=pose.cuts[packet.cut];return {blendMode:packet.blend,opacity:packet.opacity,positions:packet.points.map((value,index)=>(value-(index%2?top:left))*scale+(size[index%2]-(index%2?height:width)*scale)/2),uvs:[cut.x/iw,cut.y/ih,cut.x/iw,(cut.y+cut.height)/ih,(cut.x+cut.width)/iw,(cut.y+cut.height)/ih,(cut.x+cut.width)/iw,cut.y/ih]};}));
  const canvas=document.createElement('canvas');[canvas.width,canvas.height]=size;canvas.getContext('2d').drawImage(surface,0,0);cache.set(key,canvas);return canvas;
 };
 const gray=new Map();
 const grayscale=source=>{if(!source)return null;if(gray.has(source))return gray.get(source);const canvas=document.createElement('canvas');[canvas.width,canvas.height]=size;const context=canvas.getContext('2d');context.drawImage(source,0,0);const pixels=context.getImageData(0,0,...size);for(let i=0;i<pixels.data.length;i+=4){const value=(pixels.data[i]*77+pixels.data[i+1]*150+pixels.data[i+2]*29)>>8;pixels.data[i]=pixels.data[i+1]=pixels.data[i+2]=value;}context.putImageData(pixels,0,0);gray.set(source,canvas);return canvas;};
 try{
  await Promise.all([...new Set(assets.profiles.map(profile=>profile.character.icon).filter(Boolean))].map(async path=>{if(images.has(path))return;const image=new Image();image.src='/api/asset/'+path;try{await image.decode();signal.throwIfAborted();images.set(path,image);}catch(error){if(error.name==='AbortError')throw error;}}));
  const bone=makePose(assets.bone),units=new Map(database.units.map(unit=>[unit.id,unit]));
  const profiles=assets.profiles.map(profile=>{
   signal.throwIfAborted();const character=profile.character,image=images.get(character.icon),form=character.kind==='unit'?units.get(character.id)?.forms.find(form=>form.index===character.form):null;
   const icon=document.createElement('canvas');[icon.width,icon.height]=size;
   if(image){const crop=form?.iconCrop?.rect||[0,0,image.naturalWidth,image.naturalHeight],scale=Math.min(size[0]/crop[2],size[1]/crop[3]),width=crop[2]*scale,height=crop[3]*scale;icon.getContext('2d').drawImage(image,...crop,(size[0]-width)/2,(size[1]-height)/2,width,height);}else{const idle=makePose(profile.idle);if(idle)icon.getContext('2d').drawImage(idle,0,0);}
   return {...character,icon,kb:grayscale(makePose(profile.kb)||icon),soul:makePose(profile.soul)};
  });
  return {profiles,bone};
 }finally{renderer.dispose();surface.width=surface.height=0;}
}

function createSideInspector(list,assets,database,enemies,onChange,side){
 let group='present',offset=0,selected=null,revision=0,lastRequest=-Infinity,lastValue;
 const controller=new AbortController(),options={signal:controller.signal},rows=new Map();
 list.innerHTML='<div class="battle-inspector-stats"></div><div class="battle-inspector-filter"><div class="battle-inspector-groups" role="group" aria-label="個体の表示範囲"><button data-group="present" aria-pressed="true">場内</button><button data-group="retired" aria-pressed="false">退場</button><button data-group="all" aria-pressed="false">すべて</button></div><span class="battle-inspector-clock"></span></div><details class="battle-inspector-selection"><summary>個体の詳細</summary><div class="battle-inspector-detail"></div></details><div class="battle-inspector-rows" aria-label="戦闘個体一覧"></div><div class="battle-inspector-pages"><button data-page="-1" aria-label="前の64体">◀</button><output></output><button data-page="1" aria-label="次の64体">▶</button></div>';
 const detail=list.querySelector('.battle-inspector-detail'),selection=list.querySelector('.battle-inspector-selection');
 const body=list.querySelector('.battle-inspector-rows'),stats=list.querySelector('.battle-inspector-stats'),clock=list.querySelector('.battle-inspector-clock'),pages=list.querySelector('.battle-inspector-pages');
 const icon=(key,label)=>key==='revive'||key==='burrow'?'<img class="battle-status-image" src="/icons/enemies/'+key+'.png" alt="">':propertyIconHtml(key==='aku-shield'||key==='enemy-barrier'?enemies:database,key,label,12,false);
 const statuses=actor=>actorStatuses(actor).map(([key,value,label,broken])=>'<span class="battle-status-chip'+(broken?' is-broken':'')+'" title="'+label+' '+value+'">'+icon(key,label)+'<span>'+value+'</span></span>').join('');
 const sourceName=source=>source.kind===1?'#'+source.actorId+' '+(assets.profiles[source.profile]?.name||'個体'):source.kind===2?'にゃんこ砲（種別'+source.detail+'）':source.kind===3?'スニャイパー':'その他のダメージ';
 function sourceImage(context,source,x,y,width,height){
  const image=source.kind===1?assets.profiles[source.profile]?.icon:null;
  if(image)context.drawImage(image,x,y,width,height);
  else{context.fillStyle='#14233b';context.fillRect(x,y,width,height);context.fillStyle='#fff';context.font='10px sans-serif';context.textAlign='center';context.fillText(source.kind===2?'砲':source.kind===3?'狙':'他',x+width/2,y+height-2);}
 }
 function picture(actor,canvas){
  const profile=assets.profiles[actor.profile],kind=actorPortrait(actor),source=kind==='bone'?assets.bone:profile?.[kind];
  const context=canvas.getContext('2d');context.clearRect(0,0,...size);
  if(source)context.drawImage(source,0,0,...size);
  if(kind==='kb'&&profile?.soul)context.drawImage(profile.soul,0,0,22,22);
  if(kind!=='icon')for(const [index,source]of (actor.attackers||[]).slice(0,4).entries()){
   if(index===3&&actor.attackers.length>4){context.fillStyle='#14233b';context.fillRect(48,34,16,14);context.fillStyle='#fff';context.font='9px sans-serif';context.textAlign='center';context.fillText('+'+(actor.attackers.length-3),56,45);}
   else sourceImage(context,source,index*16,34,16,14);
  }
 }
 function showDetail(actor){
  detail.replaceChildren();
  if(!actor){detail.textContent='個体を選択';return;}
  const profile=assets.profiles[actor.profile],heading=document.createElement('strong');heading.textContent='#'+actor.id+' '+(profile?.name||'個体');detail.append(heading);
  const values=[['状態',actorState(actor)],['HP',number(actor.hp)+' / '+number(actor.maximum)],['座標','X '+actor.x/10+' / Y '+actor.y/10],['レイヤー',actor.layer],['生成',actor.bornFrame+'F'],['最終更新',actor.lastFrame+'F'],['死亡 / 蘇生',actor.deaths+' / '+actor.revivals],['陣営 / 枠 / 通番',actor.side+' / '+actor.slot+' / '+actor.serial],['行動 / アニメF',actor.action+' / '+actor.animation]];
  if(actor.retiredFrame>=0)values.push(['退場',actor.retiredFrame+'F']);
  if(actor.deathFrame>=0)values.push(['直近のHP0',actor.deathFrame+'F']);
  const table=document.createElement('dl');for(const [name,value]of values){const term=document.createElement('dt'),definition=document.createElement('dd');term.textContent=name;definition.textContent=value;table.append(term,definition);}detail.append(table);
  const chips=document.createElement('div');chips.className='battle-inspector-detail-status';chips.innerHTML=statuses(actor);detail.append(chips);
  if(actor.attackers?.length){const heading=document.createElement('strong');heading.className='battle-inspector-cause-heading';heading.textContent='HP0になったフレームの攻撃元';detail.append(heading);for(const source of actor.attackers){const row=document.createElement('div');row.className='battle-inspector-cause';const image=document.createElement('canvas');image.width=32;image.height=24;sourceImage(image.getContext('2d'),source,0,0,32,24);const text=document.createElement('span');text.textContent=sourceName(source);row.title='HP確定前の予約量 '+number(source.reserved);row.append(image,text);detail.append(row);}}
 }
 function change(){++revision;lastRequest=-Infinity;onChange();}
 selection.addEventListener('toggle',()=>{if(selection.open)change();},options);
 list.addEventListener('click',event=>{
  const filter=event.target.closest('[data-group]'),page=event.target.closest('[data-page]'),row=event.target.closest('[data-actor]');
  if(filter){group=filter.dataset.group;offset=0;for(const button of list.querySelectorAll('[data-group]'))button.setAttribute('aria-pressed',String(button.dataset.group===group));}
  else if(page)offset=Math.max(0,offset+Number(page.dataset.page)*pageSize);
  else if(row){selected=Number(row.dataset.actor);for(const [id,item]of rows)item.button.setAttribute('aria-pressed',String(id===selected));const actor=lastValue?.rows.find(actor=>actor.id===selected);if(actor)showDetail(actor);selection.open=true;}
  else return;change();
 },options);
 showDetail(null);
 return {
  query(now,force=false){if(!force&&now-lastRequest<200||!list.getClientRects().length&&!detail.getClientRects().length)return undefined;lastRequest=now;return {side,group,offset,selected,revision};},
  refresh:change,
  update(value,frame){
   if(!value||value.side!==side||value.revision!==revision)return;lastValue=value;clock.textContent=frame+'F';
   const [spawned,field,deaths,revived,retired]=value.counts[side];stats.textContent=(side?'出現 '+number(spawned):'生産 '+number(value.produced)+(value.produced!==spawned?'（生成 '+number(spawned)+'）':''))+'　場内 '+number(field)+'\n死亡 '+number(deaths)+'　蘇生 '+number(revived)+'　退場 '+number(retired);stats.title='生産は通常生産の成功数。生成には精霊・追加生産・砲の生成物も含む。死亡はHPが正から0になった回数。蘇生は待機から蘇生動作へ移った回数。場内は昇天中・退場済みを除く個体数。';
   const ids=new Set(value.rows.map(actor=>actor.id));for(const [id,item]of rows)if(!ids.has(id)){item.button.remove();rows.delete(id);}
   for(const actor of value.rows){
    let item=rows.get(actor.id);if(!item){const button=document.createElement('button');button.type='button';button.className='battle-inspector-row';button.dataset.actor=actor.id;const image=document.createElement('canvas');[image.width,image.height]=size;image.setAttribute('aria-hidden','true');const text=document.createElement('span');text.className='battle-inspector-numbers';text.innerHTML='<span class="battle-inspector-primary"><span class="battle-inspector-name"></span><span class="battle-inspector-hp"></span></span><span class="battle-inspector-secondary"><span class="battle-inspector-x"></span><span class="battle-inspector-status"></span></span>';button.append(image,text);item={button,image,text,kind:null};rows.set(actor.id,item);body.append(button);}
    const profile=assets.profiles[actor.profile],kind=actorPortrait(actor),signature=kind+':'+actor.profile+':'+JSON.stringify(actor.attackers||[]);
    if(item.kind!==signature){picture(actor,item.image);item.kind=signature;}
    item.button.title='#'+actor.id+' '+(profile?.name||'個体')+' / '+actorState(actor)+(actor.attackers?.length?' / 攻撃元: '+actor.attackers.map(sourceName).join('、'):'');item.button.setAttribute('aria-pressed',String(actor.id===selected));item.button.classList.toggle('is-retired',actor.retiredFrame>=0);
    item.text.querySelector('.battle-inspector-name').textContent='#'+actor.id+' '+(profile?.name||'個体');item.text.querySelector('.battle-inspector-hp').textContent=number(actor.hp)+' / '+number(actor.maximum);
    item.text.querySelector('.battle-inspector-x').textContent='X '+actor.x/10+' · '+actorState(actor);
    const chips=statuses(actor);if(chips!==item.chips){item.text.querySelector('.battle-inspector-status').innerHTML=chips;item.chips=chips;}
   }
   orderActorRows(body,value.rows.map(actor=>rows.get(actor.id).button));
   if(!value.rows.length){body.dataset.empty='該当する個体なし';if(offset&&value.total<=offset){offset=Math.max(0,Math.floor((value.total-1)/pageSize)*pageSize);change();}}else delete body.dataset.empty;
   pages.querySelector('output').textContent=value.total?(offset+1)+'–'+Math.min(offset+pageSize,value.total)+' / '+value.total:'0';pages.querySelector('[data-page="-1"]').disabled=!offset;pages.querySelector('[data-page="1"]').disabled=offset+pageSize>=value.total;
   if(value.selected&&selection.open)showDetail(value.selected);
  },
  stop(){controller.abort();list.replaceChildren();detail.replaceChildren();rows.clear();lastValue=null;},
 };
}

export function createBattleInspector(enemiesRoot,alliesRoot,assets,database,enemies,onChange){
 const panels=[createSideInspector(enemiesRoot,assets,database,enemies,onChange,1),createSideInspector(alliesRoot,assets,database,enemies,onChange,0)];
 return {
  query(now,force=false){const values=panels.map(panel=>panel.query(now,force)).filter(Boolean);return values.length?values:undefined;},
  update(values,frame){for(const value of values||[])for(const panel of panels)panel.update(value,frame);},
  refresh(){for(const panel of panels)panel.refresh();},
  stop(){for(const panel of panels)panel.stop();},
 };
}

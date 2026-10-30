const storageKey='kbcs:battle-keys';
export const battleKeyActions=[
 ...['KeyD','KeyF','KeyG','KeyH','KeyJ','KeyC','KeyV','KeyB','KeyN','KeyM'].map((code,index)=>({id:'slot'+index,label:'出撃枠 '+(index+1),code,group:index<5?'上段':'下段 / 1段表示中'})),
 {id:'wallet',label:'お財布',code:'KeyX',group:'戦闘'},
 {id:'cannon',label:'にゃんこ砲',code:'Comma',group:'戦闘'},
 {id:'page',label:'1段表示の前半・後半切替',code:'Space',group:'戦闘'},
 {id:'options',label:'オプションを開く・閉じる',code:'Escape',group:'戦闘'},
 {id:'speed',label:'スピードアップ切替',code:'KeyI',group:'アイテム'},
 {id:'sniper',label:'スニャイパー ON / OFF',code:'KeyO',group:'アイテム'},
 {id:'computer',label:'ニャンピュータ ON / OFF',code:'KeyP',group:'アイテム'},
];
export const defaultBattleKeys=Object.fromEntries(battleKeyActions.map(v=>[v.id,v.code]));
export function normalizeBattleKeys(value={}){return Object.fromEntries(battleKeyActions.map(v=>[v.id,typeof value[v.id]==='string'&&/^(Key[A-Z]|Digit[0-9]|Numpad[0-9]|F([1-9]|1[0-2])|Arrow(Up|Down|Left|Right)|Space|Escape|Tab|Enter|Backspace|Comma|Period|Slash|Semicolon|Quote|BracketLeft|BracketRight|Backslash|Minus|Equal|Backquote|)$/.test(value[v.id])?value[v.id]:v.code]));}
export function readBattleKeys(){try{return normalizeBattleKeys(JSON.parse(localStorage.getItem(storageKey)||'{}'));}catch{return {...defaultBattleKeys};}}
export function saveBattleKeys(value){const keys=normalizeBattleKeys(value);localStorage.setItem(storageKey,JSON.stringify(keys));return keys;}
export function keyLabel(code){return ({Space:'Space',Escape:'Esc',Comma:',',Period:'.',Slash:'/',Semicolon:';',Quote:"'",BracketLeft:'[',BracketRight:']',Backslash:'\\',Minus:'−',Equal:'=',Backquote:'`',ArrowUp:'↑',ArrowDown:'↓',ArrowLeft:'←',ArrowRight:'→'})[code]??(code?code.replace(/^(Key|Digit)/,''):'未割当');}
export function battleKeyAction(code,keys,state){
 const action=battleKeyActions.find(v=>keys[v.id]===code);if(!action)return null;
 if(action.id.startsWith('slot')){const slot=Number(action.id.slice(4));if(state.rows===1){if(slot<5)return null;return {target:state.page*5+slot-5};}return {target:slot};}
 if(action.id==='page')return state.rows===1?{control:4}:null;
 return {target:({wallet:102,cannon:101,options:state.paused?(state.info_mode?308:300):100,speed:200,sniper:205,computer:203})[action.id]};
}
// 表示更新の待機中もキーを保持し、ページ番号は送信時の状態で解決する。
export function createBattleKeyQueue(keys){
 const codes=[];
 return {
  get pending(){return codes.length>0;},
  push(code){if(codes.length>=64)return false;codes.push(code);return true;},
  take(state,ticks=0,immediate=false){
   if(ticks<1&&!immediate||state.page_frame||state.guard&&!immediate)return null;
   while(codes.length){const action=battleKeyAction(codes.shift(),keys,state);if(action&&(!state.paused||action.target>=300))return action;}
   return null;
  },
  clear(){codes.length=0;},
 };
}
export function editableKeyTarget(target){return !!target?.closest?.('input,textarea,select,[contenteditable=""],[contenteditable="true"],dialog[open]');}

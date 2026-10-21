export const gameSettingFields = [
  {key:'level',label:'キャラの初期Lv',min:1,max:200,default:30,group:'display'},
  {key:'pageSize',label:'検索の表示件数',options:[25,50,100],default:50,group:'display'},
  {key:'seconds',label:'時間の単位',options:[true,false],labels:['秒','F'],default:true,group:'display'},
  {key:'healthTreasure',label:'体力のお宝',min:0,max:300,group:'unit'},
  {key:'attackTreasure',label:'攻撃力のお宝',min:0,max:300,group:'unit'},
  {key:'fruit',label:'属性のお宝',min:0,max:300,group:'unit'},
  {key:'researchLevel',label:'研究力 Lv',min:1,max:30,group:'facility'},
  {key:'researchTreasure',label:'研究力のお宝',min:0,max:300,group:'facility'},
  {key:'accountingLevel',label:'会計力 Lv',min:1,max:30,group:'facility'},
  {key:'accountingTreasure',label:'会計力のお宝',min:0,max:300,group:'facility'},
  {key:'studyLevel',label:'勉強力 Lv',min:1,max:30,group:'experience'},
  ...[1,2,3].map(chapter=>({key:'studyJapan'+chapter,label:'関西のノリ（日本編'+chapter+'章）',min:0,max:100,group:'experience'})),
  ...[1,2,3].map(chapter=>({key:'studySpace'+chapter,label:'ニュートリノ（宇宙編'+chapter+'章）',min:0,max:100,group:'experience'})),
  {key:'cannonBase',label:'土台',options:[0,1,2,3,4,5,6,7],labels:['なし','スロウ砲（浮き）','鉄壁砲（黒）','かみなり砲（天使）','水鉄砲（赤）','エンジェル砲（ゾンビ）','キャノンブレイク砲（エイリアン）','呪い砲（古代種）'],default:0,group:'cannon'},
  {key:'cannonBaseLevel',label:'土台 Lv',min:0,max:20,default:20,group:'cannon'},
  {key:'cannonDecoration',label:'装飾',options:[0,1,2,3,4,5,6,7],labels:['なし','スロウ砲（遅くする時間）','鉄壁砲（波動ダメージ）','かみなり砲（止める時間）','水鉄砲（烈波ダメージ）','エンジェル砲（攻撃力ダウン時間）','キャノンブレイク砲（毒撃ダメージ）','呪い砲（呪い時間）'],default:0,group:'cannon'},
  {key:'cannonDecorationLevel',label:'装飾 Lv',min:0,max:20,default:20,group:'cannon'},
  {key:'alien',label:'未来編クリスタル',min:0,max:600,group:'enemy'},
  {key:'starred',label:'宇宙編クリスタル',min:0,max:1500,group:'enemy'},
  ...[1,2,3].map(chapter=>({key:'god'+chapter,label:'宇宙編'+chapter+'章の仮面',min:0,max:100,group:'enemy'})),
];
export const defaultGameSettings = Object.fromEntries(gameSettingFields.map(field=>[field.key,field.default??field.max]));

export function normalizeGameSettings(values={}) {
  return Object.fromEntries(gameSettingFields.map(({key,min,max,options})=>{
    const raw=values?.[key],fallback=defaultGameSettings[key];
    if(options)return [key,options.find(option=>String(option)===String(raw))??fallback];
    const value=raw==null||raw===''?fallback:Number(raw);
    return [key,Number.isFinite(value)?Math.max(min,Math.min(max,Math.trunc(value))):fallback];
  }));
}

export function researchSettings(values) {
  if(values.research==='none')return {research:'none',researchLevel:1,researchTreasure:0};
  const {researchLevel,researchTreasure}=normalizeGameSettings(values);
  return {research:researchLevel===30&&researchTreasure===300?'max':researchLevel===1&&researchTreasure===0?'none':'custom',researchLevel,researchTreasure};
}

export function researchReduction(settings) {
  if(Number.isFinite(settings.researchReductionOverride))return settings.researchReductionOverride;
  const {researchLevel,researchTreasure}=researchSettings(settings);
  return (researchLevel-1)*6+researchTreasure*0.3;
}

export function accountingMultiplier(settings,includeTreasure=true) {
  const {accountingLevel,accountingTreasure}=normalizeGameSettings(settings);
  return .95+.05*accountingLevel+(includeTreasure ? (settings.accountingTreasureBonus??.005*accountingTreasure) : 0);
}

export const cannonSettingKeys=['cannonBase','cannonBaseLevel','cannonDecoration','cannonDecorationLevel'];
export function cannonSettings(values) {
  const normalized=normalizeGameSettings(values);
  return Object.fromEntries(cannonSettingKeys.map(key=>[key,normalized[key]]));
}

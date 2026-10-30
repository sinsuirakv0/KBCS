import {mountUnitSearchForm,createUnitSearchState,createUnitFilterControls} from './src/features/units/search-controls.js';
import {selectUnitRows} from './src/features/units/model.js';
import {prepareUnitSearch,unitSearchProfile} from './native-unit-search.js';
import {formationIconHtml} from './formation-view.js';
import {escapeHtml} from './src/features/units/view.js';
import {createPagination} from './src/shared/browser/pagination.js';

// 絞り込みとページングはキャラデータの部品を使い、結果の操作だけ編成用にする。
export function createFormationSearch(database,manifest,onSelect,onError){
 const node=id=>document.getElementById(id),form=mountUnitSearchForm(),state=createUnitSearchState();
 state.spirits=false;
 const {initializeControls,readControls}=createUnitFilterControls(()=>database,state);
 const pagination=createPagination(node('formation-pagination'),value=>{page=value;render();});
 let page=1,revision=0;
 async function render(){
  const current=++revision,settings=structuredClone(state);
  try{
   const native=await prepareUnitSearch(database,settings);if(current!==revision)return;
   const rows=selectUnitRows(database,settings,(unit,form,values)=>unitSearchProfile(database,unit,form,values,native));
   const size=Number(node('formation-page-size').value),pages=Math.max(1,Math.ceil(rows.length/size));page=Math.min(page,pages);
   node('formation-results').innerHTML=rows.slice((page-1)*size,page*size).map(({unit,form})=>'<button data-unit="'+unit.id+'" aria-label="'+escapeHtml(form.name)+'">'+formationIconHtml(database,form,manifest)+'<span>'+escapeHtml(form.name)+'</span></button>').join('');
   node('formation-result-count').textContent=new Set(rows.map(row=>row.unit.id)).size+'キャラ / '+rows.length+'形態';pagination.update(page,pages);
   node('unit-include-talent-resistance').closest('label').hidden=state.includeTalents;
  }catch(error){if(current===revision)onError(error);}
 }
 function change(){readControls();page=1;render();}
 initializeControls();
 form.addEventListener('submit',event=>{event.preventDefault();change();});
 form.addEventListener('input',change);form.addEventListener('change',change);
 node('unit-reset').addEventListener('click',()=>{Object.assign(state,createUnitSearchState());state.spirits=false;initializeControls();page=1;render();});
 node('formation-page-size').addEventListener('change',()=>{page=1;render();});
 node('formation-results').addEventListener('click',event=>{const button=event.target.closest('[data-unit]');if(button)onSelect(Number(button.dataset.unit));});
 render();
}

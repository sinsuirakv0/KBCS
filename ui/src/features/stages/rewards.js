import {escapeHtml,formatNumber} from '../../shared/game/database-view.js';
import {loadUnitDatabase} from '../../shared/game/units.js';
import {imageHtml} from '../../shared/game/unit-view.js';
import {queryTerms,selectStageRewards} from './model.js';

export function initializeRewardPicker(root,database){
  const input=root.querySelector('input'),selected=root.querySelector('[data-reward-selected]');
  let dialog,units,draft=new Set();
  const name=value=>database.rewards[value]?.name||value;
  function renderSelected(){
    selected.innerHTML=queryTerms(input.value).map((value,index)=>'<button type="button" data-remove-reward="'+index+'" title="この報酬を除外">'+escapeHtml(name(value))+' ×</button>').join('');
  }
  function apply(){input.dispatchEvent(new Event('input',{bubbles:true}));renderSelected();}
  function renderChoices(){
    const list=selectStageRewards(database,dialog.querySelector('[name="kind"]').value,dialog.querySelector('[name="query"]').value);
    dialog.querySelector('[data-count]').textContent=formatNumber(list.length)+'件 / '+draft.size+'件選択';
    dialog.querySelector('[data-choices]').innerHTML=list.map(item=>{
      const unit=item.unit!=null?units?.units.find(unit=>unit.id===item.unit):null,form=unit?.forms.find(form=>form.index===(item.form||0))||unit?.forms[0];
      const image=form?imageHtml(units,form,32,25):item.icon?'<img src="'+escapeHtml(database.imageBase+item.icon)+'" alt="" loading="lazy" width="25" height="25">':'';
      return '<label class="stage-reward-choice"><input type="checkbox" value="'+item.id+'"'+(draft.has(String(item.id))?' checked':'')+'>'+image+'<span>'+escapeHtml(item.name)+'<small class="db-meta">ID '+item.id+(item.unit!=null?' / キャラID '+item.unit:'')+'</small></span></label>';
    }).join('')||'<p>一致する報酬がありません。</p>';
  }
  async function open(){
    if(!dialog){
      dialog=document.createElement('dialog');dialog.className='db-dialog stage-reward-dialog';dialog.setAttribute('aria-labelledby','stage-reward-title');
      dialog.innerHTML='<div class="db-toolbar"><h2 id="stage-reward-title">報酬を選ぶ</h2><button type="button" data-close>閉じる</button></div><div class="db-toolbar"><label>種類<select name="kind"><option value="">すべて</option><option value="item">アイテム</option><option value="unit">ドロップキャラ</option><option value="evolution">進化権</option></select></label><input type="search" name="query" aria-label="報酬名・IDで絞り込む" placeholder="報酬名・ID"><span data-count class="db-meta"></span></div><div data-choices class="stage-reward-choices"></div><div class="db-toolbar"><button type="button" data-apply>選択を適用</button><button type="button" data-clear>選択解除</button><span class="db-meta">複数選択すると、すべてを含むステージを検索します。</span></div><output role="status"></output>';
      document.body.append(dialog);
      for(const control of dialog.querySelectorAll('[name]'))control.addEventListener('input',renderChoices);
      dialog.querySelector('[data-close]').addEventListener('click',()=>dialog.close());
      dialog.querySelector('[data-choices]').addEventListener('change',event=>{
        const choice=event.target;if(!choice.matches('input[type="checkbox"]'))return;
        if(choice.checked)draft.add(choice.value);else draft.delete(choice.value);
        dialog.querySelector('[data-count]').textContent=formatNumber(selectStageRewards(database,dialog.querySelector('[name="kind"]').value,dialog.querySelector('[name="query"]').value).length)+'件 / '+draft.size+'件選択';
      });
      dialog.querySelector('[data-clear]').addEventListener('click',()=>{draft.clear();renderChoices();});
      dialog.querySelector('[data-apply]').addEventListener('click',()=>{input.value=[...draft].join(' ');apply();dialog.close();});
    }
    draft=new Set(queryTerms(input.value));renderChoices();dialog.showModal();
    if(!units){try{units=await loadUnitDatabase();if(dialog.open)renderChoices();}catch{dialog.querySelector('output').textContent='キャラ画像を読み込めませんでした。報酬の選択は利用できます。';}}
  }
  root.querySelector('[data-reward-open]').addEventListener('click',open);
  selected.addEventListener('click',event=>{const button=event.target.closest('[data-remove-reward]');if(!button)return;input.value=queryTerms(input.value).filter((_,index)=>index!==Number(button.dataset.removeReward)).join(' ');apply();});
  renderSelected();
}

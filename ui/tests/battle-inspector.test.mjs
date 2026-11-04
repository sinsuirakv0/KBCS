import test from 'node:test';
import assert from 'node:assert/strict';
import {actorState,actorPortrait,actorStatuses,orderActorRows} from '../battle-inspector.js';

const actor={retiredFrame:-1,action:0,hp:100,revives:0,revivesMax:0,reviveWait:0,burrows:0,burrowsMax:0,barrier:0,barrierMax:0,shield:0,shieldMax:0,stop:0,slow:0,weaken:0,curse:0,survive:0};
test('骨は蘇生待ちだけで、退場個体はKB画像を使う',()=>{
 assert.equal(actorPortrait({...actor,action:14,reviveWait:30}),'bone');
 assert.equal(actorPortrait({...actor,action:14,reviveWait:30,retiredFrame:100}),'kb');
 assert.equal(actorPortrait({...actor,action:4,reviveWait:30}),'kb');
 assert.equal(actorPortrait({...actor,action:15}),'icon');
 assert.equal(actorState({...actor,hp:0,action:3}),'死亡KB');
});
test('耐久と残り回数の0を維持し、独立していない盾の再生回数は作らない',()=>{
 const states=actorStatuses({...actor,shieldMax:5000,revivesMax:2,burrowsMax:-1,burrows:-1,stop:10});
 assert.deepEqual(states.map(value=>value.slice(0,2)),[['aku-shield','0/5,000'],['revive','0'],['burrow','∞'],['stop','10F']]);
 assert.equal(states[0][3],true);
});

test('表示範囲を戻しても生成順を守り、変化しない行は動かさない',()=>{
 // 順序操作に必要なDOMの最小契約だけを用意する。
 let children=[],moves=0;
 const nodes=[1,2,3,4].map(id=>({id,get nextElementSibling(){return children[children.indexOf(this)+1]||null;}}));
 const container={get firstElementChild(){return children[0]||null;},insertBefore(node,next){children=children.filter(child=>child!==node);children.splice(next?children.indexOf(next):children.length,0,node);++moves;}};
 children=[nodes[2],nodes[3],nodes[0],nodes[1]];
 orderActorRows(container,nodes);
 assert.deepEqual(children.map(node=>node.id),[1,2,3,4]);
 assert.equal(moves,2);
 orderActorRows(container,nodes);
 assert.equal(moves,2);
});

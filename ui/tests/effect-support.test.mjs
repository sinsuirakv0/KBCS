import assert from 'node:assert/strict';
import {applyUnitTalents} from '../talent-effects.js';
import {comboAvailable,talentMaximum,unsupportedTalentHtml} from '../effect-support.js';
import {activeFormationCombos} from '../formation-combos.js';

const known={id:31,index:0,maxLevel:1,targets:[],effect:{kind:'stat',key:'attackPercent'},values:[[20]]};
const special={id:73,index:1,maxLevel:0,comboUnlock:392,targets:[],effect:{kind:'comboUnlock'},values:[]};
const unknown={id:901,index:2,name:'<unknown>',description:'保留',support:'unsupported',raw:{slot:2,cells:[901,0,392,0]}};
const unit={talents:[known,special,unknown]};
const form={index:2,targets:['red'],abilities:[{key:'massive'}]};
const result=applyUnitTalents(unit,form,{0:1,1:1,2:1},60);
assert.deepEqual(result.attackRates,[20]);
assert.deepEqual(result.applied,[0]);
assert.equal(talentMaximum(special),1);
assert.match(unsupportedTalentHtml(unknown),/本能ID 901/);
assert.match(unsupportedTalentHtml(unknown),/392/);
assert.match(unsupportedTalentHtml(unknown),/&lt;unknown&gt;/);
assert.doesNotMatch(unsupportedTalentHtml(unknown),/<select/);

const combo={id:392,type:0,active:false,members:[{id:358,form:2}],unlock:[{unitId:358,talentIndex:1,minimumLevel:60}]};
const member={unitId:358,form:2,level:59,plus:1,talents:{1:0}};
assert.equal(comboAvailable(combo,[member]),false);
member.talents[1]=1;
assert.equal(comboAvailable(combo,[member]),true);
assert.deepEqual(activeFormationCombos({combos:[combo]},[member]),[combo]);
assert.deepEqual(activeFormationCombos({combos:[combo]},[null,null,null,null,null,member]),[]);
member.plus=0;
assert.equal(comboAvailable(combo,[member]),false);

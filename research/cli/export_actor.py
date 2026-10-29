"""版固定の生成関数・属性getter/setterをC++へ書き出す。未知の構文は停止する。"""
import hashlib
import json
from pathlib import Path
import re
import struct
from actor_hit_source import hit_source
from actor_cannon_source import cannon_hit
from actor_pool_source import adapt_actor_pool

ROOT = Path(__file__).resolve().parents[2]
reference = json.loads((ROOT / 'research/.local/reference.json').read_text(encoding='utf-8-sig'))
cache = Path(reference['cache'])
identity = json.loads((cache / 'identity.json').read_text(encoding='utf-8-sig'))
SHA = '6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea'
assert identity['version'] == '15.7.2' and identity['architecture'] == 'arm64-v8a' and identity['sha256'] == SHA
binary = Path(identity['binary']).read_bytes()
assert hashlib.sha256(binary).hexdigest() == SHA


def source(address):
    return (cache / 'code' / (('006eccf4' if address in ('006ecfec','006ed8d4','006ed43c','006ed5e0') else '006eb464' if address in ('006eb6b0','006eb8c0','006eb7e0','006ebb0c') else '006d6d04' if address in ('006d97dc','006da994','006dac8c','006d823c','006d8558','006d8cc0','006d8584','006d8cf8') else address) + '.c')).read_text(encoding='utf-8')


def clean(value):
    value = re.sub(r'/\*.*?\*/', '', value, flags=re.S)
    return '\n'.join(line.rstrip() for line in value.splitlines() if line.strip())


def closing(text, start):
    depth = 0
    for index in range(start, len(text)):
        if text[index] == '(':
            depth += 1
        elif text[index] == ')':
            depth -= 1
            if not depth:
                return index
    raise ValueError('Unclosed expression')


def effect_source():
    text = clean(source('006e62f8'))
    keys=[]
    def parameter(match):
        before=text[:match.start()]
        address=int(re.findall(r's_battle_\w+_([0-9a-f]{8})',before)[-1],16)
        key=read_string(address)
        if key not in keys:keys.append(key)
        return 'ctx.effectParameter('+str(keys.index(key))+')'
    text=re.sub(r'FUN_009019f4\([^;]+?\)',parameter,text)
    text=re.sub(r'  lVar2 = tpidr_el0;\n  local_78 = \*\(long \*\)\(lVar2 \+ 0x28\);\n','',text)
    text=re.sub(r'  if \(\*\(long \*\)\(lVar2 \+ 0x28\) == local_78\) \{\n    return;\n  \}\n  __stack_chk_fail\(\);','  return;',text)
    text=re.sub(r' +if \(\(local_\w+ & 1\) != 0\) \{\n.*?operator_delete.*?;\n +\}', '',text,flags=re.S)
    text=re.sub(r'\buVar\d+ = s_battle_\w+\.\w+,\s*','',text)
    text=text.replace('"ScoreBonusMap.json" + param_1 + 0xb','0')
    text=text.replace('bVar13 & *(int *)(param_1 + 0x4dc) != -1','bVar13 & (*(int *)(param_1 + 0x4dc) != -1)')
    # 文字列の組立て・破棄だけを除く。ゲーム値とif/else/gotoは保持する。
    text=re.sub(r'^ +(?:[^;\n]*\b(?:local_\w+|uStack_\w+|cStack_\w+|acStack_\w+|s_battle_\w+)\b[^;]*;)', '',text,flags=re.M)
    text=re.sub(r'^ +(?:uVar\d+|cVar\d+) = (?:_DAT_|_UNK_|s_battle_|CONCAT)[^;]+;', '',text,flags=re.M)
    text=clean(text)
    assert not any(value in text for value in ['operator_','local_','Stack_','s_battle_','tpidr','CONCAT','SUB']),text
    return text,keys


def segment_at(address):
    phoff = struct.unpack_from('<Q', binary, 32)[0]
    phsize,count=struct.unpack_from('<HH',binary,54)
    for index in range(count):
        kind,_,offset,virtual,_,size=struct.unpack_from('<IIQQQQ',binary,phoff+index*phsize)
        if kind==1 and virtual+0x100000<=address<virtual+0x100000+size:return offset+address-virtual-0x100000
    raise ValueError(hex(address))


def read_string(address):
    offset=segment_at(address)
    return binary[offset:binary.index(b'\0',offset)].decode('ascii')


def strengthen_source():
    text=clean(source('00a999e4'))
    text=text.replace('  lVar2 = tpidr_el0;\n','').replace('  local_68 = *(long *)(lVar2 + 0x28);\n','')
    text=re.sub(r'      local_70 = operator_new.*?      iVar8 = FUN_009019f4\([^;]+;',
        '      iVar8 = ctx.clock->kill_threshold;',text,flags=re.S)
    text=re.sub(r' +if \(\(local_80 & 1\) != 0\) \{\n +operator_delete\(local_70\);\n +\}','',text)
    text=re.sub(r'  if \(\*\(long \*\)\(lVar2 \+ 0x28\) != local_68\) \{\n +__stack_chk_fail\(\);\n  \}', '',text)
    text=re.sub(r'    uVar6 = FUN_005bc1dc\(0,param_2\);\n    iVar7 = FUN_005bce20\(0,uVar6\);',
        '    iVar7 = ctx.clock->forms[0][param_2];',text)
    text=text.replace('FUN_0066367c(lVar9 + 0x1560,iVar1 + -2,0x12)','ctx.clock->kill_orb[param_2]')
    assert 'operator_' not in text and 'tpidr' not in text and '__stack' not in text
    return text


def motion_source():
    text=clean(source('009f4688'))
    text=text.replace('  lVar1 = tpidr_el0;\n  local_48 = *(long *)(lVar1 + 0x28);\n','')
    text=re.sub(r' +if \(\*\(long \*\)\(lVar1 \+ 0x28\) != local_48\) goto LAB_009f4a70;','',text)
    guard='if (*(long *)(lVar1 + 0x28) == local_48) {'
    while guard in text:
        start=text.index(guard);opening=start+len(guard)-1;depth=1;end=opening+1
        while depth:
            depth+=(text[end]=='{')-(text[end]=='}');end+=1
        text=text[:start]+text[opening+1:end-1]+text[end:]
    text=re.sub(r'\s*goto LAB_009f4a70;', '',text)
    text=re.sub(r'LAB_009f4a70:\n +__stack_chk_fail\(\);','',text)
    text=re.sub(r'FUN_005bde34\(([^;]+)\);\n +(iVar\d+) = FUN_(0044beb4|0044bf2c)\(\);',
        r'\2 = FUN_\3(FUN_005bde34(\1));',text)
    text=re.sub(r'                local_58 = FUN_00a954b8.*?                iVar4 = FUN_0044beb4\(lVar7 \+ 0x28\);',
        '                iVar4 = ctx.motion->soul_frames;',text,flags=re.S)
    text=re.sub(r'\(iVar([35]) \+ 1\) / iVar4',r'ctx.divide(iVar\1 + 1,iVar4)',text)
    assert 'operator_' not in text and 'tpidr' not in text and '__stack' not in text and 'FUN_0044beb4()' not in text
    return text


def protection_source():
    text=clean(source('006d6d04'))
    start=text.index('              iVar30 = FUN_00a93f08(lVar65,uVar43 & 0xffffffff);',text.index('LAB_006d9768:'))
    end=text.index('                uVar68 = FUN_005bc198();',start)
    text=text[start:end]+'              }'
    text=text.replace('                  pppiVar82 = pppiVar72 + 1;\n','')
    text,count=re.subn(r'                    while \(pppiVar54.*?\*\(undefined1 \*\)\(pppiVar49 \+ 4\) = 1;',
        '                    ctx.protection->shield_hit = 1;',text,flags=re.S)
    assert count==1
    for kind in [0,1]:
        text,count=re.subn(r'                      lVar66 = 0x1e;.*?                      } while \(lVar66 != 0\);',
            '                      ctx.protectionVisual('+str(kind)+',lVar65,uVar43,FUN_'+('00a9bd44' if kind==0 else '00a9cf2c')+'(lVar65,uVar43 & 0xffffffff) == 2);',text,count=1,flags=re.S)
        assert count==1
    assert not any(value in text for value in ['operator_','pppiVar','pbVar','param_1','lVar66'])
    return 'void FUN_006d97dc(int param_2,int param_3)\n{\n  int iVar30;int iVar31;uint uVar33;ulong uVar46;ulong uVar55;ulong uVar68;\n  long lVar65=param_2;ulong uVar43=(uint)param_3;\n'+text+'\n}\n'


def health_source():
    text=clean(source('006d6d04'))
    start=text.index('            iVar30 = FUN_00a958b0(piVar62,(ulong)piVar89 & 0xffffffff);')
    end=text.index('            piVar64 = (int *)',start)
    text=text[start:end]
    text=text.replace('FUN_005bc1dc(0,(ulong)piVar89 & 0xffffffff)','ctx.health->deployment_slot')
    text=text.replace('FUN_005c2d18(plVar48,uVar76)','ctx.health->cooldown')
    text=text.replace('                uVar76 = -(uVar76 >> 0x1f) & 0xfffffffc00000000 | uVar76 << 2;\n','')
    text=text.replace('*(int *)((long)&local_250 + uVar76) = *(int *)((long)&local_250 + uVar76) + iVar31;',
        'ctx.healthResult->delay_slot = uVar76;ctx.healthResult->delay_frames = iVar31;')
    start=text.index('                pvVar51 = operator_new(0xc);')
    end=text.rindex('                param_1[0x13dc6] = (long)puVar78;')+len('                param_1[0x13dc6] = (long)puVar78;')
    text=text[:start]+'                ctx.healthResult->delay_x = iVar31;ctx.healthResult->delay_y = iVar36;'+text[end:]
    text=text.replace("(char)param_1[0x73445] != '\\0'",'ctx.health->preserve_enemy_castle != 0')
    # 元のparam_1はlong*。ここで残る参照はいずれも(long)param_1でバイト単位。
    assert not any(v in text for v in ['param_1[','operator_','local_','plVar48','pvVar','puVar']),[line for line in text.splitlines() if any(v in line for v in ['param_1[','operator_','local_','plVar48','pvVar','puVar'])]
    # 006dac40はstr w9。Ghidraの4バイト代入を同じ32bitストアへ戻す。
    text=text.replace('pbVar75[0x20] = 1;\n              pbVar75[0x21] = 0;\n              pbVar75[0x22] = 0;\n              pbVar75[0x23] = 0;','*(int *)(pbVar75 + 0x20) = 1;')
    text=text.replace('piVar62','param_2').replace('piVar89','param_3').replace('(int *)0x0','0')
    return 'void FUN_006da994(long param_1,int param_2,int param_3)\n{\n  int iVar30;int iVar31;int iVar36;int iVar38;int iVar41;ulong uVar46;ulong uVar76;\n  bool bVar26=param_2==0;long lVar65=(long)param_2*0xc804;long pbVar75=(long)param_3*0x3ec+lVar65+0x84080;\n'+text+'\n  ctx.healthResult->previous_hp=iVar30;\n}\n'


def reaction_source():
    text=clean(source('006d6d04'))
    start=text.index('LAB_006dac8c:')
    end=text.index('LAB_006db1b4:',start)
    text=text[start:end]
    text=text[:text.rindex('                goto LAB_006db1ac;')]
    # 周囲の死亡数/所持金の集計を含めず、同じ時点のHPと予約値を受ける。
    text=text[text.index('              if (((bVar26)'):]
    start=text.index('                      lVar66 = 0x1e;')
    end=text.index('                      } while (lVar66 != 0);',start)+len('                      } while (lVar66 != 0);')
    visual=text[start:end]
    visual=visual[visual.index('                          iVar31 = '):visual.index('                          break;')]
    visual=visual.replace('*(int *)(pbVar75 + 4)','ctx.reactionResult->death_x').replace('*(int *)(pbVar75 + 8)','ctx.reactionResult->death_y')
    text=text[:start]+'                      if (ctx.reaction->death_visual_available) {ctx.reactionResult->death_visual=1;\n'+visual+'                      }'+text[end:]
    text=text.replace('goto LAB_006db1ac;', 'return;')
    text=text.replace('piVar62','param_2').replace('piVar89','param_3')
    assert not any(v in text for v in ['param_1[','operator_','pbVar75[','local_','0x13cae'])
    # 抽出した外側のifを閉じる。原本の最後のgotoは関数末尾のreturnへ置換する。
    return 'void FUN_006dac8c(long param_1,int param_2,int param_3)\n{\n  int iVar30=ctx.reaction->previous_hp;int iVar31;int iVar36;int iVar38;int iVar41;int iVar74;int iVar79;int *piVar64;ulong uVar46;ulong uVar76;long lVar66;\n  bool bVar26=param_2==0;long pbVar75=(long)param_3*0x3ec+(long)param_2*0xc804+0x84080;\n'+text+'\n              }\n}\n'


def begin_source():
    unit=clean(source('006eb464'));enemy=clean(source('006eccf4'))
    start=unit.index('  FUN_00a9bb38(param_3,uVar38 & 0xffffffff,0);')
    common=unit[start:unit.index('  if (uVar38 == 0)',start)]
    start=enemy.index('      iVar13 = FUN_00a9d124')
    counter=enemy[start:enemy.index('      if (uVar23 == 0)',start)].replace('iVar13','iVar14').replace('uVar23','uVar38')
    start=unit.index('\n  puVar37 = (undefined4 *)')+1
    cooldown=unit[start:unit.index('  iVar14 = FUN_00a94234',start)]
    return 'void FUN_006eb6b0(long param_1,int param_3,int param_4)\n{\n  int iVar14;undefined4 uVar15;undefined4 *puVar37;ulong uVar38=(uint)param_4;\n  if (FUN_00a93f08(param_3,param_4)==0) return;\n'+common+'\n  if (!(ctx.environment.unit_modes[param_3]&1)) {\n'+counter+'\n  }\n  if (!uVar38) return;\n'+cooldown+'\n}\n'


def walk_source(enemy_mode):
    text=clean(source('006eccf4' if enemy_mode else '006eb464'))
    if enemy_mode:
        start=text.index('      iVar13 = FUN_00a94234(param_3,uVar23 & 0xffffffff);')
        end=text.index('      if (iVar13 == 3)',start)
        text=text[start:end].replace('goto LAB_006ece44;','return;')
        name='006ecfec'
        locals='  int iVar13;int iVar15;int iVar16;undefined4 uVar14;ulong uVar26;ulong uVar23=(uint)param_4;'
    else:
        start=text.index('  iVar14 = FUN_00a94234(param_3,uVar38 & 0xffffffff);')
        end=text.index('  iVar14 = FUN_00a94234(param_3,uVar38 & 0xffffffff);',start+10)
        text=text[start:end].replace('goto LAB_006eb6a4;','return;').replace('goto LAB_006ec5dc;',
            'FUN_009f4688(param_1,param_2,param_3,uVar38 & 0xffffffff);return;')
        name='006eb8c0'
        locals='  int iVar14;int iVar18;ulong uVar38=(uint)param_4;'
    return 'void FUN_'+name+'(long param_1,long param_2,int param_3,int param_4)\n{\n'+locals+'\n'+text+'\n}\n'


def knockback_source():
    text=clean(source('006eb464'))
    start=text.index('      iVar14 = FUN_00a94234(param_3,uVar38 & 0xffffffff);',text.index('  if (iVar14 != 3)'))
    end=text.index('      goto LAB_006eb6a4;',start)+len('      goto LAB_006eb6a4;')
    modes=text[start:end]
    start=text.index('  FUN_009f4688(param_1,param_2,param_3,uVar38 & 0xffffffff);',end)
    normal=text[start:text.index('LAB_006ebb00:',start)]
    text='  if (FUN_00a94234(param_3,param_4)!=3) {\n'+modes+'\n  }\n'+normal
    text=text.replace('goto LAB_006eb6a4;','return;')
    text=text.replace('PTR_DAT_00c1b630','0xc23fc4').replace('PTR_DAT_00c1b680','0xc24024')
    # undefined4*の加算は4倍してから8バイト書込へキャストする。
    text=re.sub(r'\*\(undefined8 \*\)\(puVar37 \+ (0x[0-9a-f]+)\)',r'*(undefined8 *)((long)puVar37 + (\1)*4)',text)
    text=text.replace("*(char *)(param_1 + 0x32e9) == '\\0'",'!ctx.knockback->quiet')
    assert not any(v in text for v in ['param_1[','operator_','PTR_DAT_','char *'])
    return 'void FUN_006eb7e0(long param_1,long param_2,int param_3,int param_4)\n{\n  int iVar14;int iVar18;int iVar17;undefined4 uVar15;undefined4 *puVar37;ulong uVar23;ulong uVar24;ulong uVar38=(uint)param_4;long puVar33;\n  int iVar2=param_3==0?60:-60;int iVar3=param_3==0?20:-20;long lVar36=param_1+(long)param_3*0x1f0;\n  puVar37=(undefined4 *)(param_1+0x84080+(long)param_3*0xc804+uVar38*0x3ec);\n'+text+'\n}\n'


def displacement_source():
    text=clean(source('006eccf4'))
    start=text.index('          iVar13 = FUN_00a94234(param_3,uVar23 & 0xffffffff);',text.index('        if (iVar13 != 0x11)'))
    end=text.index('\n        goto LAB_006ece44;',start)
    text=text[start:end].rstrip()
    # 抽出開始より外側のif(action!=17)を閉じる末尾1個だけを除く。
    assert text.endswith('}') and text.count('{')+1==text.count('}')
    text=text[:-1]
    text=re.sub(r'                if \(1 < \*piVar40\) \{.*?\n                }','',text,flags=re.S)
    text=text.replace('                local_a8 = (uint *)0x0;\n                local_a0 = (uint *)0x0;\n                local_98 = (void *)0x0;\n','')
    assert text.count('FUN_006ee5d8(&local_a8,local_128);')==7
    text=text.replace('FUN_006ee5d8(&local_a8,local_128);','fruits[fruit_count++] = local_128[0];')
    start=text.index('                puVar30 = local_a8;')
    end=text.index('                uVar39 = *puVar30;',start)+len('                uVar39 = *puVar30;')
    text=text[:start]+'                uVar39 = (uint)*std::max_element(fruits,fruits+7);'+text[end:]
    text=re.sub(r'                FUN_0041b298\(local_128,[^;]+;', '',text)
    text=re.sub(r'                if \(\(local_128\[0\] & 1\) != 0\) \{.*?\n                }','',text,flags=re.S)
    text=re.sub(r'                if \(local_a8 != \(uint \*\)0x0\) \{.*?\n                }','',text,flags=re.S)
    text=text.replace('"ScoreBonusMap.json" + param_1 + 0xb','0').replace('PTR_DAT_00c1b680','0xc24024')
    text=text.replace('goto LAB_006ece44;','return;')
    assert not any(v in text for v in ['operator_','local_a8','local_a0','local_98','local_110','local_100','local_118','PTR_DAT_'])
    return 'void FUN_006ed8d4(long param_1,long param_2,int param_3,int param_4)\n{\n  int iVar13;int iVar15;int iVar16;ulong uVar24;ulong uVar26;ulong uVar39;ulong uVar23=(uint)param_4;int local_128[1];int fruits[7];int fruit_count=0;int *piVar40;long puVar32;\n  piVar40=(int *)(param_1+0x84080+(long)param_3*0xc804+uVar23*0x3ec);\n'+text+'\n  return;\nLAB_006ed314:\n  FUN_00a94274(param_3,uVar23 & 0xffffffff,0);return;\nLAB_006ed4b0:\n  piVar40[4] = piVar40[4] + *(int *)(puVar32+(long)iVar13*4);return;\n}\n'


def block_end(text,start):
    depth=0
    for index in range(start,len(text)):
        depth+=(text[index]=='{')-(text[index]=='}')
        if not depth:return index
    raise ValueError('Unclosed block')


def attack_source(enemy_side):
    text=clean(source('006d6d04'));address='006d8cf8' if enemy_side else '006d8584'
    start=text.index('LAB_'+address+':')+len('LAB_'+address+':')
    opening=text.index('{',text.index('if ((iVar30 == 2)',start))
    head=text[start:block_end(text,opening)+1]
    if enemy_side:
        opening=head.index('{',head.index('if (iVar31 == iVar36)'))
        end=block_end(head,opening)
        start=head.index('                        uVar43 = 0;',opening)
        head=head[:start]+'                        ctx.selectAttack(1,uVar76,iVar30);\n'+head[end:]
        head=head.replace('LAB_006d8d68:\n','')
        extra=''
    else:
        opening=head.index('{',head.index('if (0 < iVar30)'))
        end=block_end(head,opening)
        start=head.index('                    *(int *)(param_1 + 0x5255b) = 0;',opening)
        head=head[:start]+'                    ctx.selectAttack(0,uVar76,iVar31);return;\n'+head[end:]
        start=text.index('code_r0x006d8614:')
        extra=text[start:text.index('LAB_006db348:',start)].replace('goto LAB_006d854c;','return;')
    head=head.replace('local_420','param_2')
    assert not any(value in head+extra for value in ['operator_','param_1[','local_','plVar','piVar'])
    return 'void FUN_'+address+'(long param_1,long param_2,int param_3)\n{\n  int iVar30;int iVar31;int iVar36;undefined4 uVar33;ulong uVar76=(uint)param_3;'+('int iVar38;ulong uVar46;bool bVar27;' if not enemy_side else '')+'\n'+head+'\n  return;\n'+extra+'\n}\n'


def attack_wait_source(enemy_side):
    text=clean(source('006d6d04'))
    if enemy_side:
        start=text.index('              uVar46 = FUN_00a94234(1,uVar76 & 0xffffffff);',text.index('LAB_006d854c:'))
        end=text.index('\nLAB_006d8cf8:',start)
        head=text[start:end].replace('goto LAB_006d8cf8;','return;')
        address='006d8cc0';setup='bool bVar26=ctx.intentBlocked;undefined4 uVar33;'
    else:
        start=text.index('              if ((piVar62[1] == 1)',text.index('0x33312c'))
        end=text.index('\nLAB_006d8584:',start)
        head=text[start:end].replace('goto LAB_006d8584;','return;')
        address='006d8558';setup='int *piVar62;piVar62=(int *)(param_1+0x84080+(long)param_3*0x3ec);'
    head=head.replace('local_420','param_2')
    return 'void FUN_'+address+'(long param_1,long param_2,int param_3)\n{\n  int iVar30;int iVar31;bool bVar27;ulong uVar46;uint uVar43;ulong uVar76=(uint)param_3;'+setup+'\n'+head+'\n}\n'


def intent_source():
    text=clean(source('006d6d04'))
    start=text.index('          uVar32 = 0;',text.index('          FUN_006eccf4('))
    end=text.index('          if (*(int *)((long)param_1 + 0x33312c)',start)
    return 'void FUN_006d823c(long param_1)\n{\n  bool bVar26=true;bool bVar27;bool bVar59;uint uVar32;int uVar33;undefined4 uVar39;ulong uVar76;int iVar30;int iVar31;int iVar36;long lVar65;long lVar66;\n'+text[start:end]+'\n  ctx.intentBlocked=bVar26;\n}\n'


def retirement_source(enemy_mode):
    text=clean(source('006eccf4' if enemy_mode else '006eb464'))
    address='006ed5e0' if enemy_mode else '006ebb0c'
    start=text.index('LAB_'+address+':')+len('LAB_'+address+':')
    end=text.index('\n  else {',start)
    head=text[start:end]
    # モデル8と魂ID+1000の読込だけを、同じ取得経路で解決した長さへ置換する。
    head=re.sub(r'      uVar(?:14|15) = FUN_005bc1dc.*?      if \(iVar(?:15|18) < 2\)',
        '      '+('iVar15' if enemy_mode else 'iVar18')+' = ctx.retirement->body_frames;\n      if ('+('iVar15' if enemy_mode else 'iVar18')+' < 2)',head,flags=re.S)
    start=head.index('      '+('iVar13' if enemy_mode else 'local_90')+' = FUN_00a95544',head.index('if (-1 <'))
    end=head.index('      if (iVar',start)
    head=head[:start]+('      iVar13' if enemy_mode else '      iVar14')+' = ctx.retirement->soul_frames;\n'+head[end:]
    start=text.index('LAB_006ed9b8:' if enemy_mode else 'LAB_006ec5d0:')
    tail=text[start:text.index('LAB_006ece44:' if enemy_mode else 'LAB_006eb6a4:',start)]
    if enemy_mode:
        tail=tail.replace('bVar11','!ctx.retirement->blocked')
        locals='int iVar13;int iVar15;int iVar16;ulong uVar24;int *piVar40;piVar40=(int *)(param_1+0x84080+(long)param_3*0xc804+(long)param_4*0x3ec);ulong uVar23=(uint)param_4;'
    else:
        tail=tail.replace('bVar13','!ctx.retirement->blocked')
        tail=tail.replace('*(undefined4 *)(lVar36 + 0x26e4 + (long)iVar14 * 4) = 0;','ctx.retirementResult->reset_production=1;ctx.retirementResult->production_slot=iVar14;')
        tail=tail.replace('*(int *)(lVar27 + 0x30)','ctx.retirementResult->cannon_remaining')
        tail=tail.replace('*(undefined8 *)(puVar37 + 0x1c) = 0;','puVar37[0x1c]=0;puVar37[0x1d]=0;')
        locals='int iVar14;int iVar17;int iVar18;ulong uVar23;ulong uVar38=(uint)param_4;undefined4 *puVar37;puVar37=(undefined4 *)(param_1+0x84080+(long)param_3*0xc804+(long)param_4*0x3ec);'
    tail=tail.replace('*piVar40 = 0;','*piVar40 = 0;ctx.retirementResult->removed=1;').replace('*puVar37 = 0;','*puVar37 = 0;ctx.retirementResult->removed=1;')
    tail=re.sub(r'LAB_(?:006ec5d0|006ec5dc|006ed9b8):\n','',tail)
    assert not any(v in head+tail for v in ['operator_','local_','FUN_005bde34','FUN_0065c134'])
    return 'void FUN_'+address+'(long param_1,long param_2,int param_3,int param_4)\n{\n'+locals+'\n'+head+'\n'+tail+'\n}\n'


def enemy_knockback_source():
    text=clean(source('006eccf4'))
    start=text.index('      iVar13 = FUN_00a94234(param_3,uVar23 & 0xffffffff);\n      if (iVar13 == 3)')
    end=text.index('\n      iVar13 = FUN_00a94234',start+20)
    text=text[start:end]
    start=text.index('              local_128[0] = 0xffffffff;')
    end=text.index('LAB_006eddfc:',start)+len('LAB_006eddfc:')
    text=text[:start]+'              local_184 = ctx.enemyCredit(param_3,uVar23);'+text[end:]
    text=text.replace('*(undefined8 *)(param_1 + 0x3310) = uVar12;',
        'ctx.enemyDeathResult->score_updated=1;ctx.enemyDeathResult->score_display='+hex(struct.unpack_from('<Q',binary,segment_at(0x2b2820))[0])+'ULL;')
    start=text.index('              uVar24 = FUN_00a0b03c')
    end=text.index('              uVar24 = FUN_005e1400',start)
    text=text[:start]+'''              if (ctx.enemyDeath->recording && ctx.enemyDeath->game_mode!=4 && ctx.enemyDeath->game_mode!=7) {
                ctx.enemyDeathResult->record_requested=1;
                ctx.enemyDeathResult->record_values[0]=ctx.enemyDeath->money_base/100;
                ctx.enemyDeathResult->record_values[1]=FUN_00a9526c(param_3,uVar23 & 0xffffffff);
              }
'''+text[end:]
    start=text.index('                  if (0 < local_184) {')
    end=text.index('\n                  }',start)+len('\n                  }')
    text=text[:start]+'                  if (0 < local_184) ctx.enemyDeathResult->bonus_visual_slot=ctx.enemyDeathResult->selected_bonus_slot;'+text[end:]
    text=text.replace('PTR_DAT_00c1b630','0xc23fc4').replace('goto LAB_006ece44;','return;')
    assert 'goto LAB_006ed4b0;' not in text
    text=text.replace('LAB_006ed4b0:', '')
    text=text.replace("*(char *)(param_1 + 0x32e9) == '\\0'",'!ctx.enemyDeath->quiet')
    assert text.count('{')==text.count('}')
    assert not any(v in text for v in ['operator_','local_a8','local_128','local_c8','plVar','puVar28','uVar12','PTR_DAT_'])
    return 'void FUN_006ed43c(long param_1,long param_2,int param_3,int param_4)\n{\n  int iVar13;int iVar15;int local_184;undefined4 uVar14;ulong uVar23=(uint)param_4;ulong uVar24;ulong uVar26;long lVar25;int *piVar40;long puVar32;\n  piVar40=(int *)(param_1+0x84080+(long)param_3*0xc804+uVar23*0x3ec);\n'+text+'\n}\n'


CUSTOM = {'0044a8d8', '0044abfc', '0044abe4', '00457e1c', '00459efc', '005bbbc8', '005bbc10', '005bbfb0', '005c2710',
          '0044beb4','0044bf2c','00459f04','00a9490c','005bc058','005be130','005c2990',
          '005bc1dc','005bde34','006fce54','00a93074',
          '0063c178','0068c330','008cfcf0','0063c480','0063a050','00a5b1b4','005bc198','009d49e4','009d4e1c',
          '00a960ac','00a5b084','0058b674','005bbba0','005e1400','006440f0','007cf950',
          '005c2ec0', '0066398c', '00663af4', '00656de0', '0081f580', '0088f9e4',
          '005bce20','00663c44','0063c21c','0068c30c','0063c3a0','0066367c', '00a9e9fc', '00a9fb88', '00a9f9fc', '00a9f0e0', '00aa2c2c', '00aa4fb0', '00aa68ec'}
constructor = clean(source('009f1e64'))
# 文字列構築/解放はparam.tsvのキー参照へ置換し、分岐と既定値は保持する。
constructor = re.sub(r'            local_70 = operator_new.*?            FUN_00a98b40',
                     '            uVar7 = ctx.parameter(0,600);\n            FUN_00a98b40', constructor, flags=re.S)
constructor = re.sub(r'            if \(\(local_80 & 1\).*?            FUN_00a98bcc',
                     '            uVar7 = ctx.parameter(1,4000);\n            FUN_00a98bcc', constructor, flags=re.S)
constructor = re.sub(r'            if \(\(local_a0 & 1\).*?            FUN_00a98c58',
                     '            FUN_00a98c58', constructor, flags=re.S)
# ARM64の2レジスタ戻り値を持つ城設定は、照合済みの整数位置関数に接続する。
constructor = re.sub(r'            iVar9 = FUN_00a92ea0\(1\);.*?\(extraout_w1_01 \* 0x7f\) / 10\);',
                     '            FUN_00a9486c(param_2,uVar16,ctx.bossPosition());', constructor, flags=re.S)
# 009f4158..416cはW2へ加算前の生成通番を読み、W8だけを+1して保存する。
# Ghidraの呼出式で欠けた第3引数を、直前の本能玉値で代用しない。
constructor = constructor.replace('FUN_00a95738(param_2,uVar16);',
    'FUN_00a95738(param_2,uVar16,*(uint *)(lVar14 + 0x284c) - 1U);')
# TLSスタック保護はホストABIの担当。ゲーム状態の分岐から外す。
constructor = re.sub(r'  lVar1 = tpidr_el0;\n  local_68 = \*\(long \*\)\(lVar1 \+ 0x28\);\n', '', constructor)
constructor = re.sub(r'  if \(\*\(long \*\)\(lVar1 \+ 0x28\) == local_68\) \{\n    return uVar16;\n  \}\n  __stack_chk_fail\(\);',
                     '  return uVar16;', constructor)

effects,effect_keys=effect_source()
ROOTS = {'005d6c3c','005d6740','005bf7d8','006e4aec','006e79bc','006e60f0','009f1e64', '006dda04', '006e9c88', '006ec9f4','006e62f8','006dde48','005ce03c','006e3f80','00a962a8','009f4688','00a9bbac','005bbc90','005bb5f0','006d97dc','006da994','006dac8c','006ecae4','006eb6b0','006eb8c0','006ecfec','006eb7e0','006ed8d4','006ed43c','0058bef8','006ebb0c','006ed5e0','006d823c','006d8558','006d8cc0','006d8584','006d8cf8','00a97980','00a94630','00a9adf0','00a97a14','00a97b38','00a97b78'}
pending = list(ROOTS)
pending.extend(['00a9467c','00a932e8','00a93914','00a93988','00a93b6c','00a93b2c','00a93b38','00a93b0c','00a93b18','00a93b4c','00a93b58'])
pending.extend(['00a9be18','00a9b0b8','00a98838','00a988c4','00a98950','00a989dc','00a987f8','00a98f70','00a98ffc','00a99088'])
pending.extend(['00a98dbc','00a98edc','00a98e04','00a98f24','00a98e50','00a98ca4','00a98c18','00a98b00','00a98b8c','00a98d30'])
# getterのW0→abs→RNGへ直接渡す3命令。+1を補った解釈にしない。
for at, getter in [(0x6e98c0,0xa98950),(0x6ea788,0xa98950),(0x6e9ae8,0xa99088),(0x6ea9b0,0xa99088)]:
    expected=tuple(0x94000000|(((target-at-i*4)//4)&0x3ffffff) for i,target in enumerate([getter,0x44ab70,0x44a8d8]))
    assert struct.unpack_from('<III',binary,segment_at(at))==expected
functions = {}
while pending:
    address = pending.pop()
    if address in functions or address in CUSTOM:
        continue
    text = cannon_hit(source,clean) if address=='005d6c3c' else hit_source(source,clean,address=='006e79bc') if address in ('006e4aec','006e79bc') else attack_source(address=='006d8cf8') if address in ('006d8584','006d8cf8') else attack_wait_source(address=='006d8cc0') if address in ('006d8558','006d8cc0') else intent_source() if address=='006d823c' else retirement_source(address=='006ed5e0') if address in ('006ebb0c','006ed5e0') else enemy_knockback_source() if address=='006ed43c' else displacement_source() if address=='006ed8d4' else knockback_source() if address=='006eb7e0' else walk_source(address=='006ecfec') if address in ('006eb8c0','006ecfec') else begin_source() if address=='006eb6b0' else reaction_source() if address=='006dac8c' else health_source() if address=='006da994' else protection_source() if address=='006d97dc' else constructor if address == '009f1e64' else effects if address=='006e62f8' else strengthen_source() if address=='00a999e4' else motion_source() if address=='009f4688' else clean(source(address))
    if address=='005d6740':
        text=text.replace('*(int *)PTR_DAT_00c1b578','*(int *)(0xc24400)')
        # 原本int*の+0xfbは個体251語（1004byte）。整数アドレス化の前に保持する。
        text=text.replace('piVar14 = piVar14 + 0xfb;', 'piVar14 = (int *)((long)piVar14 + 0x3ec);')
    if address=='006e60f0':
        text=text.replace('FUN_00a969c8(0)', 'FUN_00a969c8(0,param_2)')
    if address in ('00a94c60','00a94d0c'):
        # 先頭の呼出はX0/W1/W2をそのまま渡す。Ghidraが省略した実引数を戻す。
        text=text.replace('FUN_00a9490c();','FUN_00a9490c(param_1,param_2,param_3);')
    if address in ('00a93b04','00a93b24','00a93b44','00a93b64'):
        text=text.replace('void FUN_', 'undefined4 FUN_',1)
        text=re.sub(r'  (FUN_\w+\(param_1,0\));\n  return;',r'  return \1;',text)
    if address in ('00a92f34','00a92f48'):
        target=0xa95824 if address=='00a92f34' else 0xa958b0
        at=int(address,16)
        # 先頭はmov w1,wzr; b getter。voidと復元されてもW0の戻り値を保持する。
        assert struct.unpack_from('<II',binary,segment_at(at))==(0x2a1f03e1,0x14000000|((target-at-4)//4))
        text=text.replace('void FUN_', 'undefined4 FUN_',1)
        text=re.sub(r'  (FUN_\w+\(param_1,0\));\n  return;',r'  return \1;',text)
    functions[address] = text
    pending.extend(re.findall(r'FUN_([0-9a-f]+)\(', text)[1:])
assert not any(a.startswith(('004','005','006')) and a not in ROOTS for a in functions), sorted(functions)

TYPES = {'undefined1': 'uint8_t', 'byte': 'uint8_t', 'undefined2': 'uint16_t',
         'undefined4': 'uint32_t', 'undefined8': 'uint64_t', 'uint': 'uint32_t',
         'ulong': 'uint64_t', 'long': 'int64_t', 'int': 'int32_t'}
WIDTHS = {'undefined1': 'u8', 'byte': 'u8', 'undefined2': 'u16', 'undefined4': 'u32',
          'undefined8': 'u64', 'uint': 'u32', 'ulong': 'u64', 'long': 's64', 'int': 's32'}
constants = set()


def translate(text):
    # ヒープを伴わない原本helperだけを受理する。
    assert 'operator_' not in text and 'tpidr_el0' not in text and '__stack' not in text
    text=text.replace('(void)','()')
    text=re.sub(r'"ScoreBonusMap.json" \+ (?:param_\d+|lVar\d+) \+ 0xb','0',text)
    text = text.replace('param_6 - param_5 >> 0x1f', '(param_6 - param_5) >> 0x1f')
    # 省略したTLS/文字列構築にしか使われない一時変数を出力しない。
    text = re.sub(r'^  (?:(?:int|uint|long|ulong|bool|byte|char|undefined[12468])\s+\*?)(\w+);\n',
                  lambda m: '' if len(re.findall(r'\b'+m[1]+r'\b',text))==1 else m[0], text, flags=re.M)
    text = re.sub(r'\(&DAT_([0-9a-f]{8})\)\[([^\]]+)\]',
                  lambda m: '*(int *)(&DAT_' + m[1] + '+(' + m[2] + ')*4)', text)
    pointer_names = dict((name,kind) for kind,name in re.findall(r'\b(int|uint|undefined4|undefined8|long) \*(\w+)\s*;', text))
    pointer_names.update((name,kind) for kind,name in re.findall(r'\b(int|uint|undefined4|undefined8|long) \*(param_\d+)\s*[,)]',text))
    for name,kind in pointer_names.items():
        text = re.sub(r'\b'+name+r'\[([^\]]+)\]',lambda m:'ctx.'+WIDTHS[kind]+'('+name+'+('+m[1]+')*'+str(8 if kind in ('long','undefined8') else 4)+')',text)
    text = re.sub(r'\b(?:int|uint|undefined4|undefined8|long) \*(\w+)\s*;', r'int64_t \1;', text)
    text = re.sub(r'\b(?:int|uint|undefined4|undefined8|long) \*(param_\d+)\b',r'int64_t \1',text)
    pattern = re.compile(r'\*\s*\(\s*(undefined[1248]|byte|int|uint|ulong|long)\s*\*\s*\)\s*\(')
    while match := pattern.search(text):
        start = match.end() - 1
        end = closing(text, start)
        expression = text[start + 1:end]
        text = text[:match.start()] + 'ctx.' + WIDTHS[match[1]] + '(' + expression + ')' + text[end + 1:]
    for name,kind in pointer_names.items():
        text = re.sub(r'\*' + name + r'\b', 'ctx.'+WIDTHS[kind]+'(' + name + ')', text)
    text = re.sub(r'\((?:int|uint|undefined4|undefined8|long) \*\)', '(int64_t)', text)
    text = text.replace('(long)__DT_JMPREL', '0x22fa38')
    for address in re.findall(r'&DAT_([0-9a-f]{8})', text):
        constants.add(int(address, 16))
    text = re.sub(r'&DAT_([0-9a-f]{8})', r'0x\1', text)
    text = re.sub(r'&uleb128_([0-9a-f]{8})', r'0x\1', text)
    text = re.sub(r'&lsda_exception_table_([0-9a-f]{8})', r'0x\1', text)
    text = re.sub(r'&(?:DWORD|QWORD|fde)_([0-9a-f]{8})',r'0x\1',text)
    text = re.sub(r'FUN_([0-9a-f]+)\(', r'n_\1(ctx,', text).replace('(ctx,)', '(ctx)')
    for before, after in TYPES.items():
        text = re.sub(r'\b' + before + r'\b', after, text)
    text = text.replace('CONCAT44(', 'concat32(')
    text=text.replace('ctx.s64(lVar6 + 0x9ee78) - ctx.s64(lVar6 + 0x9ee70) >> 3',
        '(ctx.s64(lVar6 + 0x9ee78) - ctx.s64(lVar6 + 0x9ee70)) >> 3')
    # 原本のアドレスとif/else/gotoを保持し、差分を追えるようにする。
    signature, body = text.split('{', 1)
    for parameter in re.findall(r'\bparam_\d+\b',signature):
        if not re.search(r'\b'+parameter+r'\b',body):signature=re.sub(r'\b'+parameter+r'\b','',signature)
    signature = signature.replace('(ctx,', '(Context &ctx,').replace('(ctx)', '(Context &ctx)')
    # Ghidraが復元した引数以降のARM64レジスタは、このhelperでは参照されない。
    signature = signature.rstrip().removesuffix(')') + ',...)'
    signature = signature.replace('(Context &ctx,,...)', '(Context &ctx,...)')
    return ('[[maybe_unused]] ' if 'n_006ec9f4(' in signature else '') + signature.strip() + ' {\n' + body


translated = {address: translate(text) for address, text in sorted(functions.items())}
prototypes = []
for text in translated.values():
    prototypes.append(text.split('{', 1)[0].strip() + ';')


def read_word(address):
    phoff = struct.unpack_from('<Q', binary, 32)[0]
    phsize, count = struct.unpack_from('<HH', binary, 54)
    for index in range(count):
        kind, _, offset, virtual, _, size = struct.unpack_from('<IIQQQQ', binary, phoff + index * phsize)
        if kind == 1 and virtual + 0x100000 <= address < virtual + 0x100000 + size:
            return struct.unpack_from('<i', binary, offset + address - virtual - 0x100000)[0]
    raise ValueError(hex(address))


rom = {a + i * 4: read_word(a + i * 4) for a in sorted(constants) for i in range(6)}
# 同版GOT c1b630/c1b680のRELATIVE addendはc23fc4/c24024。使用される全要素を保持する。
rom.update({a+i*4:read_word(a+i*4) for a,count in [(0xc23fc4,24),(0xc24024,12)] for i in range(count)})
# 烈波の幅/発生待ち/周期/終了待ち/接触補正。同版GOT c1b580..5a0の参照先。
rom.update({0xc23e68+i*4:read_word(0xc23e68+i*4) for i in range(5)})
# c1b578の同版RELATIVE addendはc24400。波動の距離係数。
rom[0xc24400]=read_word(0xc24400)
# 波動の初期状態は陣営別。32bit状態と時計0をまとめた64bit定数も同版SOへ固定する。
for address,value in [(0x2b2820,1),(0x2b2938,2)]:
    assert struct.unpack_from('<Q',binary,segment_at(address))[0]==value
header = '// 生成元: research/cli/export_actor.py。JP15.7.2 ARM64、原本の分岐を保持する。\n'
output = header + '\n'.join(prototypes) + '\n\n' + '\n\n'.join(translated.values())
target = ROOT / 'native/kbcs-core/src/actor_generated.inc'
output = adapt_actor_pool(output)
target.write_bytes(b'\xef\xbb\xbf' + '\n'.join(line.rstrip() for line in output.split('\n')).encode('utf-8'))
(ROOT / 'native/kbcs-core/src/actor_rom.inc').write_text('static constexpr std::pair<int64_t,int32_t> actorRom[] = {\n' +
    ',\n'.join(' {0x%x,%d}'%(a,v) for a,v in sorted(rom.items()))+'\n};\n',encoding='utf-8')
manifest = {'version': '15.7.2', 'architecture': 'arm64-v8a', 'sha256': SHA,
            'functions': {a: {'sha256': hashlib.sha256(source(a).encode()).hexdigest(),
                             'branches': len(re.findall(r'\bif\s*\(', source(a)))} for a in functions},
            'fragments': {
                '006d823c': {'source':'006d6d04','terminal':'006d8510'},
                '006d8558': {'source':'006d6d04','terminals':['006d8584','006d854c']},
                '006d8584': {'source':'006d6d04','terminal':'006d854c','sink':'006e92bc'},
                '006d8cc0': {'source':'006d6d04','terminals':['006d8cf8','006d8cb4']},
                '006d8cf8': {'source':'006d6d04','terminal':'006d8cb4','sink':'006ea1c0'},
                '006d97dc': {'source':'006d6d04','terminal':'006d9da0'},
                '006da994': {'source':'006d6d04','terminal':'006dac68'},
                '006dac8c': {'source':'006d6d04','terminal':'006db1ac'},
                '006eb6b0': {'source':'006eb464','terminal':'006eb7d8','enemySource':'006eccf4','enemyTerminal':'006ecf90','enemySha256':hashlib.sha256(source('006eccf4').encode()).hexdigest()},
                '006eb7e0': {'source':'006eb464','terminal':'006eb6a4'},
                '006eb8c0': {'source':'006eb464','terminal':'006eb6a4'},
                '006ebb0c': {'source':'006eb464','terminal':'006eb6a4','actions':[4]},
                '006ecfec': {'source':'006eccf4','terminal':'006ece44'},
                '006ed43c': {'source':'006eccf4','terminal':'006ece44','actions':[3]},
                '006ed5e0': {'source':'006eccf4','terminal':'006ece44','actions':[4]},
                '006ed8d4': {'source':'006eccf4','terminal':'006ece44','actions':[5,6]}},
            'emission': {'unitSource':'006e92bc','enemySource':'006ea1c0',
                'unitSha256':hashlib.sha256(source('006e92bc').encode()).hexdigest(),
                'enemySha256':hashlib.sha256(source('006ea1c0').encode()).hexdigest(),
                'directTerminals':['006e95f4','006ea4bc'],'waveTerminals':['006e9768','006ea62c'],
                'waveStateConstants':{'002b2820':1,'002b2938':2},'waveFlagOrder':[0,1,2,3,4,6,8,7,5,9,10,11]},
            'secondarySources': {a:hashlib.sha256(source(a).encode()).hexdigest() for a in ['005d3af8','005d4158','005d4988','006eaef0','006eb364','006eb464','006eccf4']},
            'surgeGot': {hex(got):hex(target) for got,target in zip(range(0xc1b580,0xc1b5a8,8),range(0xc23e68,0xc23e7c,4))},
            'custom': sorted(CUSTOM), 'effectParameters':effect_keys,'rom': {hex(a): v for a, v in rom.items()}}
(ROOT / 'research/.local/actor-bindings.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8-sig')
print(json.dumps({'functions': len(functions), 'bytes': target.stat().st_size, 'rom': manifest['rom']}))

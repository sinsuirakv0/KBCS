"""砲命中の原本分岐を保持し、表示用文字列と参照コンテナだけを入力へ置換する。"""
import re

def cannon_hit(source, clean):
    text = clean(source('005d6c3c'))
    text = re.sub(r'  lVar1 = tpidr_el0;\n  local_68 = \*\(long \*\)\(lVar1 \+ 0x28\);\n', '', text)
    # 水鉄砲とエンジェル砲のmapはダメージ式で使わず、表示名の連結にしか使わない。
    for end in ['          uVar9 = FUN_00a96cd8', '            uVar9 = FUN_00a96ff8']:
        start = text.index('          iVar6 = FUN_00a93320' if '96cd8' in end else '            iVar6 = FUN_00a93320')
        stop = text.index(end, start)
        text = text[:start] + text[stop:]
    start = text.index('          iVar4 = FUN_00a93320(param_2);\n          if (iVar4 == 0)')
    stop = text.index('          iVar4 = FUN_00a933f8', start)
    text = text[:start] + text[stop:]
    # ステージの砲攻撃補正（ルール9）。空配列はホストが不正な入力として拒否する。
    start = text.index('              uVar7 = FUN_007cf950')
    stop = text.index('          }\n            FUN_00a9bbac',start) if False else text.index('            FUN_00a9bbac', start)
    prefix = text[:start]
    # このifの終端までを置換し、外側のmetal判定は残す。
    text = prefix + '              iVar4 = (ctx.cannonRules->attack_rate * iVar4) / 100;\n            }\n' + text[stop:]
    text = re.sub(r' +if \(\(local_\w+\[0\] & 1\) != 0\) \{\n.*?operator_delete.*?;\n +\}', '', text, flags=re.S)
    text = re.sub(r'^ +FUN_(?:0041b298|00a94074)\([^;]+;\n', '', text, flags=re.M)
    text = text.replace('      pbVar15 = (basic_string *)(uVar9 & 0xffffffff);', '')
    text = text.replace('FUN_00a94f4c(uVar17 & 0xffffffff,param_3);','FUN_00a94f4c(uVar17 & 0xffffffff,param_3,uVar9);')
    text = text.replace('thunk_FUN_00a94484(', 'FUN_00a94484(')
    text = re.sub(r'  if \(\*\(long \*\)\(lVar1 \+ 0x28\) == local_68\) \{\n    return;\n  \}\nLAB_005d75d0:\n  __stack_chk_fail\(\);', '  return;', text)
    text = re.sub(r'^ +(?:puVar14|pbVar15) = .*?;\n', '', text, flags=re.M)
    text = text.replace('  basic_string *pbVar15;','').replace('  undefined *puVar14;','')
    text = re.sub(r'if \(\*\(long \*\)\(lVar1 \+ 0x28\) == local_68\) \{\n +return;\n +\}\n +goto LAB_005d75d0;', 'return;', text)
    text = re.sub(r'if \(\*\(long \*\)\(lVar1 \+ 0x28\) == local_68\) \{\n(.*?)\n +\}\n +goto LAB_005d75d0;', r'\1', text, flags=re.S)
    text = text.replace('DAT_002b29a0','0x100000000ULL')
    text = text.replace('{\n  long lVar1;', '{\n  ctx.events->count=0;\n  long lVar1;', 1)
    assert not any(v in text for v in ['operator_', 'tpidr', '__stack', 'plVar12[', 'puVar11[', 'pbVar15', 'puVar14'])
    return text
